from datetime import date
from configuracion import engine, Session
from crear_base_entidades import (
    Base, Clinica, Consultorio, Veterinario, HistoriaClinica
)

Base.metadata.create_all(engine)
session = Session()

# Evita duplicar datos si se ejecuta dos veces
if session.query(Clinica).count() > 0:
    print("La base ya tiene datos. No se insertó nada.")
    session.close()
    raise SystemExit

# ---------- Clínicas ----------
clinica1 = Clinica(nombre_comercial="PetCare Guayaquil",
                   direccion="Av. 9 de Octubre 123, Guayaquil",
                   veterinario_responsable="Dr. Carlos Mendoza")
clinica2 = Clinica(nombre_comercial="Huellitas Quito",
                   direccion="Av. Amazonas 456, Quito",
                   veterinario_responsable="Dra. Lucía Paredes")
clinica3 = Clinica(nombre_comercial="Vet Amigos Cuenca",
                   direccion="Calle Larga 789, Cuenca",
                   veterinario_responsable="Dr. Andrés Vera")

# ---------- Consultorios ----------
cons1 = Consultorio(nombre="Consultorio 1", especialidad="Medicina general", clinica=clinica1)
cons2 = Consultorio(nombre="Consultorio 2", especialidad="Cirugía", clinica=clinica1)
cons3 = Consultorio(nombre="Consultorio A", especialidad="Dermatología", clinica=clinica2)
cons4 = Consultorio(nombre="Consultorio B", especialidad="Medicina general", clinica=clinica2)
cons5 = Consultorio(nombre="Consultorio 1", especialidad="Cirugía", clinica=clinica3)

# ---------- Veterinarios ----------
vet1 = Veterinario(nombres="Carlos", apellidos="Mendoza Ruiz",
                   correo="carlos.mendoza@petcare.com",
                   licencia_profesional="LIC-001", consultorio=cons1)
vet2 = Veterinario(nombres="María", apellidos="Alvarado Soto",
                   correo="maria.alvarado@petcare.com",
                   licencia_profesional="LIC-002", consultorio=cons2)
vet3 = Veterinario(nombres="Lucía", apellidos="Paredes León",
                   correo="lucia.paredes@huellitas.com",
                   licencia_profesional="LIC-003", consultorio=cons3)
vet4 = Veterinario(nombres="Jorge", apellidos="Castillo Mora",
                   correo="jorge.castillo@huellitas.com",
                   licencia_profesional="LIC-004", consultorio=cons4)
vet5 = Veterinario(nombres="Andrés", apellidos="Vera Salazar",
                   correo="andres.vera@vetamigos.com",
                   licencia_profesional="LIC-005", consultorio=cons5)

# ---------- Historias clínicas ----------
historias = [
    HistoriaClinica(fecha_atencion=date(2026, 9, 10), diagnostico_principal="Otitis",
                    tratamiento_prescrito="Gotas óticas por 7 días",
                    nombre_mascota="Max", veterinario=vet1),
    HistoriaClinica(fecha_atencion=date(2026, 9, 15), diagnostico_principal="Gastroenteritis",
                    tratamiento_prescrito="Dieta blanda y suero oral",
                    nombre_mascota="Luna", veterinario=vet1),
    HistoriaClinica(fecha_atencion=date(2026, 10, 2), diagnostico_principal="Fractura de pata",
                    tratamiento_prescrito="Cirugía y reposo 4 semanas",
                    nombre_mascota="Rocky", veterinario=vet2),
    HistoriaClinica(fecha_atencion=date(2026, 10, 20), diagnostico_principal="Dermatitis alérgica",
                    tratamiento_prescrito="Antihistamínico y shampoo medicado",
                    nombre_mascota="Bella", veterinario=vet3),
    HistoriaClinica(fecha_atencion=date(2026, 11, 5), diagnostico_principal="Otitis",
                    tratamiento_prescrito="Limpieza ótica y antibiótico",
                    nombre_mascota="Toby", veterinario=vet4),
    HistoriaClinica(fecha_atencion=date(2026, 11, 12), diagnostico_principal="Parvovirus",
                    tratamiento_prescrito="Hospitalización y fluidoterapia",
                    nombre_mascota="Kira", veterinario=vet4),
    HistoriaClinica(fecha_atencion=date(2026, 11, 14), diagnostico_principal="Esterilización",
                    tratamiento_prescrito="Cirugía programada y analgésicos",
                    nombre_mascota="Nina", veterinario=vet5),
]

session.add_all([clinica1, clinica2, clinica3])   # el cascade guarda el resto
session.add_all(historias)
session.commit()
session.close()
print("Datos insertados correctamente.")