import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.cadastrarMetas.cadastrarMetasCon as cadastrarMetasCon
import controllers.cadastrarMetas.listEmpreendimentoCon as listEmpreendimentoCon
import time
import streamlit as st
from datetime import datetime

ano_atual = datetime.now().year
meses = [
    "Janeiro", 
    "Fevereiro", 
    "Março", 
    "Abril", 
    "Maio", 
    "Junho",
    "Julho", 
    "Agosto", 
    "Setembro", 
    "Outubro", 
    "Novembro", 
    "Dezembro"
]
lista_meses_ano = [f"{mes}/{ano_atual}" for mes in meses]

def createMeta():

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
    
    def ListEmpreendimentoFiltro():
        customerList = []

        for item in listEmpreendimentoCon.selecionarEmpreendimento():
            customerList.append(item.empreendimento)

        return customerList

    empreendimento_ = ListEmpreendimentoFiltro() 

    # Verifica se o usuário está autenticado
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    # Garante que o usuário autenticado está disponível no session_state
    user = st.session_state.get("user", "")
        
    col1, col2 = st.columns([2, 4])

    with col1:
        input_empreendimento    = st.selectbox("**Empreendimento**", options=empreendimento_, key="selectbox_empreendimento_create")
        input_periodo           = st.selectbox("**Período**", options=lista_meses_ano, key="selectbox_periodo_create") #produto
        input_agrupamento       = st.text_input("**Agruamento do Empreendimento**", key="text_input_agrupamento")
        input_meta              = st.text_input("**Meta**", value="") # , placeholder="Digite um número"
        input_fl_considera_bi   = st.checkbox("**Considera no BI**", key="fl_considera_bi_create")
        input_user              = st.text_input("**Usuário**", value=user, disabled=True, key="usuario_autenticado_create")
        input_button_submit     = st.button("**Enviar**", key="button_create")

    with col2:
        None
        
    if input_button_submit:

        if cadastrarMetasCon.validacaoInsertEmpreendimento(input_empreendimento, input_periodo):
            return st.error(f"Meta do empreendimento **{input_empreendimento}** no período de **{input_periodo}** já lançado!")
        
        if input_meta == "":
            return st.error("O campo da meta está sem valor")

        with st.spinner("Atualizando..."):   
            sistema.empreendimento              = input_empreendimento 
            sistema.periodo                     = input_periodo
            sistema.agrupamento_empreendimento  = input_agrupamento
            sistema.meta                        = int(input_meta) 
            sistema.fl_considera_bi             = input_fl_considera_bi
            sistema.user                        = input_user
            cadastrarMetasCon.insertMetas(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Meta do empreendimento **{input_empreendimento}** lançada!")  
        time.sleep(2)
        success_container.empty()