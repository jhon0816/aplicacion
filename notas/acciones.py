import notas.nota as notes


class Acciones:
    def crear(self, usuario):
        print(f"\n Vamos a crear una nueva nota {usuario[1]}")

        titulo = input("Introduce un titulo: ")
        descripcion = input("Pon lo que quieras en tu nota: ") 

        nota = notes.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Guardaste tu nota {nota.titulo}")
        else:
            print(f"Tu nota no se guardo {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\n Mira tus notas ve! {usuario[1]} ")

        nota = notes.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n _____________________________")
            print(f"\n{nota[2]}")
            print(f"\n{nota[3]}")
            print("\n _____________________________")
    
    def borrar(self, usuario):
        print(f"{usuario[1]}, vamos a borrar notas")

        titulo = input("\n Introduce el titulo de la nota que quieres borrar: ")

        nota = notes.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Tu nota {nota.titulo} fue eliminada")
        
        else:
            print("Tu nota no se borro, escribe bien el nombre")






    