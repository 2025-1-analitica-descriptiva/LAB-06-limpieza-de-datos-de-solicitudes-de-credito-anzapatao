"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import numpy as np

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    # TODO
    # renombrar el indice 
    # ¿se necesita un set index?
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", low_memory=False)
    # Renombrar la primera columna como 'index' y establecerla como índice del DataFrame
    df.rename(columns={df.columns[0]: 'index'}, inplace=True)
    df.set_index('index', inplace=True)
    df['sexo'] = df['sexo'].str.lower().str.strip()
    # convertir sexo a tipo category
    df['sexo'] = df['sexo'].astype('category')
    # print(df.sexo.value_counts().to_list())
    # tipo de datos en tipo category
    # tipo de emprendimiento estandarización en 4 categrías y pasarlo a minu2sculas, pasarloa  tipo category
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].astype('category')

    # en idea de negocio, estandarización, eliminar espacios, reemplazar guiones bajos por espacios, pasar a minúsculas, pasarlo a tipo category
    df['idea_negocio'] = df['idea_negocio'].str.lower().str.strip()
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ')
    df['idea_negocio'] = df['idea_negocio'].str.replace('-', ' ')
    df['idea_negocio'] = df['idea_negocio'].astype('category')
    # print(df['idea_negocio'].describe())
    # en barrio 
    df['barrio'] = df['barrio'].str.lower().str.strip()
    df['barrio'] = df['barrio'].str.replace('_', ' ')
    df['barrio'] = df['barrio'].str.replace('-', ' ')
    df['barrio'] = df['barrio'].astype('category')
    df['estrato'] = df['estrato'].astype(int)
    # df = df[df['estrato'] >= 1]
    # imprimir cantidad de registros por barrio
    # print(df['estrato'].value_counts())
    # en comuna ciudadano, tipo de dato enteros y category
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    # df = df[df['comuna_ciudadano'] >= 1]
    # df['comuna_ciudadano'] = df['comuna_ciudadano'].astype('category')
    # print cantidad de registros por comuna
    # print(len(df['comuna_ciudadano'].value_counts().to_list()))
    # fecha de beneficio datefrist
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='mixed', dayfirst=True)
    # Group dates and print count
    # Examine raw date patterns
    date_counts = df['fecha_de_beneficio'].value_counts()

    # Then proceed with datetime conversion
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='mixed', dayfirst=True)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d/%m/%Y')
    # monto del crédito hacer replace, eliminar simbolo de pesos, comas por espacios, tipo de datoa  float
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '', regex=False)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(' ', '')
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)
    # df = df[df['monto_del_credito'] >= 1000]

    # print(df['monto_del_credito'].value_counts())
    # línea de crédito estandarizar minusculas, eliminar espacios, reemaplazar guiones bajos por espacios, pasarlo a tipo category
    df['línea_credito'] = df['línea_credito'].str.lower().str.strip()
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace(' ', '')
    df['línea_credito'] = df['línea_credito'].str.replace('.', '')
    df['línea_credito'] = df['línea_credito'].replace('solidiaria', 'solidaria')
    df['línea_credito'] = df['línea_credito'].astype('category')
    
    # print(df['línea_credito'].value_counts().sort_index())
    # dropna y drop_duplicates
    # Eliminar NaN, NA y None
    df.dropna(inplace=True)
    
    # Si también quieres eliminar filas con ceros en ciertas columnas numéricas
    df.drop_duplicates(inplace=True)
    print("\nDate distribution (top 10 most common patterns):")
    print(date_counts.head(10))
    print(df['comuna_ciudadano'].value_counts())
    
    
    # Print description of each column

    # print("\nDescriptive statistics for each column:")
    # for column in df.columns:
    #     print(f"\n{column}:")
    #     if df[column].dtype.name in ['category', 'object']:
    #         print(df[column].value_counts())
    #     else:
    #         print(df[column].describe())
    # 10.206

    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";")

if __name__ == "__main__":
    pregunta_01()
