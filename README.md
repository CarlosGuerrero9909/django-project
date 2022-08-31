# proyectoBackPython
[recording-2022-08-31-17-42-33.webm](https://user-images.githubusercontent.com/90810310/187797765-64a6bb18-f887-4ce3-9bd0-66a3d76c334d.webm)

Lista de endpoint funcionales
- http://localhost:8000/ --> Api Root: ruta por defecto
- http://localhost:8000/carreras/ --> Carrera List: endpoint donde se encuentran todas la carreras registradas con su codigo, nombre y materias asociadas a la misma
- http://localhost:8000/carreras/020 --> Carrera Instance de ingenieria de sistemas
- http://localhost:8000/carreras/135 --> Carrera Instance de licenciatura en fisica
- http://localhost:8000/materias/ --> Materia List: endpoint donde se encuentran el global de todas las materias registradas con su rescpectiva información
- http://localhost:8000/materias/"cod-materia"/ --> Materia Instance: informacion de una materia en especifico
- http://localhost:8000/syllabus/ --> Syllabus File: Retorna el syllabus de una respectiva materia, enviandole el codigo de la carrera y la materia a traves del metodo post
