import streamlit                         as st
import controllers.create_tbl            as create_tbl
import pages.user.acesso                 as ValidacaoUsuario
import controllers.user.usuarioCon       as controllerUser
import pages.user.createUser             as CreateUsuario
import pages.user.listUser               as ListUsuario
import pages.cadastroMetas.createMetas   as createMetas
import pages.cadastroMetas.listMetas     as listMetas

create_tbl.criar_tabelas_db()


# --- Define layout baseado no login ---
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    st.set_page_config(layout="wide")  # Modo WIDE quando autenticado

st.markdown(
    """
    <style>
    /* Esconder a barra branca do Streamlit */
    header {visibility: hidden;}

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
        margin-top: 100px !important; /* Sobe o título mais */
        margin-bottom: -90px !important;
        padding: 0 !important;
        line-height: 1;
    }

    /* Ajuste do layout principal (Remove espaços e sobe o sistema) */
    .block-container {
        padding-top: 0px !important;
        margin-top: -50px !important; /* Sobe mais */
    }

    /* Ajuste do corpo da página */
    body {
        padding-top: 0px !important;
        margin-top: -100px !important; /* Sobe ainda mais */
    }

    /* Cor de fundo da aplicação */
    .stApp {
        background-color: #F1F5F9;
    }

    /* Estilizar os botões */
    .stButton button {
        border: 2px solid #C6C8C6;
        background-color: black;
        color: white;
        padding: 5px 12px;
        border-radius: 12px;
        cursor: pointer;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: #D9D9D9;
        color: black;
        border-color: #D9D9D9;
    }

    .stButton button:focus {
        outline: none;
    }

    /* Estilizar o rodapé fixo */
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

    /* Estilizar a sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F8F9FA;
    }

    .stSidebar .stMarkdown span {
        font-size: 18px !important;
        font-weight: bold;
        color: #000000;
        text-align: center;
    }

    .stSidebar button {
        width: 90% !important;
        height: 40px !important;
        border: 2px solid #D9D9D9;
        background-color: #D9D9D9;
        color: black;
        border-radius: 8px;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
    }

    .stSidebar button:hover {
        background-color: black;
        color: white;
    }

    .stSidebar button:focus,
    .stSidebar button:active {
        background-color: black !important;
        color: white !important;
        border-color: black !important;
    }
    </style>

    <h1 class='glowing-text'> Metas de Venda </h1>
    """,
    unsafe_allow_html=True
)

# Aplicar estilo personalizado
st.markdown(
    """
    <style>
        /* Esconde o fundo padrão das abas */
        div[data-testid="stTab"] {
            background-color: transparent;
        }

        /* Estiliza as abas */
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
        button[data-baseweb="tab"]:hover {
            background-color: #B0B0B0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>
        .header-container {{
            display: flex;
            justify-content: flex-end; /* Move o nome do usuário para o canto direito */
            align-items: center;
            padding: 10px 10px;
        }}

        .user-info {{
            font-size: 14px;
            font-weight: normal;
            color: #CBCBCB;
        }}
    </style>

    <div class="header-container">
        <div class="user-info">🔑 {st.session_state.get("user", "Desconhecido")}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Pequeno espaço para ajuste
st.write("")


def usuario_adm():

    # Criar colunas para botões
    col1, col2 = st.columns(2)
    with col1:
        st.sidebar.markdown("<span style='font-size:50px; font-weight:bold;'>⚙️ Menu</span>", unsafe_allow_html=True)
        cadastrar_meta_button  = st.sidebar.button("Metas", key="cadastrar_meta")
        incluir_usuario_button = st.sidebar.button("Usuário", key="cadastrar_usuario_button")


    # Armazenar estado atual no session_state
    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "listar"  # Página inicial padrão

    # Navegar entre páginas com base nos botões
    elif incluir_usuario_button:
        st.session_state["active_page"] = "cadastrarUsuario"
    elif cadastrar_meta_button:
        st.session_state["active_page"] = "cadastrarMeta"

    # AÇÃO DE CADA BOTÃO
    if st.session_state["active_page"] == "cadastrarUsuario":
        inserir, deletar, consultar = st.tabs(["Inserir", "Deletar", "Consultar"])

        with inserir:
            CreateUsuario.Incluir_usuario()
        with deletar:
            CreateUsuario.ExcluirUsuario()
        with consultar:
            ListUsuario.ListUsuarios()

    if st.session_state["active_page"] == "cadastrarMeta":
        inserir, atualizar, deletar, consultar = st.tabs(["Inserir", "Atualizar", "Deletar", "Consultar"])

        with inserir:
            createMetas.createMeta()
        with atualizar:
            None
        with deletar:
            None
        with consultar:
            listMetas.ListMetas()


# Verifica se o usuário está autenticado
if ValidacaoUsuario.authenticate_user():
    if "just_logged_in" not in st.session_state:
        st.session_state["just_logged_in"] = True
        st.rerun()  # Força a página a atualizar para corrigir o nome do usuário
    
    perfil = controllerUser.obter_perfil_usuario(st.session_state["user"])

    if perfil == "Administrador":
        usuario_adm()


# CreateUsuario.Incluir_usuario()
# ListUsuario.ListUsuarios() #Gwy1IbYo