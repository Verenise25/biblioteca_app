from typing import List
from modelos.libro import Libro
from modelos.prestamo import Prestamo


class BibliotecaService:
    def __init__(self) -> None:
        self.catalogo: List[Libro] = []
        self.prestamos: List[Prestamo] = []

    def agregar_libro(self, libro: Libro) -> None:
        self.catalogo.append(libro)

    def mostrar_catalogo(self) -> None:
        print("=== CATÁLOGO ===")
        for i, libro in enumerate(self.catalogo, start=1):
            print(f"{i}. {libro}")

    def crear_prestamo(self, usuario_nombre: str) -> Prestamo:
        prestamo = Prestamo(usuario_nombre)
        self.prestamos.append(prestamo)
        return prestamo