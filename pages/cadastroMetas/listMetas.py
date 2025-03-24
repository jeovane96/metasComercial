import streamlit as st
import controllers.cadastrarMetas.listMetasCon as listMetasCon
import pandas as pd

def ListMetas():
    customerList = []

    for item in listMetasCon.selecionarMetas():
        customerList.append(
            [
                item.empreendimento,
                item.periodo,
                item.agrupamento_empreendimento,
                item.meta,
                item.fl_considera_bi,
                item.dt_insert,
                item.user 
            ]
        )

    df = pd.DataFrame(
        customerList,
        columns=['Empreendimento', 'Período', 'Agrupamento Empreendimento', 'Meta', 'Considera no BI', 'Data', 'Usuário']
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        empreendimento        = df['Empreendimento'].unique()
        empreendimento_filtro = st.selectbox('**Empreendimento**', options=['Todas'] + sorted(list(empreendimento)))

    with col2:
        meses = {
            "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6,
            "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
        }
        def converter_periodo(periodo):
            try:
                mes, ano = periodo.split("/")
                return pd.to_datetime(f"01/{meses[mes.lower()]}/{ano}", format="%d/%m/%Y")
            except:
                return None
            
        df["Período_Ordenado"]  = df["Período"].apply(converter_periodo)
        df                      = df.sort_values(by="Período_Ordenado")
        periodo                 = df["Período"].unique()
        periodo_filtro          = st.selectbox("**Período**", options=["Todas"] + list(periodo))

    if empreendimento_filtro != 'Todas':
        df = df[df['Empreendimento'] == empreendimento_filtro]

    if periodo_filtro != 'Todas':
        df = df[df['Período'] == periodo_filtro]

    table_html = df.to_html(index=False, classes="table", border=1)

    st.markdown("""
        <style>
            .table-container {
                max-height: 600px;  /* Ajuste a altura conforme necessário */
                overflow-y: auto;  /* Habilita a rolagem vertical */
                margin-top: 20px;
            }
            .table {
                width: 100%;
                text-align: center;
                border-collapse: collapse;
            }
            .table th {
                background-color: black;
                color: white;
                padding: 10px;
                text-align: center;  /* CENTRALIZA OS CABEÇALHOS */
                position: sticky;
                top: 0;
                z-index: 1;  /* Garante que o cabeçalho ficará acima do conteúdo */
                font-size: 14px; /* Ajuste conforme necessário */
            }
            .table td {
                border: 1px solid grow;
                padding: 8px;
                text-align: center; /* CENTRALIZA O CONTEÚDO */
                font-size: 12px; /* Ajuste conforme necessário */

            }
            .table tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .table tr:nth-child(odd) {
                background-color: #ffffff;
            }
            .table tr:hover {
                background-color: #ddd;
            }
        </style>
    """, unsafe_allow_html=True)

    # Envolver a tabela com a div para permitir a rolagem
    st.markdown(f"<div class='table-container'>{table_html}</div>", unsafe_allow_html=True)