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
    
    # Leer el archivo CSV
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", low_memory=False)
    
    # NO renombrar ni establecer índice personalizado - mantener índice por defecto
    
    # 1. Limpieza de 'sexo'
    df['sexo'] = df['sexo'].str.lower().str.strip()
    df['sexo'] = df['sexo'].astype('category')
    
    # 2. Limpieza de 'tipo_de_emprendimiento'
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].astype('category')
    
    # 3. Limpieza de 'idea_negocio'
    df['idea_negocio'] = df['idea_negocio'].str.lower().str.strip()
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ')
    df['idea_negocio'] = df['idea_negocio'].str.replace('-', ' ')
    df['idea_negocio'] = df['idea_negocio'].astype('category')
    
    # 4. Limpieza de 'barrio'
    df['barrio'] = df['barrio'].str.lower().str.strip()
    df['barrio'] = df['barrio'].str.replace('_', ' ')
    df['barrio'] = df['barrio'].str.replace('-', ' ')
    df['barrio'] = df['barrio'].astype('category')
    
    # 5. Limpieza de 'estrato'
    df['estrato'] = df['estrato'].astype(int)
    
    # 6. Limpieza de 'comuna_ciudadano'
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    
    # 7. Limpieza de 'fecha_de_beneficio'
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='mixed', dayfirst=True)
    # MANTENER como datetime, NO convertir a string
    
    # 8. Limpieza de 'monto_del_credito'
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '', regex=False)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(' ', '')
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)

    # 9. Limpieza de 'línea_credito' - MÁS CONSERVADORA
    df['línea_credito'] = df['línea_credito'].str.lower().str.strip()
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ')
    # NO eliminar espacios ni puntos completamente
    # Solo corregir errores ortográficos específicos
    df['línea_credito'] = df['línea_credito'].str.replace('solidiaria', 'solidaria')
    df['línea_credito'] = df['línea_credito'].astype('category')
    
    # 10. Eliminar registros duplicados ANTES de eliminar NaN
    df.drop_duplicates(inplace=True)
    
    # 11. Eliminar registros con valores faltantes
    df.dropna(inplace=True)
    
    # Guardar el archivo limpio
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

if __name__ == "__main__":
    pregunta_01()