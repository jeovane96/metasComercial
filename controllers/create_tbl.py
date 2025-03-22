import streamlit as st
import psycopg2
import controllers.database as db

def criar_tabelas_db():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_usuario (
                id        SERIAL PRIMARY KEY,
                email     TEXT NOT NULL,
                senha     TEXT NOT NULL,
                perfil    TEXT NOT NULL,
                dt_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours'
            )''')
        print("Tabela 'tb_usuario' criada com sucesso.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comercial_metas (
                id                          SERIAL PRIMARY KEY,
                periodo                     TEXT NOT NULL,
                empreendimento              TEXT NOT NULL,
                agrupamento_empreendimento  TEXT NOT NULL,
                meta                        INT NOT NULL,
                fl_considera_bi             BOOLEAN DEFAULT FALSE,
                dt_insert                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours',
                user_insert                 TEXT NOT NULL
            )''')
        print("Tabela 'comercial_metas' criada com sucesso.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS empreendimento (
                id              SERIAL PRIMARY KEY,
                empreendimento  TEXT NOT NULL
            )''')
        print("Tabela 'empreendimento' criada com sucesso.")

    except psycopg2.Error as e:
        print(f"Erro ao criar tabelas: {e}")

    conn.commit()
    conn.close()