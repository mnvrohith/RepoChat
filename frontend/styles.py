def load_css():
    return """
<style>

/* =========================
   Hide Streamlit Branding
========================= */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}


/* =========================
   Global
========================= */

html, body, [class*="css"] {
    font-family: Inter, "Segoe UI", sans-serif;
}

.stApp{
    background:#0D1117;
    color:#E6EDF3;
}


/* =========================
   Sidebar
========================= */

section[data-testid="stSidebar"]{
    background:#161B22;
    border-right:1px solid #30363D;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:white;
}


/* =========================
   Headers
========================= */

h1{
    color:#F0F6FC;
    font-weight:700;
}

h2,h3{
    color:#E6EDF3;
}

p,label{
    color:#C9D1D9;
}


/* =========================
   Buttons
========================= */

.stButton>button{

    width:100%;
    background:#238636;
    color:white;

    border:none;
    border-radius:10px;

    padding:12px 16px;

    font-size:15px;
    font-weight:600;

    transition:all .25s ease;
}

.stButton>button:hover{

    background:#2EA043;

    transform:translateY(-1px);

    box-shadow:0 0 12px rgba(46,160,67,.35);

    cursor:pointer;
}


/* =========================
   Text Input
========================= */

.stTextInput input{

    background:#161B22;

    color:white;

    border:1px solid #30363D;

    border-radius:10px;
}


/* =========================
   Chat Input
========================= */

[data-testid="stChatInput"]{

    border-top:1px solid #30363D;

    padding-top:12px;
}


/* =========================
   Chat Messages
========================= */

[data-testid="stChatMessage"]{

    background:#161B22;

    border:1px solid #30363D;

    border-radius:14px;

    padding:10px;

    margin-bottom:12px;
}


/* =========================
   Repository Card
========================= */

.repo-card{

    background:#161B22;

    border:1px solid #30363D;

    border-radius:12px;

    padding:18px;

    margin-bottom:12px;
}


/* =========================
   Expanders (Sources)
========================= */

details{

    background:#161B22;

    border:1px solid #30363D;

    border-radius:10px;

    padding:8px;
}


/* =========================
   Code Blocks
========================= */

code{

    color:#7EE787;

    background:#21262D;

    padding:2px 5px;

    border-radius:5px;
}

pre{

    background:#161B22 !important;

    border:1px solid #30363D;

    border-radius:10px;
}


/* =========================
   Divider
========================= */

hr{
    border-color:#30363D;
}


/* =========================
   Success / Warning
========================= */

.stSuccess{

    border-radius:10px;
}

.stWarning{

    border-radius:10px;
}

.stError{

    border-radius:10px;
}

</style>
"""