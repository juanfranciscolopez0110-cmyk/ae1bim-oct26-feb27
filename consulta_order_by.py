from configuracion import Session
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

session = Session()

print("=== Clínicas ordenadas por nombre (A-Z) ===")
for c in session.query(Clinica).order_by(Clinica.nombre_comercial):
    print(c)

print("\n=== Consultorios ordenados por especialidad ===")
for c in session.query(Consultorio).order_by(Consultorio.especialidad):
    print(c)

print("\n=== Veterinarios ordenados por apellido ===")
for v in session.query(Veterinario).order_by(Veterinario.apellidos):
    print(v)

print("\n=== Historias ordenadas por fecha (más recientes primero) ===")
for h in session.query(HistoriaClinica).order_by(HistoriaClinica.fecha_atencion.desc()):
    print(h)

session.close()