"""
Deseas simular el éxito de una campaña de marketing en la cual estás buscando que los 
usuarios realicen una compra después de ver un anuncio. Quieres estimar la probabilidad 
de que un usuario realice una compra dada una tasa de conversión conocida:
"""
import random

def simular_compras(tasa_conversion, num_usuarios):
    """
    Simula el número de compras realizadas por usuarios en una campaña de marketing utilizando una distribución binomial.
    
    Args:
        tasa_conversion (float): La tasa de conversión, es decir, la probabilidad de que un usuario realice una compra.
        num_usuarios (int): El número total de usuarios que se expusieron al anuncio.
    
    Returns:
        int: El número de compras realizadas por los usuarios.
    """
    compras_totales = 0
    for _ in range(num_usuarios):
        if random.random() < tasa_conversion:
            compras_totales += 1
    return compras_totales

# Tasa de conversión de la campaña de marketing (por ejemplo, 0.05 para 5%)
tasa_conversion = 0.05

# Número total de usuarios expuestos al anuncio
num_usuarios = 1000

# Simular el número de compras realizadas
num_compras = simular_compras(tasa_conversion, num_usuarios)

# Imprimir los resultados
print(f"Número de compras realizadas: {num_compras}")

"""
En este ejemplo, se define la función simular_compras que simula el número de 
compras realizadas por usuarios en una campaña de marketing utilizando una distribución 
binomial. La función toma la tasa de conversión (es decir, la probabilidad de que un 
usuario realice una compra) y el número total de usuarios expuestos al anuncio.

Utilizando random.random(), se simula cada usuario y se verifica si realiza una compra 
en función de la tasa de conversión. El contador de compras totales se incrementa cada 
vez que un usuario realiza una compra.

Luego, se especifica la tasa de conversión y el número de usuarios expuestos al anuncio. 
La función simular_compras se llama para obtener el número de compras realizadas.

Por último, se imprime el resultado que muestra el número de compras realizadas en 
la campaña.
"""