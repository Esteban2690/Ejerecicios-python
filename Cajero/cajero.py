from datetime import datetime

class Usuario:
    usuarios = {}
    usuarios_saldo = {}
    movimientos = {}

    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.saldo = 0
        self.contraseña = contraseña

    def registrar_usuario(self):
        if self.nombre not in Usuario.usuarios:
            Usuario.usuarios[self.nombre] = self.contraseña
            Usuario.usuarios_saldo[self.nombre] = self.saldo
            print(f"¡Usuario '{self.nombre}' registrado exitosamente!")
        else:
            print("Nombre de usuario ya existe. Intenta con otro nombre.")

    def iniciar_sesion(self):
        if self.nombre in Usuario.usuarios and Usuario.usuarios[self.nombre] == self.contraseña:
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            self.guardar_saldo()
            self.registrar_movimiento(f"Depósito de ${cantidad}")
            print(f"{self.nombre}, has depositado ${cantidad}. Tu nuevo saldo es ${self.saldo}.")
        else:
            print("La cantidad debe ser mayor a cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            self.guardar_saldo()
            self.registrar_movimiento(f"Retiro de ${cantidad}")
            print(f"{self.nombre}, has retirado ${cantidad}. Tu nuevo saldo es ${self.saldo}.")
        else:
            print("La cantidad debe ser mayor a cero y no puede exceder tu saldo.")

    def consultar_saldo(self):
        self.actualizar_saldo()
        print(f"{self.nombre}, tu saldo actual es de ${self.saldo}.")

    def ver_movimientos(self):
        if self.nombre in Usuario.movimientos:
            print(f"Historial de movimientos para {self.nombre}:")
            for movimiento in Usuario.movimientos[self.nombre]:
                print(movimiento)
        else:
            print("No hay movimientos para mostrar.")

    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
        Usuario.usuarios[self.nombre] = nueva_contraseña
        print("Contraseña cambiada exitosamente.")

    def registrar_movimiento(self, movimiento):
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        movimiento_con_fecha = f"{fecha_hora_actual} - {movimiento}"
        if self.nombre in Usuario.movimientos:
            Usuario.movimientos[self.nombre].append(movimiento_con_fecha)
        else:
            Usuario.movimientos[self.nombre] = [movimiento_con_fecha]

    def guardar_saldo(self):
        Usuario.usuarios_saldo[self.nombre] = self.saldo

    def actualizar_saldo(self):
        self.saldo = Usuario.usuarios_saldo[self.nombre]

while True:
    print("\nBienvenido al cajero automático")
    print("Selecciona una opción:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = int(input("Ingresa el número de tu opción: "))
    if opcion == 1:
        nombre = input("Ingresa tu nombre de usuario: ")
        contraseña = input("Ingresa tu contraseña: ")
        usuario = Usuario(nombre, contraseña)
        usuario.registrar_usuario()
    elif opcion == 2:
        nombre = input("Ingresa tu nombre de usuario: ")
        contraseña = input("Ingresa tu contraseña: ")
        usuario = Usuario(nombre, contraseña)
        if usuario.iniciar_sesion():
            while True:
                print("\nBienvenido, {}".format(usuario.nombre))
                print("Selecciona una opción:")
                print("1. Depositar dinero")
                print("2. Retirar dinero")
                print("3. Consultar saldo")
                print("4. Ver movimientos realizados")
                print("5. Cambiar contraseña")
                print("6. Salir")
                opcion_usuario = int(input("Ingresa el número de tu opción: "))
                if opcion_usuario == 1:
                    cantidad = float(input("Ingrese la cantidad a depositar: "))
                    usuario.depositar(cantidad)
                elif opcion_usuario == 2:
                    cantidad = float(input("Ingrese la cantidad a retirar: "))
                    usuario.retirar(cantidad)
                elif opcion_usuario == 3:
                    usuario.consultar_saldo()
                elif opcion_usuario == 4:
                    usuario.ver_movimientos()
                elif opcion_usuario == 5:
                    nueva_contraseña = input("Ingresa tu nueva contraseña: ")
                    usuario.cambiar_contraseña(nueva_contraseña)
                elif opcion_usuario == 6:
                    usuario.guardar_saldo()  # Guardar el saldo antes de salir
                    print("Gracias por utilizar el cajero automático")
                    break
                else:
                    print("Opción inválida. Por favor, selecciona una opción válida.")
    elif opcion == 3:
        print("Gracias por utilizar el cajero automático")
        for nombre_usuario, saldo_usuario in Usuario.usuarios_saldo.items():
            print(f"Usuario: {nombre_usuario}, Saldo: ${saldo_usuario}")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")