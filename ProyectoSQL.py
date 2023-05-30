def usuarios_por_zona():
    return """ SELECT z.nombre AS zona, SUM(s.total) AS personas_utilizan_transporte
                FROM Salidas s
                JOIN Estacion e ON s.id_Estacion = e.id
                JOIN Linea l ON e.id_Linea = l.id
                JOIN Zona z ON l.id_Zona = z.id
                JOIN Mes m ON s.id_Mes = m.id
                WHERE m.id = 1
                GROUP BY zona
                ORDER BY personas_utilizan_transporte DESC;"""

def usuarios_por_estacion():
    return """ SELECT e.nombre AS estacion, SUM(s.total) AS personas_utilizan_transporte
                FROM Salidas s
                JOIN Estacion e ON s.id_Estacion = e.id
                JOIN Mes m ON s.id_Mes = m.id
                WHERE m.id = 1
                GROUP BY e.nombre
                ORDER BY personas_utilizan_transporte DESC; """
                
                
def tipo_perfil_mas_utilizado():
    return """ SELECT tp.nombre AS perfil, COUNT(*) AS total_utilizado
                FROM Tarjeta t
                JOIN Tipo_perfil tp ON t.id_Tipo_perfil = tp.id
                GROUP BY tp.nombre
                ORDER BY total_utilizado DESC; """

def salidas_por_estacion():
    return """SELECT Estacion.nombre, SUM(Salidas.total) AS total_salidas
              FROM Salidas
              JOIN Estacion ON Salidas.id_Estacion = Estacion.id
              JOIN Mes ON Salidas.id_Mes = Mes.id
              WHERE Mes.id=1
              GROUP BY Estacion.nombre
              ORDER BY total_salidas DESC
              LIMIT 5; """

def salidas_hora_pico_3_8():
    return """SELECT id_Estacion, SUM(total) AS total_salidas
                FROM Salidas
                WHERE intervalo >= '15:00:00' AND intervalo <= '20:00:00'
                GROUP BY id_Estacion
                ORDER BY total_salidas DESC
                Limit 10; """             
def generar_grafico_pie_zonas():
    return """SELECT z.nombre AS zona, COUNT(*) AS cantidad
               FROM Zona z
               JOIN Linea l ON z.id = l.id_Zona
               JOIN Estacion e ON l.id = e.id_Linea
               JOIN Salidas s ON e.id = s.id_Estacion
               GROUP BY z.nombre;"""
        
def registros_por_servicio():
    return """ SELECT ts.nombre AS tipo_servicio, COUNT(*) AS cantidad
                FROM Tipo_servicio ts
                JOIN Servicio se ON ts.id = se.id_Tipo_servicio
                GROUP BY ts.nombre; """

def salidas_americas():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                FROM Zona z
                JOIN Linea l ON z.id = l.id_Zona
                JOIN Estacion e ON l.id = e.id_Linea
                LEFT JOIN Salidas s ON e.id = s.id_Estacion
                WHERE z.id = 1
                GROUP BY z.id, z.nombre, e.id, e.nombre;"""

def salidas_NQSUR():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                FROM Zona z
                JOIN Linea l ON z.id = l.id_Zona
                JOIN Estacion e ON l.id = e.id_Linea
                LEFT JOIN Salidas s ON e.id = s.id_Estacion
                WHERE z.id = 2
                GROUP BY z.id, z.nombre, e.id, e.nombre;"""
                
def salidas_CALLE80():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                FROM Zona z
                JOIN Linea l ON z.id = l.id_Zona
                JOIN Estacion e ON l.id = e.id_Linea
                LEFT JOIN Salidas s ON e.id = s.id_Estacion
                WHERE z.id = 4
                GROUP BY z.id, z.nombre, e.id, e.nombre;"""
                
def salidas_CALLE26():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                 FROM Zona z
                 JOIN Linea l ON z.id = l.id_Zona
                 JOIN Estacion e ON l.id = e.id_Linea
                 LEFT JOIN Salidas s ON e.id = s.id_Estacion
                 WHERE z.id = 6
                 GROUP BY z.id, z.nombre, e.id, e.nombre;"""               

