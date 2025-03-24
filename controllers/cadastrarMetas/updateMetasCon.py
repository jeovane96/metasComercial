import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def updateMetas(agrupamento_empreendimento, meta, fl_considera_bi, user, empreendimento, periodo):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            UPDATE comercial_metas 
            SET                   
                agrupamento_empreendimento = %s,  
                meta                       = %s,  
                fl_considera_bi            = %s,  
                user_insert                = %s,
                dt_insert                  = CURRENT_TIMESTAMP - INTERVAL '3 hours'
            WHERE
                empreendimento = %s AND periodo = %s""", (agrupamento_empreendimento, meta, fl_considera_bi, user, empreendimento, periodo)
        )
        conn.commit()

    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()