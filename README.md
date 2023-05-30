# distribuciones_discretas

Bernoulli
1. Prob_Clicks_on_link_Bernoulli

En el ejercicio de la funcion de probabilidad de Bernoulli, la distribucion de la probabilidad solo pueden tomar dos valores posibles, etiquetados como éxito (1) P o fracaso (0) P -1.

1. Simula un click en un link de una publicación en twitter 
2. Esta f de simulacion da como resulado aleatorio un 0 o 1
3. Se estima un P de exito de (0.25) 25%
4. Si P < 0 hizo click la f devuelve True de lo contrario Falsee
6. Si la P es mayor devuelve False.
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

Binomial
2. User_buy_based_Previous_conversion_rate




