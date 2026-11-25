from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import engine

Base = declarative_base()


class Clinica(Base):
    __tablename__ = "clinica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_comercial = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    consultorios = relationship(
        "Consultorio", back_populates="clinica", cascade="all, delete-orphan"
    )

    def total_historias(self):
        """Cuenta las historias clínicas de todos los veterinarios de la clínica."""
        return sum(
            len(vet.historias)
            for consultorio in self.consultorios
            for vet in consultorio.veterinarios
        )

    def __repr__(self):
        return (f"Clinica(id={self.id}, nombre_comercial='{self.nombre_comercial}', "
                f"direccion='{self.direccion}', "
                f"veterinario_responsable='{self.veterinario_responsable}')")


class Consultorio(Base):
    __tablename__ = "consultorio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)          # nombre o número
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinica.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship(
        "Veterinario", back_populates="consultorio", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (f"Consultorio(id={self.id}, nombre='{self.nombre}', "
                f"especialidad='{self.especialidad}', clinica_id={self.clinica_id})")


class Veterinario(Base):
    __tablename__ = "veterinario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False, unique=True)
    licencia_profesional = Column(String(50), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey("consultorio.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias = relationship(
        "HistoriaClinica", back_populates="veterinario", cascade="all, delete-orphan"
    )

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def __repr__(self):
        return (f"Veterinario(id={self.id}, nombre='{self.nombre_completo()}', "
                f"correo='{self.correo}', licencia='{self.licencia_profesional}')")


class HistoriaClinica(Base):
    __tablename__ = "historia_clinica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico_principal = Column(String(200), nullable=False)
    tratamiento_prescrito = Column(String(300), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinario.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias")

    def __repr__(self):
        return (f"HistoriaClinica(id={self.id}, fecha={self.fecha_atencion}, "
                f"mascota='{self.nombre_mascota}', "
                f"diagnostico='{self.diagnostico_principal}')")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")