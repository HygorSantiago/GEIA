import pandas as pd
import sqlite3

#%%CNES ESTALECIMENTO -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbEstabelecimento202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_estabelecimento (CO_UNIDADE text, CO_CNES text, NU_CNPJ_MANTENEDORA text, TP_PFPJ text, NIVEL_DEP text, NO_RAZAO_SOCIAL text, NO_FANTASIA text, NO_LOGRADOURO text, NU_ENDERECO text, NO_COMPLEMENTO text, NO_BAIRRO text, CO_CEP text, CO_REGIAO_SAUDE text, CO_MICRO_REGIAO text, CO_DISTRITO_SANITARIO text, CO_DISTRITO_ADMINISTRATIVO text, NU_TELEFONE text, NU_FAX text, NO_EMAIL text, NU_CPF text, NU_CNPJ text, CO_ATIVIDADE text, CO_CLIENTELA text, NU_ALVARA text, DT_EXPEDICAO text, TP_ORGAO_EXPEDIDOR text, DT_VAL_LIC_SANI text, TP_LIC_SANI text, TP_UNIDADE text, CO_TURNO_ATENDIMENTO text, CO_ESTADO_GESTOR text, CO_MUNICIPIO_GESTOR text, DT_ATUALIZACAO text, CO_USUARIO text, CO_CPFDIRETORCLN text, REG_DIRETORCLN text, ST_ADESAO_FILANTROP text, CO_MOTIVO_DESAB text, NO_URL text, NU_LATITUDE text, NU_LONGITUDE text, DT_ATU_GEO text, NO_USUARIO_GEO text, CO_NATUREZA_JUR text, TP_ESTAB_SEMPRE_ABERTO text, ST_GERACREDITO_GERENTE_SGIF text, ST_CONEXAO_INTERNET text, CO_TIPO_UNIDADE text, NO_FANTASIA_ABREV text, TP_GESTAO text, DT_ATUALIZACAO_ORIGEM text, CO_TIPO_ESTABELECIMENTO text, CO_ATIVIDADE_PRINCIPAL text, ST_CONTRATO_FORMALIZADO text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_estabelecimento (CO_UNIDADE, CO_CNES, NU_CNPJ_MANTENEDORA, TP_PFPJ, NIVEL_DEP, NO_RAZAO_SOCIAL, NO_FANTASIA, NO_LOGRADOURO, NU_ENDERECO, NO_COMPLEMENTO, NO_BAIRRO, CO_CEP, CO_REGIAO_SAUDE, CO_MICRO_REGIAO, CO_DISTRITO_SANITARIO, CO_DISTRITO_ADMINISTRATIVO, NU_TELEFONE, NU_FAX, NO_EMAIL, NU_CPF, NU_CNPJ, CO_ATIVIDADE, CO_CLIENTELA, NU_ALVARA, DT_EXPEDICAO, TP_ORGAO_EXPEDIDOR, DT_VAL_LIC_SANI, TP_LIC_SANI, TP_UNIDADE, CO_TURNO_ATENDIMENTO, CO_ESTADO_GESTOR, CO_MUNICIPIO_GESTOR, DT_ATUALIZACAO, CO_USUARIO, CO_CPFDIRETORCLN, REG_DIRETORCLN, ST_ADESAO_FILANTROP, CO_MOTIVO_DESAB, NO_URL, NU_LATITUDE, NU_LONGITUDE, DT_ATU_GEO, NO_USUARIO_GEO, CO_NATUREZA_JUR, TP_ESTAB_SEMPRE_ABERTO, ST_GERACREDITO_GERENTE_SGIF, ST_CONEXAO_INTERNET, CO_TIPO_UNIDADE, NO_FANTASIA_ABREV, TP_GESTAO, DT_ATUALIZACAO_ORIGEM, CO_TIPO_ESTABELECIMENTO, CO_ATIVIDADE_PRINCIPAL, ST_CONTRATO_FORMALIZADO) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}', '{i[32]}', '{i[33]}', '{i[34]}', '{i[35]}', '{i[36]}', '{i[37]}', '{i[38]}', '{i[39]}', '{i[40]}', '{i[41]}', '{i[42]}', '{i[43]}', '{i[44]}', '{i[45]}', '{i[46]}', '{i[47]}', '{i[48]}', '{i[49]}', '{i[50]}', '{i[51]}', '{i[52]}', '{i[53]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%CNES HEMOTERAPIA - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbHemoterapia202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_hemoterapia (CO_UNIDADE text, NU_SRECEPCAD text, NU_STRIAGHMT text, NU_STRIAGCLN text, NU_SCOLETA text, NU_SAFERESE text, NU_SPRESTOQ text, NU_SPROCES text, NU_SESTOQUE text, NU_SDISTRIB text, NU_SOROLOGIA text, NU_SIMUNOHEM text, NU_SPRETRANF text, NU_SHEMOSTAS text, NU_SCONTROLQ text, NU_SBIOMOLEC text, NU_SIMUNFEN text, NU_STRANSFUS text, NU_SSGDOADOR text, QT_ECADRECLI text, QT_ECENTREFR text, QT_ERFGUASNG text, QT_ECONGRAPD text, QT_EEXTAPLSM text, QT_EFREEZ18 text, QT_EFREEZ30 text, QT_EAGITPLQT text, QT_ESELADORA text, QT_EIRRADHEM text, QT_EAGLTNOSC text, QT_EMAQAFRES text, QT_ERFGAREAG text, QT_ERFGAMSTS text, QT_ECAPFLLAM text, NO_RHEMOT text, NO_RHEMAT text, NO_RETECSO text, NO_MRCAPAC text, CO_CPFMRHEMOT text, CO_CPFMRHEMAT text, CO_CPFMRTECSO text, CO_CPFMCAPAC text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_hemoterapia (CO_UNIDADE, NU_SRECEPCAD, NU_STRIAGHMT, NU_STRIAGCLN, NU_SCOLETA, NU_SAFERESE, NU_SPRESTOQ, NU_SPROCES, NU_SESTOQUE, NU_SDISTRIB, NU_SOROLOGIA, NU_SIMUNOHEM, NU_SPRETRANF, NU_SHEMOSTAS, NU_SCONTROLQ, NU_SBIOMOLEC, NU_SIMUNFEN, NU_STRANSFUS, NU_SSGDOADOR, QT_ECADRECLI, QT_ECENTREFR, QT_ERFGUASNG, QT_ECONGRAPD, QT_EEXTAPLSM, QT_EFREEZ18, QT_EFREEZ30, QT_EAGITPLQT, QT_ESELADORA, QT_EIRRADHEM, QT_EAGLTNOSC, QT_EMAQAFRES, QT_ERFGAREAG, QT_ERFGAMSTS, QT_ECAPFLLAM, NO_RHEMOT, NO_RHEMAT, NO_RETECSO, NO_MRCAPAC, CO_CPFMRHEMOT, CO_CPFMRHEMAT, CO_CPFMRTECSO, CO_CPFMCAPAC, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}', '{i[32]}', '{i[33]}', '{i[34]}', '{i[35]}', '{i[36]}', '{i[37]}', '{i[38]}', '{i[39]}', '{i[40]}', '{i[41]}', '{i[42]}', '{i[43]}', '{i[44]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%CNES MANTEDORA - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbMantenedora202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_mantedora (NU_CNPJ_MANTENEDORA TEXT, CO_BANCO TEXT, NU_AGENCIA TEXT, NU_CONTA_CORRENTE TEXT, NO_RAZAO_SOCIAL TEXT, NO_LOGRADOURO TEXT, NU_ENDERECO TEXT, NO_COMPLEMENTO TEXT, NO_BAIRRO TEXT, CO_CEP TEXT, CO_MUNICIPIO TEXT, CO_REGIAO_SAUDE TEXT, NU_TELEFONE TEXT, DT_PREENCHIMENTO TEXT, ST_FMS_FES TEXT, NU_CNPJ_FMS_FES TEXT, CO_NATUREZA_JUR TEXT, DT_ATUALIZACAO TEXT, CO_USUARIO TEXT, CO_GESTOR TEXT, CO_MUNICIPIO_MANT TEXT, DT_ATUALIZACAO_ORIGEM TEXT)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_mantedora (NU_CNPJ_MANTENEDORA, CO_BANCO, NU_AGENCIA, NU_CONTA_CORRENTE, NO_RAZAO_SOCIAL, NO_LOGRADOURO, NU_ENDERECO, NO_COMPLEMENTO, NO_BAIRRO, CO_CEP, CO_MUNICIPIO, CO_REGIAO_SAUDE, NU_TELEFONE, DT_PREENCHIMENTO, ST_FMS_FES, NU_CNPJ_FMS_FES, CO_NATUREZA_JUR, DT_ATUALIZACAO, CO_USUARIO, CO_GESTOR, CO_MUNICIPIO_MANT, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%CNES QUIMIO_RADIO -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbQuimioRadio202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_quimio_radio (CO_UNIDADE text, NU_SALARSIMU text, NU_SALARPLAN text, CO_CPFMEDRADM text, CO_CPFMRONCPD text, CO_CPFMRCIRON text, CO_CPFMR_RAD text, CO_CPFMR_FIS text, NU_SLARARMFO text, NU_SLARCONFM text, NU_SLARMOLDE text, NU_SLARBOLCP text, NU_SLAQARMAZ text, NU_SLAQPREPA text, NU_SLAQCDURA text, NU_SLAQLDURA text, NU_SLACPFLUL text, QT_EQRSIMULA text, QT_EQRACELL6 text, QT_EQR_6SEME text, QT_EQR_6COME text, QT_RORTV1050 text, QT_RORV50150 text, QT_ROV150500 text, QT_RUNIDCOBA text, QT_EQRBRBAIX text, QT_EQRBRMEDI text, QT_EQRBRALTA text, QT_EQRMONITA text, QT_EQRMONITI text, QT_EQRSISPLN text, QT_EQRDOSCLI text, QT_EQRFONSEL text, NO_MEDRADM text, NO_MRONCPD text, NO_MRCIRON text, NO_MR_RAD text, NO_MRFIS text, CO_CPFMRONC text, NO_MRONC text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_quimio_radio (CO_UNIDADE, NU_SALARSIMU, NU_SALARPLAN, CO_CPFMEDRADM, CO_CPFMRONCPD, CO_CPFMRCIRON, CO_CPFMR_RAD, CO_CPFMR_FIS, NU_SLARARMFO, NU_SLARCONFM, NU_SLARMOLDE, NU_SLARBOLCP, NU_SLAQARMAZ, NU_SLAQPREPA, NU_SLAQCDURA, NU_SLAQLDURA, NU_SLACPFLUL, QT_EQRSIMULA, QT_EQRACELL6, QT_EQR_6SEME, QT_EQR_6COME, QT_RORTV1050, QT_RORV50150, QT_ROV150500, QT_RUNIDCOBA, QT_EQRBRBAIX, QT_EQRBRMEDI, QT_EQRBRALTA, QT_EQRMONITA, QT_EQRMONITI, QT_EQRSISPLN, QT_EQRDOSCLI, QT_EQRFONSEL, NO_MEDRADM, NO_MRONCPD, NO_MRCIRON, NO_MR_RAD, NO_MRFIS, CO_CPFMRONC, NO_MRONC, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}', '{i[30]}', '{i[31]}', '{i[32]}', '{i[33]}', '{i[34]}', '{i[35]}', '{i[36]}', '{i[37]}', '{i[38]}', '{i[39]}', '{i[40]}', '{i[41]}', '{i[42]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%CNES ServicoReferenciado -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbServicoReferenciado202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_Servico_Referenciado (CO_UNIDADE text, CO_SERVICO_REFERENCIADO text, TP_SERVICO_REFERENCIADO text, CO_CNPJ text, NO_RAZAO_SOCIAL text, CO_MUNICIPIO text, CO_USUARIO text, DT_ATUALIZACAO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_Servico_Referenciado (CO_UNIDADE, CO_SERVICO_REFERENCIADO, TP_SERVICO_REFERENCIADO, CO_CNPJ, NO_RAZAO_SOCIAL, CO_MUNICIPIO, CO_USUARIO, DT_ATUALIZACAO, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}')"
    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

