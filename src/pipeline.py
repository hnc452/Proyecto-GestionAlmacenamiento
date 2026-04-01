#importar los modulos de extracción, transformación y carga
from extract import extraer_datos
from transform import transformar_datos
from load import carga_datos
import os
import time

base_path =r"D:\Users\ruizc\Desktop\PROYECTO GESTION DE ALMACENAMIENTO\data\raw"

#usamos el disparador del pipeline para ejecutar las funciones de extracción, transformación y carga
def main():
    print("Ejecutando pipeline ETL...")
    #iniciamos el cronometro para medir el tiempo de ejecución del pipeline
    
    start_time = time.time()
    archivos_origen = [os.path.join(base_path, "BASE INSTALADA METROLOGIA 2026.xlsx"),
                       os.path.join(base_path, "datos 1.xlsx"), 
                       os.path.join(base_path, "datos 2.xlsx")
                       ]  # Lista de archivos de  origen
    columnas_necesarias= ['Código', 'Descripción', 'Marca', 'Modelo', 'Estado'] 
    archivo_destino=r'D:\Users\ruizc\Desktop\PROYECTO GESTION DE ALMACENAMIENTO\data\processed\datos_transformados.xlsx'  # Archivo de salida
    # Extraer datos
    print("\nFase 1: Extracción de datos...")
    df_crudo = extraer_datos(archivos_origen, columnas_necesarias)
    # 2. Transformar datos
    print("\nFase 2: Transformación de datos...")
    df_procesado = transformar_datos(df_crudo)
    # 3. Cargar datos
    print("\nFase 3: Carga de datos...")
    carga_datos(df_procesado, archivo_destino)
    #calculamos el tiempo total de ejecución del pipeline restando el tiempo de inicio al tiempo actual
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTiempo total de ejecución del pipeline: {total_time:.2f} segundos")
    filas_procesadas = len(df_procesado)
    print(f"Total de filas procesadas: {filas_procesadas}")
    print(f"TIempo total de ejecucion: {total_time:.2f} segundos")
    print(f"Velocidad de procesamiento: {filas_procesadas/total_time:.2f} filas por segundo")
    print(f"Registros crudos leidos: {len(df_crudo)} filas")
    print(f"Registros eliminados: {len(df_crudo) - len(df_procesado)} filas")
    print(f"Registros validos limpios: {filas_procesadas} filas")
            
    print("Pipeline ETL ejecutado con éxito.")

#llamamos a cada una de las funciones para ejecutar el pipeline ETL
if __name__ == "__main__":    
    main()
    
