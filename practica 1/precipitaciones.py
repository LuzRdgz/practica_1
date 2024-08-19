import csv

def leer_datos(ruta_archivo):
    datos = {}
    with open(ruta_archivo, mode='r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            region = fila['region']
            lluvia_anual = float(fila['anual'])
            datos[region] = lluvia_anual
    return datos

def calcular_estadisticas(datos):
    valores = list(datos.values())
    n = len(valores)
    
    # Calcular media
    suma = sum(valores)
    media = suma / n
    
    # Calcular máximo y mínimo
    maximo = max(valores)
    minimo = min(valores)
    
    # Calcular moda
    conteo = {}
    for valor in valores:
        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1
    
    max_frecuencia = max(conteo.values())
    modas = [valor for valor, frecuencia in conteo.items() if frecuencia == max_frecuencia]
    
    # Calcular desviación estándar
    suma_cuadrados = 0
    for valor in valores:
        diferencia = valor - media
        suma_cuadrados += diferencia ** 2
    varianza = suma_cuadrados / n
    desviacion_estandar = varianza ** 0.5
    
    return {
        'media': media,
        'maximo': maximo,
        'minimo': minimo,
        'moda': modas,
        'desviacion_estandar': desviacion_estandar
    }

def obtener_top_regiones(datos, n=5, mayor=True):
    regiones_ordenadas = sorted(datos.items(), key=lambda item: item[1], reverse=mayor)
    return [region for region, _ in regiones_ordenadas[:n]]

def main():
    ruta_archivo = 'Precipitaciones.csv'  # Nombre del archivo CSV
    datos = leer_datos(ruta_archivo)
    estadisticas = calcular_estadisticas(datos)
    
    # Obtener las 5 regiones con más y menos lluvia
    regiones_con_mas_lluvia = obtener_top_regiones(datos, n=5, mayor=True)
    regiones_con_menos_lluvia = obtener_top_regiones(datos, n=5, mayor=False)
    
    print("Estadísticas Descriptivas:")
    print("  Media:", round(estadisticas['media'], 2))
    print("  Máximo:", round(estadisticas['maximo'], 2))
    print("  Mínimo:", round(estadisticas['minimo'], 2)) 
    print("  Moda:", end=" ")
    modas = estadisticas['moda']
    if len(modas) == 1:
        print(f"{modas[0]:.2f}")
    else:
        print(", ".join(f"{m:.2f}" for m in modas))
    
    print("  Desviación Estándar:", round(estadisticas['desviacion_estandar'], 2))
    
    print("\n5 Regiones con más lluvia:")
    for region in regiones_con_mas_lluvia:
        print("  " + region)
    
    print("\n5 Regiones con menos lluvia:")
    for region in regiones_con_menos_lluvia:
        print("  " + region)

if __name__ == "__main__":
    main()
