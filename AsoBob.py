from datetime import datetime
#----------------Funciones----------------------
def calcularCuotas(monto, tasa):
  interes = round(monto * tasa, 2)
  cuotaSinInteres = round(monto / plazo,2)
  cuotaConInteres = round((monto+interes)/plazo,2) 
  
  print("---Resumen---")
  print("Monto de prestamo: ",monto)
  print("Interes: ",interes)
  print("Total(Con interes): ", monto+interes)
  print("Cuota sin interes: ", cuotaSinInteres)
  print("Cuota con interes: ", cuotaConInteres)
  print("-------------")
  print()

def menu():
  print("---------Menu---------")
  print("1.Registrar Empleado.")
  print("2.Mostrar Empleados.")
  print("3.Modificar Empleado.")
  print("4.Solicitar Prestamo.")
  print("5.Calculo de cuotas.")
  print("6.Mostrar Ahorros y Prestamos del Asociado.")
  print("7.Reportes.")
  print("8.Mostrar Prestamos.")
  print("9.Pago de Servicios Publicos y Rebajos")
  print("10.Salir")

  op = input("Ingrese una opción: ")
  if op.isnumeric():
    return int(op)
  else:
    return 0


def registrarEmpleado():
  trabajador = []

  print()
  print("---Registrar Empleado---")
  trabajador.append(int(input("Ingrese codigo empleado: ")))
  trabajador.append(input("Ingrese nombre completo: "))
  trabajador.append(input("Ingrese cedula: "))
  trabajador.append(input("Ingrese telefono: "))
  trabajador.append(input("Ingrese direccion: "))
  trabajador.append(input("Ingrese puesto: "))
  trabajador.append(float(input("Ingrese ahorro: ")))
  trabajador.append(int(input("Ingrese años laborando: ")))

  listaTrabajadores.append(trabajador)

def mostrarPrestamos():
  print()
  print("---Mostrar Préstamos---")
  for i in range(len(listaPrestamos)):
    print("Prestamo: #", i)
    if (listaPrestamos[i][0] == 1):
      print("Tipo de prestamo: Personal")
    elif (listaPrestamos[i][0] == 2):
      print("Tipo de prestamo: Estudiantil")
    elif (listaPrestamos[i][0] == 3):
      print("Tipo de prestamo: Salud")

    print("Codigo empleado: ", listaPrestamos[i][1])
    print("Monto original: ", listaPrestamos[i][2])
    print("Saldo actual: ", listaPrestamos[i][3])
    print("Plazo: ", listaPrestamos[i][4])
    print("Fecha: ", listaPrestamos[i][5])
    print("-----------------------")
  print()

def mostrarPrestamosEmpleado(codigo):
  print()
  print("---Préstamos del empleado ",codigo,"---")
  for i in range(len(listaPrestamos)):
    if(codigo == listaPrestamos[i][1]):
      print("Prestamo: #", i)
      if (listaPrestamos[i][0] == 1):
        print("Tipo de prestamo: Personal")
      elif (listaPrestamos[i][0] == 2):
        print("Tipo de prestamo: Estudiantil")
      elif (listaPrestamos[i][0] == 3):
        print("Tipo de prestamo: Salud")

      print("Codigo empleado: ", listaPrestamos[i][1])
      print("Monto original: ", listaPrestamos[i][2])
      print("Saldo actual: ", listaPrestamos[i][3])
      print("Plazo: ", listaPrestamos[i][4])
      print("Fecha: ", listaPrestamos[i][5])
      print("-----------------------")
    print()

def mostrarEmpleados():
  print()
  print()
  print("---Empleados---")
  for f in range(len(listaTrabajadores)):
    print("Trabajador #", f + 1)
    for c in range(len(listaTrabajadores[0])):
      print(ordenDatos[c],": ",listaTrabajadores[f][c])

    print("---------------")

def mostrarEmpleado(codigo):
  print()
  print()
  print("---Empleados---")
  for f in range(len(listaTrabajadores)):
    if(codigo == listaTrabajadores[f][0]):
      print("Trabajador #", f + 1)
      for c in range(len(listaTrabajadores[0])):
        print(ordenDatos[c],": ",listaTrabajadores[f][c])
      print("---------------")
      break;

def existeEmpleado(codigo):
  for i in range(len(listaTrabajadores)):
    if (codigo == listaTrabajadores[i][0]):
      return listaTrabajadores[i]
  return ""

