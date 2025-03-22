import streamlit as st
import controllers.user.usuarioCon as ControllerSistema
import pandas as pd

def ListUsuarios():
    customerList = []

    for item in ControllerSistema.selecionarTodosUsuarios():
        customerList.append([
            item.id, 
            item.email, 
            item.senha, 
            item.perfil
        ])

    df = pd.DataFrame(
        customerList,
        columns=['ID', 'E-mail', 'Senha', 'Perfil']
    )

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
                background-color: #64A9DA;
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
