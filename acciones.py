import usuarios as users
import notas.acciones

class Acciones:
        def registro(self):
            print("\nasi que te te quieres registrar, llena el siguiente form")
            nombre = input("¿Cual es tu nombre? ")
            apellido = input("¿Cual es tu apellido? ")
            email = input("¿Cual es tu email? ")
            password = input("¿Cual es tu password? ")

            usuarios = users.Usuarios(nombre, apellido, email, password,)
            registro = usuarios.registrar()

            if registro[0] >= 1:
                print(f"Listo {registro[1].nombre} te has registrado")
            
            else:
                print("No te registraste")
        
        def login(self):
            print("Quieres hacer login, entonces ingresa tus credenciales")
            try:
                email = input("¿ingrese su email? ")
                password = input("¿ingrse su password? ")

                usuario = users.Usuarios('', '', email, password)
                login = usuario.identificar()

                if email == login[3]:
                    print(f"Bienvenido {login[1]}, te has logeado a la app")
                    self.elAccionar(login)

            except Exception as e:
                print(type(e))
                print(type(e).__name__)
                print("Error! Password y/o email incorrectos")
        
        def elAccionar(self, usuario):
            print("""
            Acciones disponibles:
               Crear nota( numero 1)
               Mostrar notas( numero 2)
               eliminar nota ( numero 3)
               Salir ( numero 4)
            """)

            accion = int(input("que quieres hacer? "))
            do = notas.acciones.Acciones()

            if accion == 1:
                do.crear(usuario)
                self.elAccionar(usuario)
                
                 
            elif accion == 2:
                do.mostrar(usuario)
                self.elAccionar(usuario)


            elif accion == 3:
                do.borrar(usuario)
                self.elAccionar(usuario)

            
            elif accion == 4:
                print(f"Gracias {usuario[1]}, nos vemos")
                exit()

            




            return




                
        


        
