import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from Connection1 import Connection1
import ProyectoSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


# ------------------------------------------------- Graficos Barras -------------------------------------------------

# Usuarios por zona
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.usuarios_por_zona(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["zona","personas_utilizan_transporte"])
figBarCases = px.bar(dfCases.head(20),x="zona", y="personas_utilizan_transporte",color_discrete_sequence=['#dde5b6'])

# Configurar la fuente en los gráficos Usuarios por zona
figBarCases.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
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
figBarCases1 = px.bar(dfCases.head(20),x="estacion", y="personas_utilizan_transporte",color_discrete_sequence=['#dde5b6'])

# Configurar la fuente de los graficos Usuarios por estacion
figBarCases1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)


# Usuarios por tipo_perfil
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.tipo_perfil_mas_utilizado(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["perfil","total_utilizado"])
figBarCases2 = px.bar(dfCases.head(20),x="perfil", y="total_utilizado",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Usuarios por tipo de perfil 
figBarCases2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
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
figBarCases3 = px.bar(dfCases.head(20),x="nombre", y="total_salidas",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)



# ------------------------------------------------- Graficos pie -------------------------------------------------

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.generar_grafico_pie_zonas(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","zona"])
figPie1 = px.pie(dfCases, values='cantidad', names='zona', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_americas(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie2 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_NQSUR(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie3 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CALLE80(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie4 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie4.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CALLE26(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie5 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie5.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARACAS(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie6 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie6.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARRERA10(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie7 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie7.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_SUBA(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie8 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie8.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARACASSUR(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie9 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie9.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_NORTE(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie10 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie10.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

# ------------------------------------------------- Tabs Graficos de Pie -------------------------------------------------
tab2_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros por zona"),
        dcc.Graph(
            id='piechart',
            figure=figPie1,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab3_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Americas"),
        dcc.Graph(
            id='piechart',
            figure=figPie2,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab4_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros NQS Sur"),
        dcc.Graph(
            id='piechart',
            figure=figPie3,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab5_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Calle 80"),
        dcc.Graph(
            id='piechart',
            figure=figPie4,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab6_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Calle 26"),
        dcc.Graph(
            id='piechart',
            figure=figPie5,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab7_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Caracas"),
        dcc.Graph(
            id='piechart',
            figure=figPie6,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})


tab8_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Carrera 10"),
        dcc.Graph(
            id='piechart',
            figure=figPie7,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})


tab9_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Suba"),
        dcc.Graph(
            id='piechart',
            figure=figPie8,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab10_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Caracas Sur"),
        dcc.Graph(
            id='piechart',
            figure=figPie9,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})


tab11_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Norte"),
        dcc.Graph(
            id='piechart',
            figure=figPie10,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})





# ------------------------------------------------- Layout-------------------------------------------------

app.layout = html.Div(children=[
    # ------------------------------------------------- Encabezado -------------------------------------------------
    html.H1(children='Analisis Sistema de Transporte Masivo Bogota', style={'margin-left': '35px'}),
    html.H6(children='Isabela Ruiz', style={'margin-left': '35px'}),
    html.Div(style={'height': '50px'}),
    # ------------------------------------------------- Tabs Pie-------------------------------------------------
    dbc.Tabs([
        dbc.Tab(tab2_content, label="Analisis por Zona"),
        dbc.Tab(tab3_content, label="Zona Americas"),
        dbc.Tab(tab4_content, label="Zona NQS Sur"),
        dbc.Tab(tab5_content, label="Zona Calle 80"),
        dbc.Tab(tab6_content, label="Zona Calle 26"),
        dbc.Tab(tab7_content, label="Zona Caracas"),
        dbc.Tab(tab8_content, label="Zona Carrera 10"),
        dbc.Tab(tab9_content, label="Zona Suba"),
        dbc.Tab(tab10_content, label="Zona Caracas Sur"),
        dbc.Tab(tab11_content, label="Zona Norte"),
    ]),
    # ------------------------------------------------- Graficos de barras -------------------------------------------------
    # Usuarios por zona
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
    # Usuarios por estacion                            
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
    # Usuarios por perfil                            
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
    # Salidas por estacion                            
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
                        html.H3(" ¿Ques estaciones registraron mas salidas? "),
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
    # ------------------------------------------------- Tabs Grafico Lineas -------------------------------------------------                            
    
    html.Label('Color Picker'),
    dcc.Input(
        id='our-color-picker',
        type='text',
        value='#119DFF',
        style={'width': '80px'}
    ),

], style={'background': '#606c38', 'color': '#FFFFFC',})




if __name__ == '__main__':
    app.run_server(debug = True)
    
    