#%% equipe - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbEquipe202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_equipe (CO_MUNICIPIO TEXT, CO_AREA TEXT, SEQ_EQUIPE TEXT, CO_UNIDADE TEXT, TP_EQUIPE TEXT, CO_SUB_TIPO_EQUIPE TEXT, NO_REFERENCIA TEXT, DT_ATIVACAO TEXT, DT_DESATIVACAO TEXT, TP_POP_ASSIST_QUILOMB TEXT, TP_POP_ASSIST_ASSENT TEXT, TP_POP_ASSIST_GERAL TEXT, TP_POP_ASSIST_ESCOLA TEXT, TP_POP_ASSIST_PRONASCI TEXT, TP_POP_ASSIST_INDIGENA TEXT, TP_POP_ASSIST_RIBEIRINHA TEXT, TP_POP_ASSIST_SITUACAO_RUA TEXT, TP_POP_ASSIST_PRIV_LIBERDADE TEXT, TP_POP_ASSIST_CONFLITO_LEI TEXT, TP_POP_ASSIST_ADOL_CONF_LEI TEXT, CO_CNES_UOM TEXT, NU_CH_AMB_UOM TEXT, CD_MOTIVO_DESATIV TEXT, CD_TP_DESATIV TEXT, CO_PROF_SUS_PRECEPTOR TEXT, CO_CNES_PRECEPTOR TEXT, CO_EQUIPE TEXT, DT_ATUALIZACAO TEXT, NO_USUARIO TEXT, DT_ATUALIZACAO_ORIGEM TEXT)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_equipe (CO_MUNICIPIO, CO_AREA, SEQ_EQUIPE, CO_UNIDADE, TP_EQUIPE, CO_SUB_TIPO_EQUIPE, NO_REFERENCIA, DT_ATIVACAO, DT_DESATIVACAO, TP_POP_ASSIST_QUILOMB, TP_POP_ASSIST_ASSENT, TP_POP_ASSIST_GERAL, TP_POP_ASSIST_ESCOLA, TP_POP_ASSIST_PRONASCI, TP_POP_ASSIST_INDIGENA, TP_POP_ASSIST_RIBEIRINHA, TP_POP_ASSIST_SITUACAO_RUA, TP_POP_ASSIST_PRIV_LIBERDADE, TP_POP_ASSIST_CONFLITO_LEI, TP_POP_ASSIST_ADOL_CONF_LEI, CO_CNES_UOM, NU_CH_AMB_UOM, CD_MOTIVO_DESATIV, CD_TP_DESATIV, CO_PROF_SUS_PRECEPTOR, CO_CNES_PRECEPTOR, CO_EQUIPE, DT_ATUALIZACAO, NO_USUARIO, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}', '{i[23]}', '{i[24]}', '{i[25]}', '{i[26]}', '{i[27]}', '{i[28]}', '{i[29]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes dadosprofissionaissus - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbDadosProfissionalSus202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_dados_profissionais_sus (CO_PROFISSIONAL_SUS text, CO_CPF text, NO_PROFISSIONAL text, CO_CNS text, DT_ATUALIZACAO text, CO_USUARIO text, ST_NMPROF_CADSUS text, CO_NACIONALIDADE text, CO_SEQ_INCLUSAO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_dados_profissionais_sus (CO_PROFISSIONAL_SUS, CO_CPF, NO_PROFISSIONAL, CO_CNS, DT_ATUALIZACAO, CO_USUARIO, ST_NMPROF_CADSUS, CO_NACIONALIDADE, CO_SEQ_INCLUSAO, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes dialise - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbDialise202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_dialise (CO_UNIDADE text, QT_SALA_HBSAG_POS text, QT_SALA_HBSAG_NEG text, QT_SALA_DPI text, QT_SALA_DPAC text, QT_SALA_REAG_POS text, QT_SALA_REAG_NEG text, QT_SALA_REHCV text, NU_MAQH_PROP text, NU_MAQH_OUTR text, CO_NEFRO_RESPONSAVEL text, CO_CPF_NEFRO text, CO_CPF_DIRETOR text, NO_DIRETOR_RESPONSAVEL text, TP_FILTRO_AREIA text, TP_FILTRO_CARVAO text, TP_ABRANDADOR text, TP_DEOINIZADOR text, TP_OSMOSE_REVERSA text, TP_OUTROS_TRAT_AGUA text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_dialise (CO_UNIDADE, QT_SALA_HBSAG_POS, QT_SALA_HBSAG_NEG, QT_SALA_DPI, QT_SALA_DPAC, QT_SALA_REAG_POS, QT_SALA_REAG_NEG, QT_SALA_REHCV, NU_MAQH_PROP, NU_MAQH_OUTR, CO_NEFRO_RESPONSAVEL, CO_CPF_NEFRO, CO_CPF_DIRETOR, NO_DIRETOR_RESPONSAVEL, TP_FILTRO_AREIA, TP_FILTRO_CARVAO, TP_ABRANDADOR, TP_DEOINIZADOR, TP_OSMOSE_REVERSA, TP_OUTROS_TRAT_AGUA, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', '{i[21]}', '{i[22]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes cargahorariasus -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/tbCargaHorariaSus202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_carga_horaria_sus (CO_UNIDADE text, CO_PROFISSIONAL_SUS text, CO_CBO text, TP_SUS_NAO_SUS text, IND_VINCULACAO text, TP_TERCEIRO_SIH text, QT_CARGA_HORARIA_AMBULATORIAL text, CO_CONSELHO_CLASSE text, NU_REGISTRO text, SG_UF_CRM text, TP_PRECEPTOR text, TP_RESIDENTE text, NU_CNPJ_DETALHAMENTO_VINCULO text, A_DT_ATUALIZACAO text, CO_USUARIO text, A_DT_ATUALIZACAO_ORIGEM text, QT_CARGA_HORARIA_OUTROS text, QT_CARGA_HOR_HOSP_SUS text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_carga_horaria_sus (CO_UNIDADE, CO_PROFISSIONAL_SUS, CO_CBO, TP_SUS_NAO_SUS, IND_VINCULACAO, TP_TERCEIRO_SIH, QT_CARGA_HORARIA_AMBULATORIAL, CO_CONSELHO_CLASSE, NU_REGISTRO, SG_UF_CRM, TP_PRECEPTOR, TP_RESIDENTE, NU_CNPJ_DETALHAMENTO_VINCULO, A_DT_ATUALIZACAO, CO_USUARIO, A_DT_ATUALIZACAO_ORIGEM, QT_CARGA_HORARIA_OUTROS, QT_CARGA_HOR_HOSP_SUS) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}', '{i[13]}', '{i[14]}', '{i[15]}', '{i[16]}', '{i[17]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabServicoApoio - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabServicoApoio202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_EstabServicoApoio (CO_UNIDADE text, CO_SERVICO_APOIO text, CO_CARACTERISTICA text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_EstabServicoApoio (CO_UNIDADE, CO_SERVICO_APOIO, CO_CARACTERISTICA, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabServClass - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabServClass202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_EstabServClass (CO_UNIDADE text, CO_SERVICO text, CO_CLASSIFICACAO text, TP_CARACTERISTICA text, CO_CNPJCPF text, CO_AMBULATORIAL text, CO_AMBULATORIAL_SUS text, CO_HOSPITALAR text, CO_HOSPITALAR_SUS text, CO_END_COMPL text, ST_ATIVO_SN text, DT_ATUALIZACAO text, CO_USUARIO text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_EstabServClass (CO_UNIDADE, CO_SERVICO, CO_CLASSIFICACAO, TP_CARACTERISTICA, CO_CNPJCPF, CO_AMBULATORIAL, CO_AMBULATORIAL_SUS, CO_HOSPITALAR, CO_HOSPITALAR_SUS, CO_END_COMPL, ST_ATIVO_SN, DT_ATUALIZACAO, CO_USUARIO ) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}', '{i[10]}', '{i[11]}', '{i[12]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabEquipamento -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabEquipamento202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_EstabEquipamento (CO_UNIDADE text, CO_EQUIPAMENTO text, CO_TIPO_EQUIPAMENTO text, QT_EXISTENTE text, QT_USO text, TP_SUS text, DT_ATUALIZACAO text, CO_USUARIO text, T_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_EstabEquipamento (CO_UNIDADE, CO_EQUIPAMENTO, CO_TIPO_EQUIPAMENTO, QT_EXISTENTE, QT_USO, TP_SUS, DT_ATUALIZACAO, CO_USUARIO, T_ATUALIZACAO_ORIGEM) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabInstFisiAssist - ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabInstFisiAssist202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_EstabInstFisiAssist (CO_UNIDADE text, CO_INSTALACAO text, QT_INSTALACAO text, NU_LEITOS text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_EstabInstFisiAssist (CO_UNIDADE, CO_INSTALACAO, QT_INSTALACAO, NU_LEITOS, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM ) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabColetaSelRejeito -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabColetaSelRejeito202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_EstabColetaSelRejeito (CO_UNIDADE text, CO_COLETA_REJEITO text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_EstabColetaSelRejeito (CO_UNIDADE, CO_COLETA_REJEITO, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM ) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabComissaoOutro -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabComissaoOutro202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_EstabComissaoOutro (CO_UNIDADE text, CO_COMISSAO text, DT_ATIVACAO text, DT_DESATIVACAO text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_EstabComissaoOutro (CO_UNIDADE, CO_COMISSAO, DT_ATIVACAO, DT_DESATIVACAO, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM ) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabComplementar -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabComplementar202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_EstabComplementar (CO_UNIDADE text, CO_LEITO text, CO_TIPO_LEITO text, TP_ALTACOMP text, QT_EXIST text, QT_CONTR text, QT_SUS text, DT_ATUALIZACAO text, CO_USUARIO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_EstabComplementar (CO_UNIDADE, CO_LEITO, CO_TIPO_LEITO, TP_ALTACOMP, QT_EXIST, QT_CONTR, QT_SUS, DT_ATUALIZACAO, CO_USUARIO, DT_ATUALIZACAO_ORIGEM ) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}', '{i[8]}', '{i[9]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes Cooperativa -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlCooperativa202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table cnes_Cooperativa (CO_UNIDADE text, CO_COOPERATIVA text, CO_CBO text, CO_USUARIO text, DT_ATUALIZACAO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into cnes_Cooperativa (CO_UNIDADE, CO_COOPERATIVA, CO_CBO, CO_USUARIO, DT_ATUALIZACAO, DT_ATUALIZACAO_ORIGEM ) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}')"
    cursor.execute(insert_sql)

