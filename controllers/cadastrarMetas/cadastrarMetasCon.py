import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertMetas(insert_metas):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO comercial_metas (
                periodo,                   
                empreendimento,            
                agrupamento_empreendimento,
                meta,
                fl_considera_bi,
                user_insert                      
            ) 
            VALUES(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )""",
            (
                insert_metas.periodo, 
                insert_metas.empreendimento,
                insert_metas.agrupamento_empreendimento,
                insert_metas.meta,
                insert_metas.fl_considera_bi,
                insert_metas.user
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()