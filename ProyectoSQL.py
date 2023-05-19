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