conn.commit()

#%%cnes EstabAtendPrestConv -ok

df = pd.read_csv('C:/Users/mathe/Downloads/wetransfer_base_de_dados_cnes_202301_2023-03-05_1919/BASE_DE_DADOS_CNES_202301/rlEstabAtendPrestConv202301.csv', sep= 'column' and ';', encoding = 'ISO-8859-1')

colunas = str(df.columns.values).replace('\n','')[1:-1]
colunas = str(df.columns.values).replace("'",'')[1:-1]
valores = df.values[0]

conn = sqlite3.connect('C:/Users/mathe/Downloads/my_way.db')

create_sql = 'create table EstabAtendPrestConv (CO_UNIDADE text, CO_ATENDIMENTO_PRESTADO text, CO_CONVENIO text, CO_USUARIO text, DT_ATUALIZACAO text, DT_ATUALIZACAO_ORIGEM text)'

cursor = conn.cursor()
cursor.execute(create_sql)

i = []
for i in df.itertuples(i):
#    print (i)
    insert_sql = f"insert into EstabAtendPrestConv (CO_UNIDADE, CO_ATENDIMENTO_PRESTADO, CO_CONVENIO, CO_USUARIO, DT_ATUALIZACAO, DT_ATUALIZACAO_ORIGEM ) values ('{i[0]}','{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}')"
    cursor.execute(insert_sql)

conn.commit()

