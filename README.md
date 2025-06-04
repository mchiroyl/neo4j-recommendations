# Descripción del proyecto

Este proyecto muestra el uso de bases de datos de grafos con Neo4j y Flask,  
mostrando recomendaciones de películas basadas en relaciones entre usuarios y películas.

# Instrucciones para instalar dependencias y ejecutar la app
1. Clonar el repositorio en la terminal de windows  
   git clone https://github.com/mchiroyl/neo4j-recommendations  
2. abrir vs code  
3. abrir la carpeta contenedora del proyecto desde vs code   
4. Crear y activar un entorno virtual en la raiz del proyecto  
   python -m venv venv  
   venv\Scripts\activate  
5. Instalar Flask y Neo4j  
   pip install flask neo4j  
6. Ejecutar la aplicación Flask  
   python app.py  
7. Abrir el navegador y acceder a la dirección siguiente  
   http://localhost:5000

# Capturas o explicación del funcionamiento básico.
El programa permite consultar recomendaciones por usuario como por pelicula.  
El usuario puede ingresar un ID, puede ser el 1 al 20 para obtener películas sugeridas basadas en los hábitos de otros usuarios similares.  
Alternativamente puede ingresar el nombre de una película y visualizaer títulos relacionados que han sido valorados por los mismos usuarios.  
   
![Captura de pantalla 2025-06-04 165609](https://github.com/user-attachments/assets/c51c6a33-8c88-49b0-8330-35acd17ee5d0)
![Captura de pantalla 2025-06-04 170608](https://github.com/user-attachments/assets/a09c849e-2467-4689-9ad7-e872ef362fb2)
![Captura de pantalla 2025-06-04 170623](https://github.com/user-attachments/assets/95bbee69-85a7-404e-a816-1772b80acf1d)
![Captura de pantalla 2025-06-04 170634](https://github.com/user-attachments/assets/19bff234-8e9c-48e1-b5c5-c23944d67c4a)


# Conexión a la base de datos demo
URI = "neo4j+s://demo.neo4jlabs.com:7687"  
USERNAME = "recommendations"  
PASSWORD = "***************"  
driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))  


