import streamlit                         as st
import controllers.create_tbl            as create_tbl
import pages.user.acesso                 as ValidacaoUsuario
import controllers.user.usuarioCon       as controllerUser
import pages.user.createUser             as CreateUsuario
import pages.user.listUser               as ListUsuario
import pages.cadastroMetas.createMetas   as createMetas
import pages.cadastroMetas.listMetas     as listMetas
import pages.cadastroMetas.updateMetas   as updateMetas

# create_tbl.criar_tabelas_db()


# --- Define layout baseado no login ---
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    st.set_page_config(layout="wide")  # Modo WIDE quando autenticado


import streamlit as st

# Exibir a logo
st.markdown("""
    <div style="text-align: center; margin-bottom: 10px; margin-top: -80px;">
        <img src="https://catagua.com.br/wp-content/uploads/2022/01/cropped-catagua-construtora-180x50.png.webp" 
             alt="Logo Catagua" style="width: 180px; height: auto;">
    </div>
""", unsafe_allow_html=True)

# CSS otimizado
st.markdown("""
    <style>
    /* Esconder a barra branca do Streamlit */
    header { visibility: hidden; }

    /* Animação de brilho do título */
    @keyframes glow {
        0% { text-shadow: 0 0 5px #fff, 0 0 10px #CCCCCC, 0 0 15px #D2FED8; }
        50% { text-shadow: 0 0 10px #fff, 0 0 20px #CCCCCC, 0 0 30px #D2FED8; }
        100% { text-shadow: 0 0 5px #fff, 0 0 10px #CCCCCC, 0 0 15px #D2FED8; }
    }

    /* Estilizar o título */
    .glowing-text {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: white;
        animation: glow 5s infinite alternate;
        margin: -30px 0 -50px 0 !important;
        line-height: 1;
    }

    /* Cor de fundo da aplicação */
    .stApp { background-color: #F1F5F9; }

    /* Estilizar os botões */
    .stButton button {
        border: 2px solid #286398;
        background-color: #286398;
        color: white;
        padding: 5px 12px;
        border-radius: 12px;
        cursor: pointer;
        font-size: 16px;
        transition: all 0.3s ease;
        width: 120px !important;
        height: 35px !important;
    }

    .stButton button:hover {
        background-color: black;
        border-color: #D9D9D9;
    }

    /* Remover efeito vermelho ao clicar */
    .stButton button:focus, .stButton button:active {
        outline: none !important;
        box-shadow: none !important;
        background-color: #286398 !important;
        border-color: #286398 !important;
    }

    /* Ajuste do layout das abas */
    div[data-testid="stTab"] { background-color: transparent; }

    button[data-baseweb="tab"] {
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px 10px 0 0;
        background-color: #D9D9D9;
        color: black;
        padding: 10px 20px;
        transition: 0.3s;
    }

    /* Aba ativa */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: black;
        color: white;
        border-bottom: 2px solid white;
    }

    /* Hover nas abas */
    button[data-baseweb="tab"]:hover { background-color: #B0B0B0; }

    /* Rodapé fixo */
    .fixed-footer {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 5px 10px;
        border-radius: 5px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        font-size: 14px;
        z-index: 1000;
    }

    /* Nome do usuário no canto direito */
    .header-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 10px 10px;
    }

    .user-info {
        font-size: 14px;
        font-weight: normal;
        color: #CBCBCB;
    }
    </style>

    <h1 class='glowing-text'> Metas de Venda </h1>
""", unsafe_allow_html=True)

# Exibir o nome do usuário no canto direito
st.markdown(f"""
    <div class="header-container">
        <div class="user-info">🔑 {st.session_state.get("user", "Desconhecido")}</div>
    </div>
""", unsafe_allow_html=True)


# Pequeno espaço para ajuste
st.write("")


def usuario_adm():

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([0.03, 0.2])
    with col1:
        cadastrar_meta_button = st.button("📊 Metas", use_container_width=True)
            
    with col2:
        incluir_usuario_button = st.button("👤 Usuário", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "listar"
    elif incluir_usuario_button:
        st.session_state["active_page"] = "cadastrarUsuario"
    elif cadastrar_meta_button:
        st.session_state["active_page"] = "cadastrarMeta"

    if st.session_state["active_page"] == "cadastrarUsuario":
        inserir, deletar, consultar = st.tabs(["Inserir", "Deletar", "Consultar"])
        with inserir:
            CreateUsuario.Incluir_usuario()
        with deletar:
            CreateUsuario.ExcluirUsuario()
        with consultar:
            ListUsuario.ListUsuarios()

    if st.session_state["active_page"] == "cadastrarMeta":
        inserir, atualizar, consultar = st.tabs(["Inserir", "Atualizar", "Consultar"])
        with inserir:
            createMetas.createMeta()
        with atualizar:
            updateMetas.updateMeta()
        with consultar:
            listMetas.ListMetas()

if ValidacaoUsuario.authenticate_user():
    if "just_logged_in" not in st.session_state:
        st.session_state["just_logged_in"] = True
        st.rerun()  # Força a página a atualizar para corrigir o nome do usuário
    
    perfil = controllerUser.obter_perfil_usuario(st.session_state["user"])

    if perfil == "Administrador":
        usuario_adm()


# CreateUsuario.Incluir_usuario()
# ListUsuario.ListUsuarios() #Gwy1IbYo