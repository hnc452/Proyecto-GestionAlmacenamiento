import pandas as pd

def carga_datos(df, nombre_archivo_salida):
    print("Cargando datos...")
    """
    Guarda el dataframe transformado en un nuevo archivo de Excel con el nombre especificado.
    """
    try:
        #guardamos en excel index=false para no incluir el indice del dataframe en el archivo de salida
        df.to_excel(nombre_archivo_salida, index=False, engine='openpyxl')
        print(f"Datos cargados con éxito en {nombre_archivo_salida}")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        
