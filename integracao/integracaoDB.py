import database_sienge  as sienge
import database_sistema as sistema
import pandas as pd
import psycopg2


def consultaEmpreendimento():
    conn   = psycopg2.connect(**sienge.db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT nmempreend FROM ecadempreend;")
    consulta = cursor.fetchall()

    # Pegando os nomes reais das colunas
    colunas = [desc.name for desc in cursor.description]  # Aqui estava o problema

    # Criando o DataFrame corretamente
    df = pd.DataFrame(consulta, columns=colunas)

    cursor.close()
    conn.close()

    return df

empreendimento_sienge = consultaEmpreendimento()


def integracaoEmpreendimento():
    conn = psycopg2.connect(sistema.db_url)
    cursor = conn.cursor()

    for index, row in empreendimento_sienge.iterrows():
        cursor.execute("INSERT INTO empreendimento (empreendimento) VALUES (%s)", (row["nmempreend"],))
        print(f"Inserido: {row['nmempreend']}")


    conn.commit()

    cursor.close()
    conn.close()

integracaoEmpreendimento()