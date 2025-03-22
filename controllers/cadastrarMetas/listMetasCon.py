import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def selecionarMetas():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            id,                        
            periodo,                   
            empreendimento,            
            agrupamento_empreendimento,
            meta,   
            CASE 
                WHEN fl_considera_bi = TRUE THEN 'Sim' 
                ELSE 'Não' 
            END AS fl_considera_bi,                            
            TO_CHAR(dt_insert, 'DD/MM/YYYY HH24:MI') AS dt_insert,                 
            user_insert                
        FROM 
            comercial_metas
        ORDER BY
            ID
        ASC
    """)
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.metas(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    return customerList