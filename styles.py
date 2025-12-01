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
    </style>
"""