def salidas_CARACAS():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                 FROM Zona z
                 JOIN Linea l ON z.id = l.id_Zona
                 JOIN Estacion e ON l.id = e.id_Linea
                 LEFT JOIN Salidas s ON e.id = s.id_Estacion
                 WHERE z.id = 8
                 GROUP BY z.id, z.nombre, e.id, e.nombre;"""      
                 
def salidas_CARRERA10():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                 FROM Zona z
                 JOIN Linea l ON z.id = l.id_Zona
                 JOIN Estacion e ON l.id = e.id_Linea
                 LEFT JOIN Salidas s ON e.id = s.id_Estacion
                 WHERE z.id = 9
                 GROUP BY z.id, z.nombre, e.id, e.nombre;"""    

def salidas_SUBA():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                 FROM Zona z
                 JOIN Linea l ON z.id = l.id_Zona
                 JOIN Estacion e ON l.id = e.id_Linea
                 LEFT JOIN Salidas s ON e.id = s.id_Estacion
                 WHERE z.id = 10
                 GROUP BY z.id, z.nombre, e.id, e.nombre;""" 
                 
def salidas_CARACASSUR():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                 FROM Zona z
                 JOIN Linea l ON z.id = l.id_Zona
                 JOIN Estacion e ON l.id = e.id_Linea
                 LEFT JOIN Salidas s ON e.id = s.id_Estacion
                 WHERE z.id = 17
                 GROUP BY z.id, z.nombre, e.id, e.nombre;"""     
                 
def salidas_NORTE():
    return """SELECT e.nombre AS estacion, COUNT(s.id) AS cantidad
                 FROM Zona z
                 JOIN Linea l ON z.id = l.id_Zona
                 JOIN Estacion e ON l.id = e.id_Linea
                 LEFT JOIN Salidas s ON e.id = s.id_Estacion
                 WHERE z.id = 18
                 GROUP BY z.id, z.nombre, e.id, e.nombre;"""   

def tipo_emision():
   return  """SELECT Zona.nombre AS nombre, COUNT(*) AS vehiculos
            FROM Vehiculo
            JOIN Nivel_emision ON Vehiculo.id_Nivel_emision = Nivel_emision.id
            JOIN Zona ON Vehiculo.id_Zona = Zona.id
            GROUP BY Zona.nombre, Nivel_emision.tipo;
            """

def  emision_BOSA():
    return """SELECT ne.tipo AS nivel_emision, COUNT(*) AS total_vehiculos
                FROM Vehiculo v
                INNER JOIN Nivel_emision ne ON v.id_Nivel_emision = ne.id
                INNER JOIN Zona z ON v.id_Zona = z.id
                WHERE z.id = 2
                GROUP BY ne.tipo;"""

def mas_y_menos():
    return """SELECT estacion_mas_salidas.estacion, estacion_mas_salidas.total_salidas
                FROM (
                    SELECT e.nombre AS estacion, COUNT(s.id) AS total_salidas
                    FROM Estacion e
                    JOIN Salidas s ON e.id = s.id_Estacion
                    GROUP BY e.nombre
                    ORDER BY total_salidas DESC
                    LIMIT 1
                ) AS estacion_mas_salidas
                
                UNION ALL
                
                SELECT estacion_menos_salidas.estacion, estacion_menos_salidas.total_salidas
                FROM (
                    SELECT e.nombre AS estacion, COUNT(s.id) AS total_salidas
                    FROM Estacion e
                    JOIN Salidas s ON e.id = s.id_Estacion
                    GROUP BY e.nombre
                    ORDER BY total_salidas ASC
                    LIMIT 1
                ) AS estacion_menos_salidas;
                
                """
                
def hora_americas():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 1
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""
                
def hora_bosa():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 2
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""

def hora_80():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 3
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""                      

def hora_bolivar():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 4
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""   

def hora_engativa():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 5
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""     

                
def hora_fontibon():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 6
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""
                
def hora_kennedy():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 7
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""

def hora_perdomo():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 8
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""                      

def hora_cristobal():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 9
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""   

def hora_suba():
    return """SELECT AHZ.hora_del_dia, AHZ.cantidad_transacciones
                FROM Zona Z
                JOIN (
                    SELECT E.id_Linea, DATE_PART('hour', S.intervalo) AS hora_del_dia, SUM(S.total) AS cantidad_transacciones
                    FROM Salidas S
                    INNER JOIN Estacion E ON E.id = S.id_Estacion
                    GROUP BY E.id_Linea, hora_del_dia
                ) AHZ ON Z.id = AHZ.id_Linea
                Where id = 10
                ORDER BY Z.nombre, AHZ.hora_del_dia;"""       
