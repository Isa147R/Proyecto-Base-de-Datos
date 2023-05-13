import psycopg2

try:

	conexion = psycopg2.connect(user = "postgres", password = "123456789", host="localhost", database = "Proyecto", port = "5432")
	print("Conexion correcta")
	
#Ejecutar las sentencias para mostrar los elementos tabla Zona
	print("--------ZONA---------")
	Tabla1 = """SELECT id, nombre 
    		  FROM Zona;"""
              
	cursor = conexion.cursor()
	cursor.execute(Tabla1)
	Zona = cursor.fetchall()
	for z in Zona:
		print("ID",z[0])
		print("nombre",z[1])

#Ejecutar las sentencias para mostrar los elementos tabla Accesibilidad
	print("--------ACCESIBILIDAD---------")
	Tabla2 = """SELECT id, nombre 
		  FROM Accesibilidad;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla2)
	Accesibilidad = cursor.fetchall()
	for a in Accesibilidad:
		print("ID",a[0])
		print("nombre",a[1])

#Ejecutar las sentencias para mostrar los elementos tabla Concesion
	print("--------CONCESION---------")
	Tabla3 = """SELECT id, nombre, codigo, anio_otorgado 
		  FROM Concesion;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla3)
	Concesion = cursor.fetchall()
	for c in Concesion:
		print("ID",c[0])
		print("nombre",c[1])
		print("codigo",c[2])
		print("anio_otorgado",c[3])

#Ejecutar las sentencias para mostrar los elementos tabla Dispositivo
	print("--------DISPOSITIVO---------")
	Tabla4 = """SELECT id, codigo 
		  FROM Dispositivo;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla4)
	Dispositivo = cursor.fetchall()
	for d in Dispositivo:
		print("ID",d[0])
		print("codigo",d[1])

#Ejecutar las sentencias para mostrar los elementos tabla Tipo_vehiculo
	print("--------TIPO_VEHICULO---------")
	Tabla5 = """SELECT id, nombre 
		  FROM Tipo_vehiculo;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla5)
	Tipo_vehiculo = cursor.fetchall()
	for t in Tipo_vehiculo:
		print("ID",t[0])
		print("nombre",t[1])

#Ejecutar las sentencias para mostrar los elementos tabla Marca
	print("--------MARCA---------")
	Tabla6 = """SELECT id, nombre 
		  FROM Marca;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla6)
	Marca = cursor.fetchall()
	for m in Marca:
		print("ID",m[0])
		print("nombre",m[1])

#Ejecutar las sentencias para mostrar los elementos tabla Nivel_emision
	print("--------NIVEL_EMISION---------")
	Tabla7 = """SELECT id, tipo
		  FROM Nivel_emision;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla7)
	Nivel_emision = cursor.fetchall()
	for n in Nivel_emision:
		print("ID",n[0])
		print("tipo",n[1])

#Ejecutar las sentencias para mostrar los elementos tabla Tipo_perfil
	print("--------TIPO_PERFIL---------")
	Tabla8 = """SELECT id, nombre 
		  FROM Tipo_perfil;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla8)
	Tipo_perfil = cursor.fetchall()
	for t in Tipo_perfil:
		print("ID",t[0])
		print("nombre",t[1])

#Ejecutar las sentencias para mostrar los elementos tabla Tipo_tarjeta
	print("--------TIPO_TARJETA---------")
	Tabla9 = """SELECT id, nombre 
		  FROM Tipo_tarjeta;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla9)
	Tipo_tarjeta = cursor.fetchall()
	for t in Tipo_tarjeta:
		print("ID",t[0])
		print("nombre",t[1])

#Ejecutar las sentencias para mostrar los elementos tabla Tipo_servicio
	print("--------TIPO_SERVICIO---------")
	Tabla10 = """SELECT id, nombre 
		  FROM Tipo_servicio;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla10)
	Tipo_servicio = cursor.fetchall()
	for t in Tipo_servicio:
		print("ID",t[0])
		print("nombre",t[1])

#Ejecutar las sentencias para mostrar los elementos tabla Mes
	print("--------MES---------")
	Tabla11 = """SELECT id, nombre 
        		  FROM Mes;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla11)
	Mes = cursor.fetchall()
	for m in Mes:
		print("ID",m[0])
		print("nombre",m[1])

