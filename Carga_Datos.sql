COPY Zona (nombre) FROM '/Users/isabela/Zona.csv' WITH DELIMITER ';' CSV HEADER;
INSERT INTO Zona(nombre) VALUES ('NORTE');
Select * from Zona;

COPY Accesibilidad (nombre) FROM '/Users/isabela/Accesibilidad.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Accesibilidad;

COPY Concesion (nombre, codigo, anio_otorgado ) FROM '/Users/isabela/Concesion.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Concesion;

COPY Dispositivo (codigo) FROM '/Users/isabela/Dispositivo.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Dispositivo;

COPY Tipo_vehiculo (nombre)  FROM '/Users/isabela/tipo_vehiculo.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Tipo_vehiculo;

COPY Marca(nombre)  FROM '/Users/isabela/Marca.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Marca;

COPY Nivel_emision(tipo)  FROM '/Users/isabela/Tipo_emision.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Nivel_emision;

COPY Tipo_perfil(nombre)  FROM '/Users/isabela/Tipo_perfil.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Tipo_perfil;

INSERT INTO Tipo_tarjeta (nombre) Values ('tullave Plus');
INSERT INTO Tipo_tarjeta (nombre) Values ('tullave Basica');
Select * from Tipo_tarjeta;

COPY Tipo_servicio(nombre)  FROM '/Users/isabela/Tipo_servicio.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Tipo_servicio;

INSERT INTO Mes(nombre) Values ('FEBRERO');
Select * from Mes;

COPY Tipo_emisor(nombre,codigo)  FROM '/Users/isabela/emisor.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Tipo_emisor;

COPY Linea(nombre)  FROM '/Users/isabela/Linea1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Linea;

COPY Estacion(nombre,id_Linea)  FROM '/Users/isabela/Estaciones1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Estacion;

COPY Salidas(total,intervalo,id_Estacion,id_Mes)  FROM '/Users/isabela/Salidas1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Salidas;

COPY Tarjeta(numero_tarjeta,id_Tipo_emisor,id_Tipo_perfil,id_tipo_tarjeta )  FROM '/Users/isabela/Tarjeta2.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Tarjeta;

COPY Transaccion(saldo_antes,saldo_despues,id_Tarjeta,id_Dispositivo)  FROM '/Users/isabela/Transaccion1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Transaccion;

COPY Servicio(id_Zona,id_Tipo_servicio,id_Tipo_vehiculo,id_Accesibilidad )  FROM '/Users/isabela/Servicio1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Servicio;

COPY Vehiculo(etiqueta,matricula ,id_Concesion,modelo,id_Marca,id_Nivel_emision ,id_Zona)  FROM '/Users/isabela/Vehiculo1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Vehiculo;

COPY Pagar (id_Estacion,id_Transaccion)  FROM '/Users/isabela/Pagar2.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Pagar;



