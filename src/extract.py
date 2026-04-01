def extraer_datos(lista_archivos, columnas_deseadas):
    print("Extrayendo datos...")
    
    #la función de extracción lee los archivos de Excel y los almacena en variables para su posterior uso en el pipeline ETL.   
    dataframes = []
    for archivo in lista_archivos:
        try:
            df = pd.read_excel(archivo, usecols=columnas_deseadas)
            dataframes.append(df)
        except Exception as e:
            print(f"Error al extraer el archivo {archivo}: {e}")

    #unimos todos los dataframes en uno solo para facilitar su transformación y carga posterior.
    df_total = pd.concat(dataframes, ignore_index=True)
    print("Datos extraídos con éxito.")
    return df_total


    
