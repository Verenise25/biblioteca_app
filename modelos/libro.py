from dataclasses import dataclass

@dataclass
class Libro:
    titulo: str
    autor: str
    disponible: bool = True

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"