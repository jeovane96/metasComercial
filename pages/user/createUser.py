import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.user.usuarioCon as UsuarioCon
import pandas as pd
import random
import string
import time

def Incluir_usuario():  

    st.markdown(
        """
        <style>
        /* Alterando o fundo do campo de texto (st.text_input) */
        input[type="text"], input[type="number"] {
            background-color: #D7D9DB !important; /* Cor de fundo */
            color: #333 !important; /* Cor do texto */
        }

        /* Alterando o fundo do campo do selectbox */
        div[data-baseweb="select"] > div {
            background-color: #D7D9DB !important; /* Cor de fundo */
        }

        .stButton button:focus,
        .stButton button:active {
            background-color: black !important;
            color: white !important;
            border-color: black !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    def gerar_senha():
        tamanho_senha = 8
        caracteres = string.ascii_letters + string.digits  # Letras e números
        senha = ''.join(random.choice(caracteres) for i in range(tamanho_senha))
        return senha

    # Chama a função e gera uma senha aleatória
    senha_gerada = gerar_senha()

    col1, col2 = st.columns([2, 4])

    with col1:
        input_usuario       = st.text_input("**Usuário**", value=None)
        input_senha         = st.text_input("**Senha**", value=senha_gerada, disabled=True)
        input_perfil        = st.selectbox("**Perfil**", options=["Administrador", "Executor"])
        input_button_submit = st.button("**Enviar**")

    with col2:
        None

    if input_button_submit:
        if input_usuario is None:
            st.error("O E-mail está em branco.")
            return
        
        usuarios_existentes = UsuarioCon.obter_usuarios_cadastrados(input_usuario) 
        if usuarios_existentes:
            st.error("Usuário já cadastrado")
            return

        with st.spinner("Atualizando..."):
            sistema.email  = input_usuario
            sistema.senha  = input_senha
            sistema.perfil = input_perfil
            UsuarioCon.Incluir_usuario(sistema)
            time.sleep(3)

        st.success(f"Usuário: **{input_usuario}** e Senha: **{input_senha}** cadastrado!" )
        time.sleep(3)        
        

def ExcluirUsuario():

    def ListEmailFiltro():
        customerList = []

        for item in UsuarioCon.selecionarEmailUsuario():
            customerList.append(item.email)

        return customerList

    email = ListEmailFiltro() 

    col1, col2 = st.columns([2, 4])

    with col1:   
        input_email  = st.selectbox("**E-mail cadastrado**", email, key="list_email")
        input_button = st.button("**Enviar**", key="button_enviar")

    with col2:
        None

    if input_button:
        with st.spinner("Atualizando..."):
            sistema.email = input_email
            UsuarioCon.ExcluirUsuario(sistema)
            time.sleep(3)

        st.success(f"Usuário {input_email} excluído!" )
        time.sleep(3)        