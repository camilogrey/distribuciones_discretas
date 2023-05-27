"""
BERNOULLI
"""
import random

def simular_click(probabilidad):
    """
    Simula un click en un link de una publicación en twitter 
    utilizando una distribución de Bernoulli.
    
    Args:
        probabilidad (float): La probabilidad de que un usuario haga click en el enlace.
    
    Returns:
        bool:   True el usuario SI hizo click 
                False el usuario NO hizo click
    """
    return random.random() < probabilidad 
"""
Esta f devuelve un número aleatorio entre 0 y 1. Si el número aleatorio 
es menor que la probabilidad dada (0.25):
1. Se considera que el usuario hizo click y la función devuelve True
2. Si la P es mayor devuelve False.
"""
# Probabilidad de que un usuario haga click en el link (por ejemplo, 0.25 para 25%)
probabilidad_click = 0.25

# Número de simulaciones
num_simulaciones = 5000

# Realizar las simulaciones
clicks = [simular_click(probabilidad_click) for i in range(num_simulaciones)]

# Contar el número de clicks
num_clicks = sum(clicks)

# Calcular la proporción de clicks
proporcion_clicks = num_clicks / num_simulaciones

# Imprimir los resultados
print(f"Número de simulaciones: {num_simulaciones}")
print(f"Número de clicks: {num_clicks}")
print(f"Proporción de clicks: {proporcion_clicks}")
