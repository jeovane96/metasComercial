import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def selecionarEmpreendimentoFiltro():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empreendimento")
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.empreendimento_class(id=None, empreendimento=row[1]))
    
    return customerList