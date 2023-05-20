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


