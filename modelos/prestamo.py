from dataclasses import dataclass, field
from typing import List
from .libro import Libro


@dataclass
class Prestamo:
    usuario_nombre: str
    libros: List[Libro] = field(default_factory=list)

    def agregar_libro(self, libro: Libro) -> None:
        if libro.disponible:
            self.libros.append(libro)
            libro.disponible = False

    def resumen(self) -> str:
        lineas = [f"Usuario: {self.usuario_nombre}"]
        for libro in self.libros:
            lineas.append(f" - {libro.titulo}")
        return "\n".join(lineas)