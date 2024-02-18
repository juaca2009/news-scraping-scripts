import pandas as pd

def add_rows_csv(nuevas_filas, nombre_archivo = 'noticias.csv'):
    try:
        df = pd.read_csv(nombre_archivo, sep='\t')
    except FileNotFoundError:
        if nuevas_filas:
            columnas = list(vars(nuevas_filas[0]).keys())
            df = pd.DataFrame(columns=columnas)
        else:
            df = pd.DataFrame()
    nuevas_filas_df = pd.DataFrame([vars(obj) for obj in nuevas_filas])
    df = pd.concat([df, nuevas_filas_df], ignore_index=True)
    df.to_csv(nombre_archivo, index=False, sep='\t')