def modificarEmpleado(empleado):
  print()
  print("---Datos nuevos---")
  empleado

  empleado[1] = (input("Ingrese nombre completo: "))
  empleado[2] = (input("Ingrese cedula: "))
  empleado[3] = (input("Ingrese telefono: "))
  empleado[4] = (input("Ingrese direccion: "))
  empleado[5] = (input("Ingrese puesto: "))
  empleado[6] = (float(input("Ingrese ahorro: ")))
  empleado[7] = (int(input("Ingrese años laborando: ")))

  for i in range(len(listaTrabajadores)):
    if (codigo == listaTrabajadores[i][0]):
      listaTrabajadores[i] = empleado

def solicitarPrestamo(tipoPrestamo,montoMinimo, montoMaximo, plazoMinimo, plazoMaximo, añosMinimo):
  tienePrestamo = False

  print()
  # Verificar si el empleado tiene suficientes años laborando
  if (empleado[7] >= añosMinimo):
    # Recorrer listaPrestamos
    for i in range(len(listaPrestamos)):
      # Verificamos si existe algun prestamo para ese empleado
      if (empleado[0] == listaPrestamos[i][1]):
        # Verificar el tipo de prestamo
        if (listaPrestamos[i][0] == tipoPrestamo):
          print("El empleado ya tiene un prestamo en esa linea de crédito.")
          tienePrestamo = True
          break

    if (tienePrestamo == False):
      print("Prestamo personal: (", montoMinimo," a ", montoMaximo,")")
      monto = float(input("Ingrese el monto de préstamo: "))

      if (monto >= montoMinimo and monto <= montoMaximo):
        prestamo.append(monto)
        prestamo.append(monto)

        print("Plazo de prestamo(En meses): 1 mes a maximo un 1 año.")
        plazo = int(input("Ingrese el plazo: "))

        if (plazo >= plazoMinimo and plazo <= plazoMaximo):
          prestamo.append(plazo)
          # Agregamos fecha del prestamo
          fecha = datetime.now()
          prestamo.append(fecha.date())

          listaPrestamos.append(prestamo)
          print("Se ha registrado el prestamo exitosamente.")

      else:
        print("El monto no cumple con los requisitos.")
  else:
    print("Cantidad de años laborando es insuficiente.")

def mostrarAhorros(empleado):
  print("---Ahorros del empleado ",empleado[0],"---")
  print("Saldo: ",empleado[6])

def pagoServicios():
  deduciones = []
  print()
  print("---Pago de servicios---")
  print("Tipo de pago:")
  print("1 - Contado")
  print("2 - Rebajo del salario")
  op = int(input("Escoja una opción: "))

  print()
  servicio = input("Ingrese el nombre del servicio: ")
  montoServicio = float(input("Ingrese el monto a pagar: "))

  if( op == 2):
      rebajo(servicio, montoServicio)
  else:
    print("Pago efectuado...")
    print("Servicio: ", servicio)
    print("Monto cancelado: ", montoServicio)
  listadeducciones.append(deduciones)

def rebajo(servicio, montoServicio):
  print()
  codigo = int(input("Ingrese codigo de empleado: "))
  empleado = existeEmpleado(codigo)

  if(empleado != ""):
    print("Pago efectuado...")
    print("Servicio: ", servicio)
    print("Monto cancelado: ", montoServicio)
    print("Monto a descontar del próximo pago: ", montoServicio + (montoServicio*0.2))
  else:
    print("No existe un empleado con ese código.")


def leerArchivo(ruta):
  archivo = open(ruta)
  print(archivo.read())


def guardarEmpleados(ruta):
  archivo = open(ruta, "w")

  fecha = datetime.now()

  texto = "Empresa: Bob El Constructor \n" \
          "Asociación: Asobob \n" \
          "Fecha: "+str(fecha.date())+" \n" \
          "Informe: Lista Empleados \n\n"



  for f in range(len(listaTrabajadores)):
    texto += "Empleado#" + str(f) + "\n"
    for c in range(len(listaTrabajadores[0])):
      texto += str(ordenDatos[c]) + ": <" +str(listaTrabajadores[f][c])+">\n"
    texto += "\n"


  archivo.write(texto)


