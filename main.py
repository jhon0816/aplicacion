import acciones


print(
    """
    Acciones disponobles:
          - registro
          - login
          para registrarte digita el numero 1
          para hacer login digita el numero 2

    """
)


loginYregistro = acciones.Acciones()
accion =int(input("Que quieres hacer? "))

if accion == 1:
    loginYregistro.registro()
  
elif accion == 2:
    loginYregistro.login()
   