#Ejecutar las sentencias para mostrar los elementos tabla Tipo_emisor
	print("--------TIPO_EMISOR---------")
	Tabla12 = """SELECT id, nombre, codigo 
		  FROM Tipo_emisor;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla12)
	Tipo_emisor = cursor.fetchall()
	for t in Tipo_emisor:
		print("ID",t[0])
		print("nombre",t[1])
		print("codigo",t[2])

#Ejecutar las sentencias para mostrar los elementos tabla Linea
	print("--------LINEA---------")
	Tabla13 = """SELECT id, nombre, id_Zona 
		  FROM Linea;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla13)
	Linea = cursor.fetchall()
	for l in Linea:
		print("ID",l[0])
		print("nombre",l[1])
		print("id_Zona",l[2])

#Ejecutar las sentencias para mostrar los elementos tabla Estacion
	print("--------ESTACION---------")
	Tabla14 = """SELECT id, nombre, id_Linea 
		  FROM Estacion;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla14)
	Estacion = cursor.fetchall()
	for e in Estacion:
		print("ID",e[0])
		print("nombre",e[1])
		print("id_Linea",e[2])

#Ejecutar las sentencias para mostrar los elementos tabla Salidas
	print("--------SALIDAS---------")
	Tabla15 = """SELECT id, total, intervalo, id_Estacion, id_Mes 
		  FROM Salidas;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla15)
	Salidas = cursor.fetchall()
	for s in Salidas:
		print("ID",s[0])
		print("total",s[1])
		print("intervalo",s[2])
		print("id_Estacion",s[3])
		print("id-Mes",s[4])

#Ejecutar las sentencias para mostrar los elementos tabla Tarjeta
	print("--------TARJETA---------")
	Tabla16 = """SELECT id, numero_tarjeta, id_Tipo_emisor, id_Tipo_perfil, id_Tipo_tarjeta 
		  FROM Tarjeta;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla16)
	Tarjeta = cursor.fetchall()
	for t in Tarjeta:
		print("ID",t[0])
		print("numero_tarjtea",t[1])
		print("id_Tipo_emisor",t[2])
		print("id_Tipo_perfil",t[3])
		print("id_Tipo_tarjeta",t[4])

#Ejecutar las sentencias para mostrar los elementos tabla Transaccion
	print("--------TRANSACCION---------")
	Tabla17 = """SELECT id, saldo_antes, saldo_despues, id_Tarjeta, id_Dispositivo 
		  FROM Transaccion;"""

	cursor = conexion.cursor() 
	cursor.execute(Tabla17)
	Transaccion = cursor.fetchall()
	for t in Transaccion:
		print("ID",t[0])
		print("saldo_antes",t[1])
		print("saldo_despues",t[2])
		print("id_Tarjeta",t[3])
		print("id_Dipositivo", t[4])

#Ejecutar las sentencias para mostrar los elementos tabla Servicio
	print("--------SERVICIO---------")
	Tabla18 = """SELECT id, id_Zona, id_Tipo_servicio, id_Tipo_vehiculo, id_Accesibilidad
		  FROM Servicio;"""

	cursor = conexion.cursor()
	cursor.execute(Tabla18)
	Servicio = cursor.fetchall()
	for s in Servicio:
		print("ID",s[0])
		print("id_Zona",s[1])
		print("id_Tipo_servicio", s[2])
		print("id_Tipo_vehiculo", s[3])
		print("id_Accesibilidad", s[4])

#Ejecutar las sentencias para mostrar los elementos tabla Vehiculo
	print("--------VEHICULO---------")
	Tabla19 = """SELECT id, etiqueta, matricula, id_Concesion, modelo, id_Marca, id_Nivel_emision, id_Zona 
		  FROM Vehiculo;"""

	cursor = conexion.cursor()  
	cursor.execute(Tabla19)
	Vehiculo = cursor.fetchall()
	for v in Vehiculo:
		print("ID",v[0])
		print("etiqueta",v[1])
		print("matricula",v[2])
		print("id_Concesion",v[3])
		print("modelo",v[4])
		print("id_Marca",v[5])
		print("id_Nivel_emision",v[6])
		print("id_Zona",v[7])

#Ejecutar las sentencias para mostrar los elementos tabla Pagar
	print("--------PAGAR---------")
	Tabla20 = """SELECT id,_Estacion, id_Transaccion 
		  FROM Pagar;"""

	cursor = conexion.cursor()  
	cursor.execute(Tabla20)
	Pagar = cursor.fetchall()
	for p in Pagar:
		print("id_Estacion",p[0])
		print("nombre",p[1])



except psycopg2.Error as e:
        print("Ocurrio un error",e)

finally:

        cursor.close()
        conexion.close()
