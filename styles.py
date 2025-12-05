CUSTOM_CSS = """
    <style>
    /* Set main background color */
    .stApp {
        background-color: #FFF9F0 !important;
    }
    
    /* Set header background color */
    header[data-testid="stHeader"] {
        background-color: #FFF9F0 !important;
    }
    
    /* Set footer background color */
    footer[data-testid="stFooter"] {
        background-color: #FFF9F0 !important;
    }
    
    /* Set main content area background */
    .main {
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
        background: transparent;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1.5rem;
        margin-top: 0.5rem;
    }
    
    .sidebar-branding h1 {
        color: black;
        font-size: 2rem;
        margin-bottom: 0.75rem;
        font-weight: 700;
    }
    
    .sidebar-branding p {
        color: black;
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
        border-radius: 10px !important;
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
