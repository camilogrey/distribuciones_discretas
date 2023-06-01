# distribuciones_discretas

BERNOULLI DRISTRIBUTION
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

BINOMIAL DRISTRIBUTION
2. User_buy_based_Previous_conversion_rate

"""
Se simula el éxito de una anuncio. Se quiere estimar la probabilidad 
de que un usuario realice una compra dada una tasa de conversión conocida:
"""
1. Se genera un f en con 2 parametros, (1) la tasa de compra de los usuarios y (2) el numero de usuarios expuestos al anuncio
2. Se conoce que la tasa_conversion es de 5%
3. Se evaluan 1000 usuarios 
4. Se hace la simulacion

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

POISSON DRISTRIBUTION
3. Performance_2_ads_Poisson 



