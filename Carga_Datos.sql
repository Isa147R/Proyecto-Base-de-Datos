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


INSERT INTO Linea(nombre, id_Zona) VALUES ('(11) Zona K Calle 26', 6);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(12) Zona L Carrera 10', 9);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(30) Zona G NQS Sur', 2);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(31) Zona F Av. Américas', 1);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(32) Zona C Av. Suba', 10);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(33) Zona B AutoNorte', 18);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(34) Zona H Caracas Sur', 17);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(35) Zona D Calle 80', 4);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(36) Zona A Caracas', 8);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(37) Zona J Eje Ambiental', 8);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(38) Zona E NQS Central', 6);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(39) Zona F Calle 13', 8);
INSERT INTO Linea(nombre, id_Zona) VALUES ('(40) Zona T Ciudad Bolívar', 4);
SELECT * FROM Linea;

COPY Estacion(nombre,id_Linea)  FROM '/Users/isabela/Estaciones1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Estacion;

COPY Salidas(total,intervalo,id_Estacion,id_Mes)  FROM '/Users/isabela/Salidas1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Salidas;

COPY Tarjeta(numero_tarjeta,id_Tipo_emisor,id_Tipo_perfil,id_tipo_tarjeta )  FROM '/Users/isabela/Tarjeta2.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Tarjeta;

COPY Transaccion(saldo_antes,saldo_despues,id_Tarjeta,id_Dispositivo)  FROM '/Users/isabela/Transaccion1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Transaccion;

COPY Pagar (id_Estacion,id_Transaccion)  FROM '/Users/isabela/Pagar2.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Pagar;

COPY Servicio(id_Zona,id_Tipo_servicio,id_Tipo_vehiculo,id_Accesibilidad )  FROM '/Users/isabela/Servicio1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Servicio;

COPY Vehiculo(etiqueta,matricula ,id_Concesion,modelo,id_Marca,id_Nivel_emision ,id_Zona)  FROM '/Users/isabela/Vehiculo1.csv' WITH DELIMITER ';' CSV HEADER;
Select * from Vehiculo;



