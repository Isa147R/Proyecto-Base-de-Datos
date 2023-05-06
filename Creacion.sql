CREATE TABLE Zona
(
	id serial,
	nombre varchar(20),
	PRIMARY KEY(id)
);

CREATE TABLE Accesibilidad
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Concesion
(
	id serial,
	nombre varchar(30),
	codigo varchar(15),
	anio_otorgado integer,
	PRIMARY KEY(id)
);

CREATE TABLE Dispositivo
(
	id serial,
	codigo int,
	PRIMARY KEY(id)
);

CREATE TABLE Tipo_vehiculo
(
	id serial,
	nombre varchar(30),
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

CREATE TABLE Tipo_perfil
(
	id serial,
	nombre varchar(40),
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
	id serial,
	nombre varchar(20),
	PRIMARY KEY(id)
);

CREATE TABLE Mes
(
	id serial,
	nombre varchar(35),
	PRIMARY KEY(id)
);

CREATE TABLE Tipo_emisor
(
	id serial,
	nombre varchar(50),
	codigo integer,
	PRIMARY KEY(id)
);

CREATE TABLE Linea
(
	id serial,
	nombre varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Estacion
(
	id serial,
	nombre varchar(60),
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

CREATE TABLE Tarjeta
(
	id serial,
	numero_tarjeta varchar(100),
	id_Tipo_emisor integer,
	id_Tipo_perfil integer,
	id_Tipo_tarjeta integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Tipo_emisor)
		REFERENCES Tipo_emisor(id),
	FOREIGN KEY (id_Tipo_perfil)
		REFERENCES Tipo_perfil(id),
	FOREIGN KEY (id_Tipo_tarjeta)
		REFERENCES Tipo_tarjeta(id)
);


CREATE TABLE Transaccion
(
	id serial,
	saldo_antes float,
	saldo_despues float,
	id_Tarjeta integer,
	id_Dispositivo integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Dispositivo)
		REFERENCES Dispositivo(id),
	FOREIGN KEY (id_Tarjeta)
		REFERENCES Tarjeta(id)
);

CREATE TABLE Servicio
(
	id serial,
	id_Zona integer,
	id_Tipo_servicio integer,
	id_Tipo_vehiculo integer,
	id_Accesibilidad integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Zona)
		REFERENCES Zona(id),
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
	etiqueta varchar(10),
	matricula varchar(10),
	id_Concesion integer,
	modelo integer,
	id_Marca integer,
	id_Nivel_emision integer,
	id_Zona integer,
	PRIMARY KEY(id),
	FOREIGN KEY (id_Concesion)
		REFERENCES Concesion(id),
	FOREIGN KEY (id_Marca)
		REFERENCES Marca(id),
	FOREIGN KEY(id_Nivel_emision)
		REFERENCES Nivel_emision(id),
	FOREIGN KEY(id_Zona)
		REFERENCES Zona(id)
);

CREATE TABLE Pagar
(
	id_Estacion integer,
	id_Transaccion integer,
	FOREIGN KEY (id_Transaccion)
		REFERENCES Transaccion(id),
	FOREIGN KEY (id_Estacion)
		REFERENCES Estacion(id)
);












