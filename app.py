import streamlit as st
import ollama
import PyPDF2
import os
from io import BytesIO
from PIL import Image
from system_prompt import SYSTEM_PROMPT
from styles import CUSTOM_CSS
from st_copy import copy_button

# Load environment variables from .env file
def load_env_file():
    """Simple .env file parser"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    # Remove quotes if present
                    value = value.strip().strip("'\"")
                    os.environ[key.strip()] = value
    
load_env_file()

# Model configuration
MODEL_MAPPING = {
    "Gemma3:4b": {"name": "gemma3:4b", "type": "local"},
    "Kimi K2:1T": {"name": "kimi-k2:1t", "type": "cloud"}
}

# Load API key from environment
OLLAMA_API_KEY = os.getenv('ollama_api_key')

def get_ollama_client(model_display_name):
    """Get appropriate Ollama client based on selected model"""
    model_config = MODEL_MAPPING.get(model_display_name)
    
    if not model_config:
        # Default to local if model not found
        return ollama.Client()
    
    if model_config["type"] == "cloud":
        # Use cloud API with authentication
        return ollama.Client(
            host='https://ollama.com',
            headers={'Authorization': f'Bearer {OLLAMA_API_KEY}'}
        )
    else:
        # Use local Ollama
        return ollama.Client()

def process_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            # For .txt files
            return uploaded_file.getvalue().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            # For .pdf files
            try:
                pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.getvalue()))
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
            except Exception as e:
                return f"Error reading PDF: {e}"
    return None

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                'role': 'system',
                'content': SYSTEM_PROMPT
            },
            {
                'role': 'assistant',
                'content': "Hi, I'm Sammy, your creative writing assistant. What great story are we going to write today?"
            }
        ]

def reset_chat():
    """Reset the chat to initial state"""
    st.session_state.messages = [
        {
            'role': 'system',
            'content': SYSTEM_PROMPT
        },
        {
            'role': 'assistant',
            'content': "Hi, I'm Sammy, your creative writing assistant. What great story are we going to write today?"
        }
    ]

def display_chat_history():
    for message in st.session_state.messages:
        if message["role"] != "system" and message["role"] != "hidden_content":
            avatar = "Sammy.png" if message["role"] == "assistant" else None
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    copy_button(message["content"])

def handle_user_input():
    if prompt := st.chat_input("What would you like to write about?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar="Sammy.png"):
            with st.spinner("Sammy is thinking..."):
                # Get the selected model information
                selected_model_display = st.session_state.selected_model
                model_config = MODEL_MAPPING.get(selected_model_display)
                model_name = model_config["name"] if model_config else "gemma3:4b"
                
                # Get appropriate client (local or cloud)
                client = get_ollama_client(selected_model_display)
                
                # Generate response using selected model and client
                response = client.chat(
                    model=model_name,
                    messages=[
                        {"role": "user" if m["role"] == "hidden_content" else m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response_container = st.empty()
                full_response = ""
                for chunk in response:
                    full_response += chunk['message']['content']
                    response_container.markdown(full_response + "▌")
                response_container.markdown(full_response)
                
                copy_button(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

def main():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    initialize_session_state()
    
    # Sidebar on the left with branding and controls
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-branding">
            <h1>SammyAI</h1>
            <p>SammyAI is a free, open source creative writing assistant. SammyAI helps you create rich characters and worlds from the scratch.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # LLM selection dropdown
        if "selected_model" not in st.session_state:
            st.session_state.selected_model = "Gemma3:4b"
        
        st.session_state.selected_model = st.selectbox(
            "Select LLM Model",
            options=["Gemma3:4b", "Kimi K2:1T"],
            index=0 if st.session_state.selected_model == "Gemma3:4b" else 1
        )
        
        # Add spacing before button to match spacing after branding
        st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
        
        if st.button("Start New Chat", key="reset_button"):
            reset_chat()
            st.rerun()
    
    # Main chat area (no column wrapper)
    # Header with logo
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("Sammy.png", width=100)
    with col2:
        st.title("Sammy - Creative Writing Assistant")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
    if uploaded_file is not None:
        file_content = process_uploaded_file(uploaded_file)
        if file_content:
            st.session_state.messages.append({"role": "hidden_content", "content": f"Document content:\n{file_content}"})
            st.success("File uploaded successfully! Sammy will consider its content.")
    
    display_chat_history()
    handle_user_input()

if __name__ == "__main__":
    main()
