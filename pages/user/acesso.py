import streamlit as st
import time
import psycopg2
import controllers.database as db

def verificar_usuario(email, senha):
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tb_usuario WHERE email = %s AND senha = %s", (email, senha))
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado > 0  

def authenticate_user():

    st.markdown(
        """
        <style>
        /* Alterando o fundo do campo de texto (usuário e senha) */
        input[type="text"], input[type="password"] {
            background-color: #D7D9DB !important;   /* Cor de fundo */
            color: #333 !important;                 /* Cor do texto */
            border-radius: 5px !important;          /* Bordas arredondadas */
            border: 1px solid #ccc !important;      /* Borda sutil */
            padding: 8px !important;                /* Ajuste de padding */
        }

        /* Ajustando o fundo do container do input (inclui o "olhinho") */
        div[data-testid="stPassword"] {
            background-color: #D7D9DB !important; /* Mesma cor do campo */
            border-radius: 5px !important;
            padding: 5px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.get("authenticated", False):  
        return True

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    login_placeholder = st.empty()  
    success_placeholder = st.empty()  

    with login_placeholder.container():
        st.markdown(""" 
            <style>
            .title-container { display: flex; justify-content: center; text-align: center; height: 10vh; }
            .title-container h1 { font-size: 2em; }
            </style>
        """, unsafe_allow_html=True)
        st.markdown('<div class="title-container"><h1>''</h1></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 4, 3])
        with col1:
            None

        with col2:
            email        = st.text_input("**E-mail**", key="login_email")
            password     = st.text_input("**Senha**", type="password", key="login_password")
            login_button = st.button("Entrar")

            if login_button:
                with st.spinner("Autenticando..."):
                    autenticado = verificar_usuario(email, password)
                    time.sleep(3)

                if autenticado:
                    st.session_state["authenticated"] = True
                    st.session_state["user"]          = email

                    success_placeholder.success(f"Bem-vindo, **{email.upper()}** !")
                    time.sleep(3)
                    success_placeholder.empty()  
                    login_placeholder.empty()  

                    return True  
                else:
                    st.error("E-mail ou senha inválidos.")

            return False
        
        with col3:
            None