def cargarEmpleados():
  archivo = open("empleados.txt")
  with archivo as item:
    lines = item.readlines()

  trabajador = []
  for i in lines:
    for c in range(len(i)):
      if i[c] == "<":
          ini = i.find("<")
          fin = i.find(">")
          trabajador.append(i[ini+1:fin])
      if len(trabajador) == 8:
        trabajador[0] = int(trabajador[0])
        trabajador[6] = float(trabajador[6])
        trabajador[7] = int(trabajador[7])
        listaTrabajadores.append(trabajador)
        trabajador = []


def guardarPrestamos():
  archivo = open("prestamos.txt", "w")

  fecha = datetime.now()

  texto = "Empresa: Bob El Constructor \n" \
          "Asociación: Asobob \n" \
          "Fecha: "+str(fecha.date())+" \n" \
          "Informe: Lista Prestamos \n\n"



  for f in range(len(listaPrestamos)):
    texto += "Prestamo#" + str(f) + "\n"
    for c in range(len(listaPrestamos[0])):
      texto += str(ordenDatosPrestamo[c]) + ": <" +str(listaPrestamos[f][c])+">\n"
    texto += "\n"


  archivo.write(texto)


def cargarPrestamos():
  archivo = open("prestamos.txt")
  with archivo as item:
    lines = item.readlines()

  prestamo = []
  for i in lines:
    for c in range(len(i)):
      if i[c] == "<":
          ini = i.find("<")
          fin = i.find(">")
          prestamo.append(i[ini+1:fin])
      if len(prestamo) == 6:
        prestamo[0] = int(prestamo[0])
        prestamo[1] = int(prestamo[1])
        prestamo[2] = float(prestamo[2])
        prestamo[3] = float(prestamo[3])
        prestamo[4] = int(prestamo[4])
        listaPrestamos.append(prestamo)
        prestamo = []


def leerEmpleados():
  archivo = open("empleados.txt")
  print(archivo.read())


def leerPrestamos():
  archivo = open("prestamos.txt")
  print(archivo.read())


def guardardeducciones():
  archivo = open("deducciones.txt", "w")

  fecha = datetime.now()

  texto = "Empresa: Bob El Constructor \n" \
          "Asociación: Asobob \n" \
          "Fecha: " + str(fecha.date()) + " \n" \
          "Informe: Lista de Deduciones \n\n"

  for f in range(len(listadeducciones)):
    texto += "Empleado#" + str(f) + "\n"
    for c in range(len(listadeducciones[0])):
      texto += str(ordenDeduciones[c]) + ": <" + str(listadeducciones[f][c]) + ">\n"
    texto += "\n"

  archivo.write(texto)

def cargardeducciones():
  archivo = open("deducciones.txt")
  with archivo as item:
    lines = item.readlines()

  deduciones = []
  for i in lines:
    for c in range(len(i)):
      if i[c] == "<":
          ini = i.find("<")
          fin = i.find(">")
          deduciones.append(i[ini+1:fin])
      if len(deduciones) == 6:
        deduciones[1] = float(deduciones[1])
        listadeducciones.append(deduciones)
        deduciones = []

def leerdeducciones():
  archivo = open("deducciones.txt")
  print(archivo.read())

#Definicion de variables
print("Bienvenido a ... ")
print("""                                
    __                ____              
    / |               /   )          /  
---/__|---__----__---/__ /-----__---/__-
  /   |  (_ ` /   ) /    )   /   ) /   )
_/____|_(__)_(___/_/____/___(___/_(___/_
""")

#Modelo de datos utilizado las listas de los trabajadores.
ordenDatos = ["CodigoEmpleado",
              "Nombre",
              "Cedula",
              "Telefono",
              "Direccion",
              "Puesto",
              "Ahorro",
              "AñosLaborando"]

ordenDatosPrestamo = ["Tipo",
                      "Empleado",
                      "Monto Original",
                      "Monto Actual",
                      "Plazo",
                      "Fecha"]

ordenDeduciones = ["Tipo de pago",
                   "Monto Ingresado",
                   "Monto de Deduccion",
                   "Codigo del Empleado",
                   "Nombre",
                   "Cedula",
                   "Fecha"]


#Lista de trabajadores y deduciones
listaTrabajadores = []
listadeducciones = []


