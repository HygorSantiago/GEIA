import pandas as pd
import sqlite3

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')


def buscar_dados(query):
    
    conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')
    cursor = conn.cursor()
    
    cursor.execute(query)
    
    df = cursor.fetchall()
    conn.close()
    
    return df

x = buscar_dados('select * from cnes_dados_profissionais_sus')

x = pd.DataFrame(x)

x.head()

