import pandas as pd

def transformar_datos(df):
    print("Transformando datos...") 
    """
    La funcion limpia el dataframe eliminando valores nulos y datos genericos errados
    """
    try: 
        # Eliminamos filas con valores vacios#
        df_limpio= df.dropna().copy()
        #eliminamos datos errados (filas con valores *****)
        df_limpio= df_limpio[~df_limpio['Descripción'].astype(str).str.contains(r'\*\*\*\*\*', na=False)]
        #Eliminar marcas con la palabra "Genérico o Generico", case=false ignora myusculas y minusculas
        df_limpio= df_limpio[~df_limpio['Marca'].astype(str).str.contains(r'gen[eé]rico', case=False, na=False)]
        #Estandarizamos marcas eliminando espacios en blanco y convirtiendo a mayusculas para evitar duplicados por diferencias de formato
        df_limpio['Marca'] = df_limpio['Marca'].astype(str).str.upper().str.strip()
        #usamos un diccionario de correcciones para estandarizar marcas comunes con errores de tipeo o variaciones, por ejemplo "GENERAL ELECTRIC" y "gENRAL ELECTRICS" se unifican a "GENERAL ELECTRIC"
        correcciones_marca = {
            'ABBOT': 'ABBOTT',
            'ABBOTT': 'ABBOTT',
            'ALLIED': 'ALLIED HEALTHCARE',
            'ALLIEDHEALTHCARE': 'ALLIED HEALTHCARE',
            'ALLIED HEALTH CARE': 'ALLIED HEALTHCARE',
            'ACCUCHECK': 'ACCU-CHECK',
            'ACCUCHEK': 'ACCU-CHECK',
            'ACCU-CHEK': 'ACCU-CHECK',
            'ACCUCHEC': 'ACCU-CHECK',
            'ABBOTT LABORATORIES': 'ABBOTT',
            'AIR SHIELDS': 'AIR-SHIELDS',
            'AMSCO SURGICAL': 'AMSCO',
            'ARJOHUNTLEIGH': 'ARJO HUNTLEIGH',
            'BECKMAN': 'BECKMAN COULTER',
            'BIO-TEK'  : 'BIOTEK',
            'BRAUN': 'B BRAUN',
            'B.BRAUN':'B BRAUN',
            'B. BRAUN':'B BRAUN',
            'BRAUND' : 'B BRAUN',
            'BRAUN': 'B BRAUN',
            'BIOCARTIS IDYLLA': 'BIOCARTIS',
            'BIOCATISIDYLLA': 'BIOCARTIS',
            'BIO-TEK': 'BIOTEK',
            'BRAINLAB': 'BRAIN LAB',
            'CASTELL':'CASTEL',
            'CENTRON TECTHONOLOGI': 'CENTRON',
            'CHEMETROM': 'CHEMETRON',
            'CHEMET': 'CHEMETRON',
            'CONMED LINVANTEC': 'CONMED LINVATEC',
            'CONMED UNVATEX': 'CONMED LINVATEC',
            'CONVIDEN': 'CONVIDIEN',
            'CRA LAB': 'CRALAB',
            'DAIGGER SCIENTIFIC':'DAIGGER',
            'DATEX-OHMEDA': 'DATEX OHMEDA',
            'DATEX OHMEDA': 'DATEX OHMEDA',
            'DWYER INSTRUMENTS': 'DWYER',
            'EDWARD LIFESCIENCE':'EDWARDS',
            'EDWARDS LIFE SCIENCE': 'EDWARDS',
            'EITAN MEDICAL': 'EITAN',
            'EPPENDFORF': 'EPPENDORF',
            'EXTECH INSTRUMENTS': 'EXTECH',
            'FISHER SICNETIFIC': 'FISHER SCIENTIFIC',
            'FLUKE MEDICA': 'FLUKE MEDICAL',
            'FRESENIUS': 'FRESENIUS KABI',
            'FULLCAUGE': 'FULL GAUGE',
            'FUKUDA': 'FUKUDA DENSHI',
            'GIVE IMAGING': 'GIVEN IMAGING',
            'GIVEN':'GIVEN IMAGING',
            'GENERAL ELECTRICS': 'GENERAL ELECTRIC',
            'GENERAL ELECTREIC': 'GENERAL ELECTRIC',
            'GREISINGER ELECTRONI': 'GREISINGER',
            'HAMILTON': 'HAMILTON MEDICAL',
            'HANNA': 'HANNA INSTRUMENTS',
            'HAWO': 'HAWK',
            'HELLMER':'HELMER',
            'HELLMERT':'HELMER',
            'HELMERT':'HELMER',
            'FISHER CIENTIFIC': 'FISHER SCIENTIFIC',
            'FISHER SCIENTIF': 'FISHER SCIENTIFIC',
            'HUNTELIGH HEALTHCARE': 'HUNTLEIGH HEALTHCARE',
            'HILL-ROM': 'HILL ROM',
            'HILLROM': 'HILL ROM',
            'HP': 'HEWLETT PACKARD',
            'JHONSON': 'JOHNSON & JOHNSON',
            'JOHSON & JOHSON': 'JOHNSON & JOHNSON',
            'JOHNSON & JOHSON': 'JOHNSON & JOHNSON',
            'KARL  STORZ': 'KARL STORZ',
            'KEX': 'KEX GERMANY',
            'KEX': 'KEX GERMANY',
            'METLER TOLEDO': 'METTLER TOLEDO',
            'METTER TOLEDO': 'METTLER TOLEDO',
            'ROCKT': 'Rocket',
            'Thermo Fisher Scient': 'THERMO SCIENTIFIC',
            'UNIT': 'UNI-T',
            'WALLC':'WALLC',
            'WALLAC PERKIN ELMER':'WALLC',
            'WALLC DELFIA':'WALLC',
            'WARM TOUCH': 'WARM TOUCH',
            'WARMTOUCH': 'WARM TOUCH',
            'WELCH ALLYN': 'WELCH ALLYN',
            'WELCHALLYN': 'WELCH ALLYN',
            'WELCH ALLYN INC': 'WELCH ALLYN',
            'WELLCH ALLYN': 'WELCH ALLYN',
            'WELCHALLYN': 'WELCH ALLYN',
            'WELCH ALLYN': 'WELCH ALLYN',
            'WESCOR ELITECH':'WESCOR',
            'WESCOR CYTOPRO': 'WESCOR',
            'WHIRLPOOL': 'WHIRLPOOL',
            'WHIRPOOL': 'WHIRLPOOL',
            'WTWLF 330': 'WTW'
            #SE PUEDEN AGREGAR MAS DE AQUI EN ADELANTE SI SE IDENTIFICAN MAS VARIACIONES DE MARCAS COMUNES
        }        
        #APLICAMOS EL DICCIONARIO PARA REEMPLAZAR LOS VALORES DE LA COLUMNA DE MARCA CON LAS CORRECCIONES DEFINIDAS EN EL DICCIONARIO
        df_limpio['Marca'] = df_limpio['Marca'].replace(correcciones_marca)
        #eliminamos A-y I- de la columna de estado
        #agregamos a la limpieza nuevos valores erroneos que se encuentran en la columna de estado, eliminamos A- e I- para dejar solo el estado limpio
        #usamos (?i)]^\s*-\s*' para eliminar cualquier valor que comience con A- o I- seguido de cualquier cantidad de espacios y un guion, sin importar mayusculas o minusculas
        df_limpio['Estado'] = df_limpio['Estado'].astype(str).str.replace(r'(?i)^[ai]\s*-\s*', '', regex=True)
        #limpiamos los posibles espacios en blanco al inicio o al final de los valores en las columnas de texto
        df_limpio['Estado'] = df_limpio['Estado'].astype(str).str.strip() 
        #eliminamos codigos duplicados, manteniendo solo la primera ocurrencia de cada codigo unico para evitar registros repetidos en el inventario final
        #reiniciamos el indice del dataframe limpio para que sea consecutivo despues de eliminar filas
        df_limpio= df_limpio.drop_duplicates(subset=['Código'], keep='first').reset_index(drop=True)
        print(f"Datos transformados con éxito. Total de filas limpias: {len(df_limpio)}")
        return df_limpio

    except KeyError as e:
        print(f"Error: La columna {e} no se encuentra en el dataframe. Verifique los nombres de las columnas.")
        return df_limpio   # Devolvemos el dataframe original en caso de error

    except Exception as e:
        print(f"Error al transformar los datos: {e}")
        return df_limpio  # Devolvemos el dataframe original en caso de error

    


