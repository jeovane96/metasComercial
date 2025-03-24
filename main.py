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
        border: 2px solid black;
        background-color: #AFE6FF;
        color: black;
        padding: 5px 12px;
        border-radius: 12px;
        cursor: pointer;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: black;
        color: white;
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

    st.markdown(
        """
        <style>
            .button-container {
                display: flex;
                justify-content: center; /* Centraliza os botões */
                gap: 1px; /* Define o espaço entre os botões */
            }

            .stButton button {
                width: 120px !important;  /* Define um tamanho fixo para os botões */
                height: 35px !important;  /* Define uma altura menor */
                font-size: 14px !important;
                padding: 5px !important;
                border-radius: 5px !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([0.03, 0.2])
    with col1:
        cadastrar_meta_button = st.button("📊 Metas", use_container_width=True)
            
    with col2:
        incluir_usuario_button = st.button("👤 Usuário", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Armazenar estado atual no session_state
    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "listar"

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
        inserir, atualizar, consultar = st.tabs(["Inserir", "Atualizar", "Consultar"])

        with inserir:
            createMetas.createMeta()
        with atualizar:
            updateMetas.updateMeta()
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