Hola Juanpa. Cómo va todo?
Te dejo este README con el fin de explicar cómo pensé y construí el proyecto Simulación de Red Social — Conecta-DS. La idea es que veas el proceso lógico (clase por clase) justificando cada decisión técnica con propiedad. También incluyo enlaces a documentación que me fue muy útil para cada bloque.

Contexto rápido: el objetivo del parcial es implementar gestión de perfiles (Tabla Hash), almacenamiento de amistades (listas de adyacencia), componentes conectados (Union-Find WQU), un motor de sugerencias (Max-PQ) y filtros/ordenamiento, todo según el enunciado y la rúbrica del parcial. Podés revisar el enunciado y la rúbrica adjunta.
[Simulación de Red Social - Parcial #4.pdf](https://github.com/user-attachments/files/23225721/Simulacion.de.Red.Social.-.Parcial.4.pdf)
[Rubrica Parcial #4.pdf](https://github.com/user-attachments/files/23225720/Rubrica.Parcial.4.pdf)


Estructura del Proyecto:
SimulacionRedSocial/
├─ main.py
├─ model/
│  ├─ perfil.py
│  ├─ tabla_hash.py
│  ├─ union_find.py
│  ├─ max_pq.py
├─ services/
│  ├─ gestor_perfiles.py
│  ├─ motor_sugerencias.py
│  ├─ ordenamiento.py
├─ data/
│  └─ perfiles_ejemplo.csv

Explicación, Justificación y Documentación:

- model/perfil.py

Representa un perfil de usuario con sus datos y una lista de amigos.
Usé un diccionario (dict) para almacenar los amigos con su peso porque tiene búsquedas O(1) promedio y mantiene el código limpio.

Documentación:
Diccionarios en Python: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
Type hints (-> y tipos opcionales): https://docs.python.org/3/library/typing.html
PEP 484 (Anotaciones de tipo): https://peps.python.org/pep-0484/


- model/tabla_hash.py

Implementa una Tabla Hash con encadenamiento.
Permite crear, buscar, eliminar y cargar perfiles desde CSV de forma eficiente.
El método cargar_desde_csv() usa el módulo estándar csv para la lectura masiva.

Documentación:
Módulo csv en Python: https://docs.python.org/3/library/csv.html
Explicación sobre Tablas Hash: https://en.wikipedia.org/wiki/Hash_table
Rehash y colisiones (artículo educativo): https://realpython.com/python-hash-table/


- model/union_find.py

Implementa Weighted Quick Union con compresión de caminos, para manejar los componentes conectados entre usuarios (es decir, saber si dos usuarios están en la misma red).

Documentación:
Disjoint Set (Union-Find): https://en.wikipedia.org/wiki/Disjoint-set_data_structure
Quick Union explicado (Princeton): https://algs4.cs.princeton.edu/15uf/
Compresión de caminos y complejidad α(N): https://cp-algorithms.com/data_structures/disjoint_set_union.html


- model/max_pq.py

Implementa una cola de prioridad máxima (Max-Heap) para determinar los usuarios más relevantes en las sugerencias.
Elegí una implementación propia (en lugar de usar heapq) para mostrar dominio de la estructura.

Documentación:
Módulo heapq (cola de prioridad en Python): https://docs.python.org/3/library/heapq.html
Heaps y Priority Queues: https://en.wikipedia.org/wiki/Priority_queue
Tutorial práctico sobre heaps: https://realpython.com/python-heapq-module/


- services/gestor_perfiles.py

Conecta la Tabla Hash con el Union-Find.
Aquí se crean perfiles, se generan lazos y se asegura que ambas estructuras estén sincronizadas.
Sigue el principio de responsabilidad única (SRP) y las buenas prácticas SOLID.

Documentación:
Principios SOLID en POO: https://en.wikipedia.org/wiki/SOLID
SRP (Single Responsibility Principle): https://stackify.com/solid-design-principles/
Buenas prácticas de arquitectura en Python: https://docs.python-guide.org/writing/structure/


- services/motor_sugerencias.py

Lógica central de sugerencia de amigos (Friends of Friends).
Usa la cola de prioridad máxima para calcular relevancia (Q = calidad(X, A)), y aplica filtros de género y edad.
Luego, ordena los resultados con Merge Sort.

Documentación:
Algoritmo Merge Sort: https://en.wikipedia.org/wiki/Merge_sort
Complejidad Big-O de algoritmos de ordenamiento: https://www.bigocheatsheet.com/
Filtros con comprensión de listas en Python: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions


- services/ordenamiento.py

Implementa Merge Sort de forma estable para ordenar las sugerencias dentro de una misma prioridad por nombreCompleto.

Documentación:
Merge Sort paso a paso: https://www.geeksforgeeks.org/merge-sort/
Estabilidad de algoritmos de ordenamiento: https://stackoverflow.com/questions/1517793/stable-vs-unstable-sorting-algorithms


- main.py

Punto de entrada del proyecto.
Carga los perfiles desde CSV, genera lazos de amistad (aleatorios o manuales) y ejecuta el motor de sugerencias.
El objetivo fue dejar un script que ejecute todo el flujo automáticamente, sin dependencias extra.

Documentación:
Lectura de archivos CSV: https://docs.python.org/3/library/csv.html
Generación aleatoria (random): https://docs.python.org/3/library/random.html
Entrada principal (if __name__ == "__main__"): https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts


Gracias por ser tan buen profe mi Juanpa, lo quiero mucho!
