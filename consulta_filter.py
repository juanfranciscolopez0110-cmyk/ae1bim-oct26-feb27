from configuracion import Session
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

session = Session()

print("=== Clínica con nombre 'PetCare Guayaquil' ===")
for c in session.query(Clinica).filter(Clinica.nombre_comercial == "PetCare Guayaquil"):
    print(c)

print("\n=== Consultorios de especialidad 'Cirugía' ===")
for c in session.query(Consultorio).filter(Consultorio.especialidad == "Cirugía"):
    print(c)

print("\n=== Veterinarios cuyo apellido contiene 'Mendoza' ===")
for v in session.query(Veterinario).filter(Veterinario.apellidos.like("%Mendoza%")):
    print(v)

print("\n=== Historias con diagnóstico 'Otitis' ===")
for h in session.query(HistoriaClinica).filter(HistoriaClinica.diagnostico_principal == "Otitis"):
    print(h)

session.close()