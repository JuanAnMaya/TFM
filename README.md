# Triple Influence Ranking Model (TIRM): una medida de influencia de usuarios en Twitter

# Author
 - Juan Antonio Maya Marín

# Abstract 
 > Debido a la creciente importancia del estudio de la influencia de los usuarios dentro de
   las redes sociales, en este trabajo se presenta una nueva medida llama TIRM, encargada de 
   cuantificar la influencia potencial de todos los perfiles en una red de usuarios de Twitter. 
   Además de eso también se prueba su efectividad con usuarios, y luego con los usuarios que 
   pueden ser considerados bots, y se observan los resultados obtenidos en este caso.

# Guía del código

-> 1. Preparación del dataset: Partiendo de los conjuntos de datos iniciales, se realizan todos
      los cambios pertinentes para que los datos sean aptos para el objetivo del trabajo.

-> 2. Ejecución del método TIRM. Creación de los diferentes grafos. Usando todos los datos de 
      la sección anterior, creamos todos los grafos con los que vamos a trabajar. Creamos sus 
      nodos, aristas y pesos de estas.

-> 3. Una vez disponemos de todos los grafos, ejecutamos el método IRM sobre ellos, calculando
      de esta forma la puntuación final de cada usuario al unir la información que resulta al
      aplicar el método sobre los 3 grafos. Esta puntuación representa su posible influencia.

-> 4. Estudio de los resultados obtenidos. Partiendo de el ranking de usuarios obtenido con 
      el método TIRM, dividimos el total de usuarios en 4 grupos dependiendo de la naturaleza
      de estos usuarios. Comparamos los atributos de los usuarios de cada grupo, para demostrar
      que efectivamente el grupo con los usuarios más influyentes está lejos del resto.
