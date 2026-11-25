from configuracion import Session
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

session = Session()

# --- Punto 9: Clínicas y número de historias clínicas asociadas ---
print("=== CLÍNICAS Y SU NÚMERO DE HISTORIAS CLÍNICAS ===")
for clinica in session.query(Clinica).all():
    print(f"{clinica.nombre_comercial} ({clinica.direccion}) -> "
          f"{clinica.total_historias()} historias clínicas")

# --- all() sobre las demás entidades ---
print("\n=== CONSULTORIOS ===")
for c in session.query(Consultorio).all():
    print(f"{c.nombre} | {c.especialidad} | Clínica: {c.clinica.nombre_comercial}")

print("\n=== VETERINARIOS ===")
for v in session.query(Veterinario).all():
    print(f"{v.nombre_completo()} | {v.correo} | Lic: {v.licencia_profesional}")

print("\n=== HISTORIAS CLÍNICAS ===")
for h in session.query(HistoriaClinica).all():
    print(f"{h.fecha_atencion} | {h.nombre_mascota} | {h.diagnostico_principal} "
          f"| Vet: {h.veterinario.nombre_completo()}")

session.close()