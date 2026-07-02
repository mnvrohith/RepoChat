def load_css():
    return """
<style>

/* Hide Streamlit default UI */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}


/* Background */

.stApp{
    background-color:#0D1117;
    color:white;
}


/* Sidebar */

section[data-testid="stSidebar"]{
    background-color:#161B22;
}


/* Buttons */

.stButton > button{
    width:100%;
    background:#238636;
    color:white;
    border:none;
    border-radius:8px;
    padding:10px;
    font-weight:bold;
}

.stButton > button:hover{
    background:#2EA043;
}


/* Inputs */

.stTextInput input{
    background:#161B22;
    color:white;
    border:1px solid #30363D;
}


/* Chat */

.user-message{

    background:#1F6FEB;

    padding:15px;

    border-radius:12px;

    margin-bottom:10px;
}


.bot-message{

    background:#21262D;

    padding:15px;

    border-radius:12px;

    margin-bottom:15px;
}


/* Cards */

.repo-card{

    background:#161B22;

    padding:18px;

    border-radius:12px;

    border:1px solid #30363D;

}

</style>
"""