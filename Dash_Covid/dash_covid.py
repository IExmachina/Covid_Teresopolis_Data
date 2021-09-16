
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the covid teresopolis data into pandas dataframe

df_tere = pd.read_csv('SQL_COVID_DATA.csv')
df_rj = pd.read_csv('Rj_dados_clean.csv')
df_tere['Semanas_Epidemológicas'] = df_tere['Semanas_Epidemológicas'].astype(str)
# Pie fig
rj_plot = df_rj.groupby('CIDADE')['NOVAS_MORTES'].sum().reset_index()
rj_plot = rj_plot.sort_values(by=['NOVAS_MORTES'], ascending=False)
pie_fig = px.pie(rj_plot.head(10), values='NOVAS_MORTES', names='CIDADE', title='Mortes por Cidade')

# Line fig
line_fig = px.line(df_tere.tail(8), y="Numero_mortes", x="Semanas_Epidemológicas",title='Novas Mortes: Semana 28 de 2021 a semana 35 de 2021 (Julho - Setembro)')

# bar fig
bar_fig = px.bar(df_tere.tail(8), y="Numero_novos_casos", x="Semanas_Epidemológicas",title='Novos casos: Semana 28 de 2021 a semana 35 de 2021 (Julho - Setembro)')

# Scatter fig 1
scatter_fig1 = px.scatter(df_tere, x="Semanas_Epidemológicas", y="Índice_mortalidade",
                         title='Índice de mortalidade: De Abril de 2020 a Setembro de 2021',
                         color='Índice_mortalidade')

# Scatter fig 2

scatter_fig2 = px.scatter(df_tere, x="Semanas_Epidemológicas", y="Numero_mortes",
                          title='Novas Mortes: De Abril de 2020 a Setembro de 2021', color='Numero_mortes')

# Create a dash application
app = dash.Dash(__name__)
server = app.server
# Create an app layout
app.layout = html.Div(children=[html.H1('COVID Teresópolis',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites



                                       # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                       # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                       html.Div(dcc.Graph(figure=pie_fig)),
                                       html.Br(),

                                       html.P("Gráficos Temporais", style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 20}),
                                       html.Br(),

                                       # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                       html.Div([
                                           html.Div(dcc.Graph(figure=line_fig)),
                                           html.Div(dcc.Graph(figure=bar_fig))

                                       ],style={'display': 'flex'}),
                                       # Segment 2
                                       html.Div([
                                           html.Div(dcc.Graph(figure=scatter_fig1)),
                                           html.Div(dcc.Graph(figure=scatter_fig2))
                                       ], style={'display': 'flex'})
                                       ])

                               # TASK 2:
                               # Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
                               # Callback decorator

#@app.callback([Output(component_id='pie_chart', component_property='figure'),
 #                Output(component_id='line_plot', component_property='figure'),
  #               Output(component_id='bar_plot', component_property='figure'),
   #              Output(component_id='scatter_plot1', component_property='figure'),
    #             Output(component_id='scatter_plot2', component_property='figure')])

# Computation to callback function and return graph


#def get_pie(pie_chart):
     #rj_plot = df_rj.groupby('CIDADE')['NOVAS_MORTES'].sum().reset_index()
     #rj_plot = rj_plot.sort_values(by=['NOVAS_MORTES'], ascending=False)
     #pie_fig = px.pie(rj_plot.head(10), values='NOVAS_MORTES', names='CIDADE', title='Mortes por Cidade')
     #return pie_fig


#def get_line(line_plot):
     #line_fig = px.line(df_tere.tail(8).astype(str), y="Numero_mortes", x="Semanas_Epidemológicas",title='Novas Mortes: Semana 28 de 2021 a semana 35 de 2021 (Julho - Setembro)')
     #return line_fig


#def get_bar(bar_plot):
    #bar_fig = px.bar(df_tere.tail(8).astype(str), y="Numero_novos_casos", x="Semanas_Epidemológicas",title='Novos casos: Semana 28 de 2021 a semana 35 de 2021 (Julho - Setembro)')
    #return bar_fig


#def get_scatter1(scatter_plot1):
    #scatter_fig1 = px.scatter(df_tere, x="Semanas_Epidemológicas", y="Índice_mortalidade",
     #                     title='Índice de mortalidade: De Abril de 2020 a Setembro de 2021',
      #                    color='Índice_mortalidade')
    #return scatter_fig1


#def get_scatter2(scatter_plot2):
    #scatter_fig2 = px.scatter(df_tere, x="Semanas_Epidemológicas", y="Numero_mortes",
    #                      title='Novas Mortes: De Abril de 2020 a Setembro de 2021', color='Numero_mortes')
    #return scatter_fig2


# Run the app
if __name__ == '__main__':
    app.run_server()