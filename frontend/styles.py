
def load_css():
    return """
<style>

/* ========= Hide Streamlit ========= */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* ========= Theme ========= */
:root{
 --bg:#0F172A;
 --sidebar:#111827;
 --card:#1E293B;
 --border:#334155;
 --primary:#6366F1;
 --primary-hover:#4F46E5;
 --text:#F8FAFC;
 --secondary:#CBD5E1;
 --success:#22C55E;
}

html,body,[class*="css"]{
 font-family:Inter,"Segoe UI",Roboto,sans-serif;
 color:var(--text);
}

.stApp{
 background:var(--bg);
 color:var(--text);
}

/* ========= Layout ========= */
.block-container{
 max-width:1500px;
 padding-top:1.5rem;
 padding-left:2rem;
 padding-right:2rem;
 padding-bottom:1rem;
}

/* ========= Sidebar ========= */
section[data-testid="stSidebar"]{
 background:var(--sidebar);
 border-right:1px solid var(--border);
}
section[data-testid="stSidebar"] .block-container{
 padding-top:2rem;
}
section[data-testid="stSidebar"] h1{
 font-size:28px;
 font-weight:700;
 color:var(--text);
}

/* ========= Text ========= */
h1,h2,h3{
 color:var(--text);
}
p,label,span{
 color:var(--secondary);
}

/* ========= Buttons ========= */
.stButton>button{
 width:100%;
 border-radius:12px;
 min-height:42px;
 font-weight:600;
 transition:.25s;
}

.stButton button[kind="primary"]{
 background:var(--primary);
 color:white;
 border:none;
 box-shadow:0 8px 22px rgba(99,102,241,.22);
}
.stButton button[kind="primary"]:hover{
 background:var(--primary-hover);
 transform:translateY(-2px);
}

.stButton button[kind="secondary"]{
 background:var(--card);
 color:var(--text);
 border:1px solid var(--border);
}
.stButton button[kind="secondary"]:hover{
 border-color:var(--primary);
 background:#253347;
}

/* ========= Inputs ========= */
.stTextInput input,
textarea{
 background:var(--card)!important;
 color:white!important;
 border:1px solid var(--border)!important;
 border-radius:12px!important;
}
.stTextInput input:focus,
textarea:focus{
 border-color:var(--primary)!important;
 box-shadow:0 0 10px rgba(99,102,241,.3);
}

/* ========= Chat ========= */
[data-testid="stChatInput"]{
 border-top:1px solid var(--border);
 padding-top:12px;
}
[data-testid="stChatMessage"]{
 background:var(--card);
 border:1px solid var(--border);
 border-radius:16px;
 padding:15px;
 margin-bottom:14px;
 box-shadow:0 8px 24px rgba(0,0,0,.18);
 transition:.2s;
}
[data-testid="stChatMessage"]:hover{
 border-color:var(--primary);
 transform:translateY(-1px);
}

/* ========= Expanders ========= */
details{
 background:var(--card);
 border:1px solid var(--border);
 border-radius:12px;
 padding:10px;
}

/* ========= Code ========= */
code{
 background:#111827;
 color:var(--success);
 padding:3px 6px;
 border-radius:6px;
}
pre{
 background:#111827!important;
 border:1px solid var(--border);
 border-radius:12px;
 padding:14px;
 overflow:auto;
}

/* ========= Alerts ========= */
.stSuccess,.stWarning,.stError{
 border-radius:12px;
}

/* ========= File uploader ========= */
[data-testid="stFileUploader"]{
 border:1px dashed var(--border);
 border-radius:12px;
}

/* ========= Dividers ========= */
hr{
 border-color:var(--border);
}

/* ========= Scrollbar ========= */
::-webkit-scrollbar{
 width:8px;
}
::-webkit-scrollbar-track{
 background:var(--bg);
}
::-webkit-scrollbar-thumb{
 background:#475569;
 border-radius:8px;
}
::-webkit-scrollbar-thumb:hover{
 background:#64748B;
}

/* ========= Small Animations ========= */
.stButton>button,
.stTextInput input,
textarea,
[data-testid="stChatMessage"]{
 transition:all .2s ease;
}

</style>
"""
