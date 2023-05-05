CREATE TABLE Modelo
(
	id serial,
	nombre varchar(15),
	PRIMARY KEY(id)
);

CREATE TABLE Marca
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Nivel_emision
(
	id serial,
	tipo varchar(45),
	PRIMARY KEY(id)
);

CREATE TABLE Operador
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Concesion
(
	id serial,
	anio_otorgado integer,
	PRIMARY KEY(id)
);

CREATE TABLE dispositivo
(
	id integer,
	PRIMARY KEY(id)
);

CREATE TABLE Tipo_perfil
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Tipo_tarjeta
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Tipo_servicio
(
	id integer,
	nombre varchar(7),
	PRIMARY KEY(id)
);

CREATE TABLE Tipo_vehiculo
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Accesibilidad
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Mes
(
	id serial,
	nombre varchar(35),
	PRIMARY KEY(id)
);

CREATE TABLE tipo_emisor
(
	id serial,
	tipo varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Linea
(
	id serial,
	nombre varchar(30),
	id_Concesion integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Concesion)
		REFERENCES Concesion(id)
);

CREATE TABLE Estacion
(
	id serial,
	nombre varchar(30),
	id_Linea integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Linea)
		REFERENCES Linea(id)
);

CREATE TABLE Salidas
(
	id serial,
	total integer,
	intervalo time,
	id_Estacion integer,
	id_Mes integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Estacion)
		REFERENCES Estacion(id),
	FOREIGN KEY (id_Mes)
		REFERENCES Mes(id)
);

CREATE TABLE Emisor
(
	id serial,
	nombre varchar(30),
	id_tipo_emisor integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_tipo_emisor)
		REFERENCES tipo_emisor(id)
);

CREATE TABLE Tarjeta
(
	id serial,
	numero_tarjeta varchar(50),
	id_Emisor integer,
	id_Tipo_perfil integer,
	id_tipo_tarjeta integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Emisor)
		REFERENCES Emisor(id),
	FOREIGN KEY (id_Tipo_perfil)
		REFERENCES Tipo_perfil(id),
	FOREIGN KEY (id_tipo_tarjeta)
		REFERENCES tipo_tarjeta(id)
);

CREATE TABLE Transaccion
(
	id serial,
	saldo_antes integer,
	saldo_despues integer,
	id_dispositivo integer,
	id_Tarjeta integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_dispositivo)
		REFERENCES dispositivo(id),
	FOREIGN KEY (id_Tarjeta)
		REFERENCES Tarjeta(id)
);

CREATE TABLE Servicio
(
	id serial,
	id_Linea integer,
	id_Tipo_vehiculo integer,
	id_Tipo_servicio integer,
	id_Accesibilidad integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Linea)
		REFERENCES Linea(id),
	FOREIGN KEY (id_Tipo_vehiculo)
		REFERENCES Tipo_vehiculo(id),
	FOREIGN KEY (id_Tipo_servicio)
		REFERENCES Tipo_servicio(id),
	FOREIGN KEY (id_Accesibilidad)
		REFERENCES Accesibilidad(id)
);


CREATE TABLE Vehiculo
(
	id serial,
	etiqueta integer,
	matricula varchar(6),
	id_Servicio integer,
	id_Concesion integer,
	id_Modelo integer,
	id_Marca integer,
	id_Nivel_emision integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Servicio)
		REFERENCES Servicio(id),
	FOREIGN KEY (id_Concesion)
		REFERENCES Concesion(id),
	FOREIGN KEY (id_Modelo)
		REFERENCES Modelo(id),
	FOREIGN KEY (id_Marca)
		REFERENCES Marca(id),
	FOREIGN KEY(id_Nivel_emision)
		REFERENCES Nivel_emision(id)
);

CREATE TABLE Trabajar
(
	id_Concesion integer,
	id_Operador integer,
	FOREIGN KEY (id_Concesion)
		REFERENCES Concesion(id),
	FOREIGN KEY (id_Operador)
		REFERENCES Operador(id)
);

CREATE TABLE Pagar
(
	id_Transaccion integer,
	id_Estacion integer,
	FOREIGN KEY (id_Transaccion)
		REFERENCES Transaccion(id),
	FOREIGN KEY (id_Estacion)
		REFERENCES Estacion(id)
);





