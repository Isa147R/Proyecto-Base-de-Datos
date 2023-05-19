import ProyectoSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

# Usuarios por zona

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.usuarios_por_zona(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["zona","personas_utilizan_transporte"])
figBarCases = px.bar(dfCases.head(20),x="zona", y="personas_utilizan_transporte")

# Usuarios por estacion

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.usuarios_por_estacion(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["estacion","personas_utilizan_transporte"])
figBarCases1 = px.bar(dfCases.head(20),x="estacion", y="personas_utilizan_transporte")

# usuarios por tipo_perfil

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.tipo_perfil_mas_utilizado(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["perfil","total_utilizado"])
figBarCases2 = px.bar(dfCases.head(20),x="perfil", y="total_utilizado")


#Layout

app.layout = html.Div(children = [
    html.H1(children = 'Covid 19 Dashboard'),
    html.H2(children = 'Covid 19 Dashboard'),
    dcc.Graph(
        id = 'barCasesByCountry',
        figure = figBarCases
        ),
    dcc.Graph(
        id = 'barCasesByCountry',
        figure = figBarCases1
        ),
    dcc.Graph(
        id = 'barCasesByCountry',
        figure = figBarCases2
        ),
    ])

if __name__ == '__main__':
    app.run_server(debug = True)
