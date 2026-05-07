from random import uniform, choice
from pathlib import Path

nombres = [
    "Alejandro","Carlos","David","Javier","Miguel","Sergio","Adrian","Pablo","Daniel","Alvaro",
    "Victor","Ivan","Raul","Hector","Mario","Samuel","Andres","Ruben","Diego","Manuel",
    "Lucia","Marta","Elena","Sara","Claudia","Paula","Andrea","Carmen","Laura","Noelia"
]

apellidos = [
    "Garcia","Martinez","Lopez","Sanchez","Perez","Gonzalez","Rodriguez","Fernandez","Ruiz","Diaz",
    "Moreno","Alonso","Navarro","Torres","Vazquez","Ramirez","Gil","Serrano","Molina","Castro"
]

asignaturas = [
    "Implementacion de sistemas", "Bases de datos", "Programacion", 
    "Redes", "Hardware", "IPPE", "Lenguaje de Marcas"
]

lineas = []
for i in range(1, 51):
    nombre = choice(nombres)
    apellido = choice(apellidos)


    notas = ",".join(
        [f"{asig}:{uniform(0.0, 10.0):.1f}" for asig in asignaturas]
    )

    linea = f"{i};{nombre};{apellido};1º ASIR;{notas}"
    lineas.append(linea)

contenido = "\n".join(lineas)

ruta = Path("data/expedientes.txt")
ruta.write_text(contenido, encoding="utf-8")

