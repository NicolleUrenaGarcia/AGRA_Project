# Proyecto final: Árboles y grafos 2026-2
Integrantes: Nicolle Ureña, Nicolas Carrillo

# Descripción del problema
Se describe una realidad imaginaria de Mumm-Ra, un conquistador que, a lo largo de los años ha intentado conquistar la tercera tierra. Para lograrlo, debe capturar al líder de la oposición, Lion-O, a quien ya tiene localizado y está a punto de atacar.
Lion-O debe escapar de la tierra y para ello, debe dirigirse de alguna manera a las estaciones espaciales disponibles antes de que los mutantes aliados de Mumm-Ra lo atrapen.
Inicialmente, en el enunciado se puede observar que hay indicios claros de un grafo ponderado no dirigido al mencionar: “Una red de carreteras que conectan sus intersecciones”, “Cada carretera tiene una longitud conocida y los vehículos pueden circular por ellas en cualquiera de las dos direcciones”, por lo tanto, una representación de un grafo podría apuntar a que los vértices son las intersecciones y sus aristas no dirigidas son las carreteras.
Por otro lado, el problema busca evaluar la menor velocidad máxima sobre la que Lion-O puede garantizar su escape priorizando la optimización, en base a la estrategia de movimiento permitida a los mutantes 
Ya que adicionalmente se menciona que se conocen las posiciones iniciales de Lion-O y Mumm-Ra, es posible modelar un grafo inicial para representar ambas posiciones.

# Resumen de la bitácora primer entrega

## Especificación del problema

Entrada: 
Un grafo no dirigido G = (V, E) tal que V es el conjunto de intersecciones donde n = |V| y E el conjunto de carreteras que conectan con las intersecciones donde m = |E| con una función de peso w : E → ℝ+ > 0 donde w(e) representa la longitud de una carretera en centenas de metros, nótese que e ∈ E  ; Un entero v ≥ 0, tal que v es la velocidad máxima en km/h de las naves de los mutantes; Un entero k ∈ ℕ₀ tal que k es la cantidad de salidas espaciales en el grafo. Se cumple que 0 ≤ k ≤ |V|; Dos vértices s y r tal que s,r ∈ V que corresponden a las ubicaciones de Lion-O y los mutantes respectivamente; un arreglo L[0…k) de nodos tal que ∀i [0,k), L[i] ∈ V ∧  |L| = k que corresponden a los nodos donde están ubicadas las estaciones espaciales. 

Salida: 
Un valor C, tal que C ∈ R+, que representa la velocidad mínima que debe alcanzar Lion-O para escapar de los mutantes, ubicados en el vértice r, partiendo de su posición inicial s, desplazándose a través de los caminos y las carreteras en el grafo G=(V,E), cuyas longitudes están definidas por un costo e, y llegando a alguna de las k salidas espaciales ubicadas en los vértices almacenados en el arreglo L[0..k), tal que |L|=k, antes de ser alcanzado por los mutantes, cuya velocidad máxima es v.

## Ejectutable - Código desarrollado