#Lista de pretamos
# Indice 0 = Tipo de prestamo 1 = Personal, 2 = Estudiantil y 3 = Salud.
# Indice 1 = Codigo de empleado.
# Indice 2 = Monto Original del prestamo.
# Indice 3 = Saldo actual.
# Indice 4 = Plazo de pago del prestamos(En meses)
# Indice 5 = Fecha de solicitud del prestamo.

listaPrestamos = []






#Main-------------------------------------------------------------------------------------
#Entrada de datos

cargarEmpleados()
cargarPrestamos()
cargardeducciones()

opcion=0

while(opcion != 10):
  opcion = menu()

  #Registrar Empleados
  if(opcion==1):
    registrarEmpleado()
    guardarEmpleados("empleados.txt")

  #Mostrar Empleados
  elif(opcion==2):
    mostrarEmpleados()
  
  #Modificar Empleados
  elif(opcion==3):
    print()
    print("---Modificar Empleado---")
    codigo = int(input("Ingrese codigo del empleado:"))

    empleado = existeEmpleado(codigo)

    if(empleado != ""):
      mostrarEmpleado(empleado[0])
      modificarEmpleado(empleado)

    else:
      print("No existe un empleado con ese codigo.")

    guardarEmpleados("empleados.txt")
  #Solicitar prestamos
  elif(opcion == 4):
    print()
    print("---Solicitar Prestamo---")
    codigo = int(input("Ingrese codigo de empleado: "))
    empleado = ""

    #Validamos que exista un empleado con el codigo.
    empleado = existeEmpleado(codigo)
    
    #Si el empleado existe
    if(empleado != ""):
      print("El empleado tiene ",empleado[7]," años trabajando para la empresa.")

      prestamo = []

      print()
      print("---Tipos de préstamos---")
      print("1 = Personal")
      print("2 = Estudiantil")
      print("3 = Salud")
      prestamo.append(int(input("Ingrese el tipo de prestamo: ")))
      prestamo.append(empleado[0])

      #Solicitud de prestamo personal
      if(prestamo[0] == 1):

        solicitarPrestamo(prestamo[0], 100000, 500000, 1, 12, 1)

      #Solicitud de prestamo estudiantil
      elif(prestamo[0] == 2):

        solicitarPrestamo(prestamo[0], 1000000, 2000000, 1, 24, 2)

      #Solicitud de prestamo de salud
      elif(prestamo[0] == 3):

        solicitarPrestamo(prestamo[0], 500000, 1000000, 1, 12, 0)
    else:
      print("El empleado no existe.")
    guardarPrestamos()


  elif(opcion == 5):
    print()
    print("---Calculo de cuotas---")
    monto = float(input("Ingrese el monto de la deuda: "))
    tipo = int(input("Ingrese el tipo de linea(1=Personal, 2=Estudiantil y 3=Salud): "))
    plazo = int(input("Ingrese plazo original del prestamo(En meses): "))
    print()
    
    if(tipo==1):
      calcularCuotas(monto, 0.14)
    elif(tipo==2):
      calcularCuotas(monto, 0.12)
    elif(tipo==3):
      calcularCuotas(monto, 0.8)

  elif(opcion == 6):
    codigo = int(input("Ingrese codigo de empleado: "))
    empleado = existeEmpleado(codigo)

    if(empleado != ""):
      print()
      print("--------ESTADO ACTUAL--------")
      mostrarAhorros(empleado)
      mostrarPrestamosEmpleado(codigo)

    else:
      print("No existe un empleado con ese código.")

  elif(opcion == 7):
    print()
    print("---REPORTES---")
    print("1-Reporte Empleados")
    print("2-Reporte Prestamos")
    reporte = input("Ingrese el numero de reporte: ")

    print()
    print("-----------------------------------------")
    if(reporte == "1"):

      leerEmpleados()
    elif(reporte == "2"):
      leerPrestamos()

    print("-----------------------------------------")


  elif(opcion == 8):
    mostrarPrestamos()



  elif(opcion == 9):
    print()
    print("---Pago de Servicios Publicos y Deduciones---")
    print("1-Pago de Servicios")
    print("2-Reporte de Deducciones")
    reporte = input("Ingrese una Opccion: ")

    print()
    print("-----------------------------------------")
    if (reporte == "1"):

      pagoServicios()
    elif (reporte == "2"):
      leerdeducciones()

    print("-----------------------------------------")



  


















