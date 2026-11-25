from datetime import date
from sqlalchemy import and_
from configuracion import Session
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

session = Session()

print("=== Clínicas en Quito Y con responsable 'Dra. Lucía Paredes' ===")
for c in session.query(Clinica).filter(
        and_(Clinica.direccion.like("%Quito%"),
             Clinica.veterinario_responsable == "Dra. Lucía Paredes")):
    print(c)

print("\n=== Consultorios de 'Medicina general' Y de la clínica 1 ===")
for c in session.query(Consultorio).filter(
        and_(Consultorio.especialidad == "Medicina general", Consultorio.clinica_id == 1)):
    print(c)

print("\n=== Veterinarios del consultorio 4 Y con correo @huellitas.com ===")
for v in session.query(Veterinario).filter(
        and_(Veterinario.consultorio_id == 4, Veterinario.correo.like("%@huellitas.com"))):
    print(v)

print("\n=== Historias con 'Otitis' Y atendidas desde el 2026-10-01 ===")
for h in session.query(HistoriaClinica).filter(
        and_(HistoriaClinica.diagnostico_principal == "Otitis",
             HistoriaClinica.fecha_atencion >= date(2026, 10, 1))):
    print(h)

session.close()