import pandas as pd
import sqlite3

#%% to
df = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_TO.csv', sep= 'column' and ';')

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table hospitalar (ID_REDE text, CD_OPERADORA text, NO_RAZAO text, DS_CLASSIFICACAO text, DE_PORTE text,\
 ID_PLANO text, CD_PLANO text, TP_VIGENCIA_PLANO text, CONTRATACAO text,\
 DE_TIPO_CONTRATACAO text, DE_TIPO_MODALIDADE_FINM text,\
 SEGMENTACAO_ASSISTENCIAL text, DE_TIPO_ABRANGENCIA_GEOGRAFICA text,\
 LG_FATOR_MODERADOR text, DE_SITUACAO_PRINCIPAL text, CD_SITUACAO_PLANO text,\
 ID_ESTABELECIMENTO_SAUDE text, CD_CNPJ_ESTB_SAUDE text, CD_CNES text,\
 NM_ESTABELECIMENTO_SAUDE text, DE_CLAS_ESTB_SAUDE text, LG_URGENCIA_EMERGENCIA text,\
 DE_TIPO_PRESTADOR text, DE_TIPO_CONTRATO text, DE_DISPONIBILIDADE text,\
 CD_MUNICIPIO text, NM_MUNICIPIO_X text, SG_UF text, DT_VINCULO_INICIO text,\
 DT_VINCULO_FIM text, NM_REGIAO text, DT_ATUALIZACAO text)'

cursor = conn.cursor()
cursor.execute(create_sql)


i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% SE
df1 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_SE.csv', sep= 'column' and ';')

i = []
for i in df1.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% rr
df3 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_RR.csv', sep= 'column' and ';')

i = []
for i in df3.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% rn
df4 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_RN.csv', sep= 'column' and ';')

i = []
for i in df4.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%pe
df5 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_PE.csv', sep= 'column' and ';')

i = []
for i in df5.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% pb
df6 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_PB.csv', sep= 'column' and ';')

i = []
for i in df6.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% pa
df7 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_PA.csv', sep= 'column' and ';')

i = []
for i in df7.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% ms
df9 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_MS.csv', sep= 'column' and ';')

i = []
for i in df9.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% pi
df10 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_PI.csv', sep= 'column' and ';')

i = []
for i in df10.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% ma
df11 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_MA.csv', sep= 'column' and ';')

i = []
for i in df11.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% df
df12 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_DF.csv', sep= 'column' and ';')

i = []
for i in df12.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% ce
df13 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_CE.csv', sep= 'column' and ';')

i = []
for i in df13.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% es
df14 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_ES.csv', sep= 'column' and ';')

i = []
for i in df14.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% am
df15 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_AM.csv', sep= 'column' and ';')

i = []
for i in df15.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% ap
df16 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_AP.csv', sep= 'column' and ';')

i = []
for i in df16.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% al
df17 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_AL.csv', sep= 'column' and ';')

i = []
for i in df17.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% ac
df18 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_AC.csv', sep= 'column' and ';')

i = []
for i in df18.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% rj
df19 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_RJ.csv', sep= 'column' and ';')

i = []
for i in df19.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% mg
df20 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_MG.csv', sep= 'column' and ';')

i = []
for i in df20.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% go

df21 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_GO.csv', sep= 'column' and ';')

i = []
for i in df21.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
    cursor.execute(insert_sql)

conn.commit()

#%% ba

df22 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_BA.csv', sep= 'column' and ';')

i = []
for i in df22.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
#    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

#%% sc

df23 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_SC.csv', sep= 'column' and ';')

i = []
for i in df23.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
#    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

#%%  rs

df24 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_RS.csv', sep= 'column' and ';')

i = []
for i in df24.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
#    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

#%%  pr

df25 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_PR.csv', sep= 'column' and ';')

i = []
for i in df25.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
#    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

#%%  ro

df26 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_RO.csv', sep= 'column' and ';')

i = []
for i in df26.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
#    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

#%% mt

df27 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_MT.csv', sep= 'column' and ';')

i = []
for i in df27.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
#    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

#%% sp

df28 = pd.read_csv('C:/Users/mathe/Downloads/produtos_e_prestadores_hospitalares/produtos_prestadores_hospitalares_SP.csv', sep= 'column' and ';')

i = []
for i in df28.itertuples(i):
#    print (i)
    insert_sql = f"insert into hospitalar (ID_REDE, CD_OPERADORA, NO_RAZAO, DS_CLASSIFICACAO, DE_PORTE, ID_PLANO, CD_PLANO, TP_VIGENCIA_PLANO, CONTRATACAO, DE_TIPO_CONTRATACAO, DE_TIPO_MODALIDADE_FINM, SEGMENTACAO_ASSISTENCIAL, DE_TIPO_ABRANGENCIA_GEOGRAFICA, LG_FATOR_MODERADOR, DE_SITUACAO_PRINCIPAL, CD_SITUACAO_PLANO, ID_ESTABELECIMENTO_SAUDE, CD_CNPJ_ESTB_SAUDE, CD_CNES, NM_ESTABELECIMENTO_SAUDE, DE_CLAS_ESTB_SAUDE, LG_URGENCIA_EMERGENCIA, DE_TIPO_PRESTADOR, DE_TIPO_CONTRATO, DE_DISPONIBILIDADE, CD_MUNICIPIO, NM_MUNICIPIO_X, SG_UF, DT_VINCULO_INICIO, DT_VINCULO_FIM, NM_REGIAO, DT_ATUALIZACAO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}')"
#    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()
