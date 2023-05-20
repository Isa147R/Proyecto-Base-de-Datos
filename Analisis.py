import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection1 import Connection1
import ProyectoSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

# Usuarios por zona

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.usuarios_por_zona(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["zona","personas_utilizan_transporte"])
figBarCases = px.bar(dfCases.head(20),x="zona", y="personas_utilizan_transporte",color_discrete_sequence=['#0B1F2A'])

# Configurar la fuente en los gráficos
figBarCases.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#11414E',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

# Usuarios por estacion

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.usuarios_por_estacion(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["estacion","personas_utilizan_transporte"])
figBarCases1 = px.bar(dfCases.head(20),x="estacion", y="personas_utilizan_transporte",color_discrete_sequence=['#0B1F2A'])

figBarCases1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#11414E',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)


# usuarios por tipo_perfil

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.tipo_perfil_mas_utilizado(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["perfil","total_utilizado"])
figBarCases2 = px.bar(dfCases.head(20),x="perfil", y="total_utilizado",color_discrete_sequence=['#0B1F2A'])

figBarCases2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#11414E',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

# salidas por estaciones

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_por_estacion(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["nombre","total_salidas"])
figBarCases3 = px.bar(dfCases.head(20),x="nombre", y="total_salidas",color_discrete_sequence=['#0B1F2A'])

figBarCases3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#11414E',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#Layout

app.layout = html.Div(children=[
    
    html.H1(children='Analisis Sistema de Transporte Masivo Bogota', style={'margin-left': '35px'}),
    html.H6(children='Isabela Ruiz', style={'margin-left': '35px'}),
    html.Div(style={'height': '50px'}),
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Usuarios por zona", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='barusuarios_por_zona',
                            figure=figBarCases,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Cuántas personas utilizan el transporte público en una zona en particular? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT z.nombre AS zona, SUM(s.total) AS personas_utilizan_transporte
                        FROM Salidas s
                        JOIN Estacion e ON s.id_Estacion = e.id
                        JOIN Linea l ON e.id_Linea = l.id
                        JOIN Zona z ON l.id_Zona = z.id
                        JOIN Mes m ON s.id_Mes = m.id
                        WHERE m.id = 1
                        GROUP BY zona
                        ORDER BY personas_utilizan_transporte DESC;"""),                        
                    ]
                )
            ]
        ),
    html.Div(style={'height': '50px'}),                            
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Usuarios por estacion", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='barusuarios_por_estacion',
                            figure=figBarCases1,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Cuántas personas utilizan el transporte público por estacion? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT e.nombre AS estacion, SUM(s.total) AS personas_utilizan_transporte
                        FROM Salidas s
                        JOIN Estacion e ON s.id_Estacion = e.id
                        JOIN Mes m ON s.id_Mes = m.id
                        WHERE m.id = 1
                        GROUP BY e.nombre
                        ORDER BY personas_utilizan_transporte DESC; """),                        
                    ]
                )
            ]
        ),
    html.Div(style={'height': '50px'}),
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Perfil mas utilizado", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='bartipo_perfil_mas_utilizado',
                            figure=figBarCases2,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Cual es el perfil de tarjeta mas utilizado? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT tp.nombre AS perfil, COUNT(*) AS total_utilizado
                        FROM Tarjeta t
                        JOIN Tipo_perfil tp ON t.id_Tipo_perfil = tp.id
                        GROUP BY tp.nombre
                        ORDER BY total_utilizado DESC; """),                        
                    ]
                )
            ]
        ),
    html.Div(style={'height': '50px'}),
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Salidas por estacion", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='barsalidas_por_estacion',
                            figure=figBarCases3,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Que estaciones registraron mas salidas? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT Estacion.nombre, SUM(Salidas.total) AS total_salidas
                        FROM Salidas
                        JOIN Estacion ON Salidas.id_Estacion = Estacion.id
                        JOIN Mes ON Salidas.id_Mes = Mes.id
                        WHERE Mes.id=1
                        GROUP BY Estacion.nombre
                        ORDER BY total_salidas DESC
                        LIMIT 5; """),                        
                    ]
                )
            ]
        ),                            
    html.Label('Color Picker'),
    dcc.Input(
        id='our-color-picker',
        type='text',
        value='#119DFF',
        style={'width': '80px'}
    ),

], style={'background': '#153243', 'color': '#FFFFFC',})


if __name__ == '__main__':
    app.run_server(debug = True)
    
    
