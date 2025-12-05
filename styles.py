CUSTOM_CSS = """
    <style>
    /* Set main background color */
    .stApp {
        background-color: #FFF9F0 !important;
    }
    
    /* Target user messages by finding the parent of stChatMessageAvatarUser */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        flex-direction: row-reverse !important;
        background-color: #F0F2F6 !important;
    }
    
    /* Change user message content background color */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] {
        background-color: #F0F2F6 !important;
    }
    
    /* Target the inner markdown container too */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown {
        background-color: #F0F2F6 !important;
    }
    
    /* Target assistant messages by finding the parent of stChatMessageAvatarAssistant */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
        background-color: #FFF9F0 !important;
    }
    
    /* Change assistant message content background color */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) div[data-testid="stChatMessageContent"] {
        background-color: #FFF9F0 !important;
    }
    
    /* Target the inner markdown container for assistant too */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) .stMarkdown {
        background-color: #FFF9F0 !important;
    }
    
    /* Sidebar branding section */
    .sidebar-branding {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        margin-top: 0.5rem;
    }
    
    .sidebar-branding h1 {
        color: white;
        font-size: 2rem;
        margin-bottom: 0.75rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .sidebar-branding p {
        color: rgba(255, 255, 255, 0.95);
        font-size: 0.9rem;
        line-height: 1.5;
        margin-bottom: 0;
    }
    
    /* Stylized button */
    .stButton > button {
        width: 100%;
        background: white !important;
        color: #667eea !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stButton > button:hover {
        background: #f8f9fa !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }
    </style>
"""
