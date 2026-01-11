from modelos.libro import Libro
from servicios.biblioteca_service import BibliotecaService

def main() -> None:
    biblioteca = BibliotecaService()

    # Crear libros
    libro1 = Libro("1984", "George Orwell")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")
    libro3 = Libro("Python Básico", "Guido van Rossum")

    # Agregar al catálogo
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Mostrar catálogo
    biblioteca.mostrar_catalogo()

    # Crear préstamo
    prestamo = biblioteca.crear_prestamo("Carlos")

    # Agregar libros al préstamo
    prestamo.agregar_libro(libro1)
    prestamo.agregar_libro(libro2)

    # Mostrar resumen
    print("\n=== RESUMEN DEL PRÉSTAMO ===")
    print(prestamo.resumen())

if __name__ == "__main__":
    main()