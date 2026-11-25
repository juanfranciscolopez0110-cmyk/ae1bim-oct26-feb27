from sqlalchemy import or_
from configuracion import Session
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

session = Session()

print("=== Clínicas ubicadas en Guayaquil O Quito ===")
for c in session.query(Clinica).filter(
        or_(Clinica.direccion.like("%Guayaquil%"), Clinica.direccion.like("%Quito%"))):
    print(c)

print("\n=== Consultorios de Cirugía O Dermatología ===")
for c in session.query(Consultorio).filter(
        or_(Consultorio.especialidad == "Cirugía", Consultorio.especialidad.like("%Dermatolog%"))):
    print(c)

print("\n=== Veterinarios con apellido 'Vera' O 'Castillo' ===")
for v in session.query(Veterinario).filter(
        or_(Veterinario.apellidos.like("%Vera%"), Veterinario.apellidos.like("%Castillo%"))):
    print(v)

print("\n=== Historias de la mascota 'Max' O con diagnóstico 'Parvovirus' ===")
for h in session.query(HistoriaClinica).filter(
        or_(HistoriaClinica.nombre_mascota == "Max",
            HistoriaClinica.diagnostico_principal == "Parvovirus")):
    print(h)

session.close()