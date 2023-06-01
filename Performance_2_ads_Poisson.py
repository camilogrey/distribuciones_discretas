"""
POISSON
"""

"""
La distribución de Poisson se utiliza comúnmente para modelar eventos que ocurren en un 
intervalo de tiempo fijo, pero en el ejemplo proporcionado, simplemente se simuló el número 
de clics sin referencia a un intervalo de tiempo específico.

Si deseas incorporar un intervalo de tiempo en la simulación, puedes ajustar el código para 
simular los clics en función de una tasa de clics por unidad de tiempo. Por ejemplo, si 
conoces la tasa de clics por hora, puedes convertirla a una tasa por simulación 
dividiéndola por el número de simulaciones.

Aquí tienes una versión modificada del ejemplo anterior que incorpora un intervalo de 
tiempo y utiliza la distribución de Poisson:
"""

import random
import numpy as np

def simular_clics(tasa_clics, num_simulaciones):
    """
    Simula el número de clics en un anuncio en línea utilizando una distribución de Poisson.
    
    Args:
        tasa_clics (float): La tasa de clics por unidad de tiempo.
        num_simulaciones (int): El número de simulaciones a realizar.
    
    Returns:
        int: El número promedio de clics en el anuncio.
    """
    clics_totales = np.random.poisson(tasa_clics, num_simulaciones)
    return clics_totales

# Tasa de clics por hora para la versión A y B
tasa_clics_a = 5.0
tasa_clics_b = 7.5

# Número de simulaciones
num_simulaciones = 1000

# Convertir la tasa de clics a una tasa por simulación
tasa_por_simulacion_a = tasa_clics_a / num_simulaciones
tasa_por_simulacion_b = tasa_clics_b / num_simulaciones

# Simular el rendimiento de la versión A
clics_a = simular_clics(tasa_por_simulacion_a, num_simulaciones)

# Simular el rendimiento de la versión B
clics_b = simular_clics(tasa_por_simulacion_b, num_simulaciones)

# Imprimir los resultados
print(f"Número de clics para la versión A: {sum(clics_a)}")
print(f"Número de clics para la versión B: {sum(clics_b)}")
"""
En este ejemplo, se utiliza la función np.random.poisson de NumPy para generar números 
aleatorios que siguen una distribución de Poisson. La tasa de clics por unidad de 
tiempo se divide por el número de simulaciones para obtener una tasa por simulación.

Luego, se llama a la función simular_clics con la tasa por simulación correspondiente 
y se obtiene una lista de clics simulados para cada versión.

Recuerda que el número total de clics se obtiene sumando los valores en las listas 
clics_a y clics_b.
"""
