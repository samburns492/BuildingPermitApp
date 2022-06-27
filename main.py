# Author: Sam Burns
# Plotly dash application that uses two large datasets "bp_scrubbed.csv" and "sf_data.csv" in addition to
# pandas and plotly.express libraries to create an interactive dashboard application that can
# displays information regarding housing data and building permits in the city and county of San Francisco.
# The data can be filtered by the year.

import dash_auth
import plotly.express as px
import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


VALID_USERNAME_PASSWORD_PAIRS = {
    'username': 'password'
}

app = dash.Dash(__name__)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
server = app.server

plot = px.bar()
plot2 = px.bar()

bp = pd.DataFrame()
sf = pd.DataFrame()

bp = pd.read_csv("bp_scrubbed.csv")
sf = pd.read_csv("sf_data.csv")

group_year = bp.groupby('Filed Year')
group_wait = bp.groupby('Wait Time')

groupy_stats = group_year.describe()['Wait Time']
groupy_stats = groupy_stats.drop(index=[1901, 1908, 1909, 1929, 1949, 1968])
groupp_stats = group_year.describe()['Permit Type']
groupp_stats = groupp_stats.drop(index=[1901, 1908, 1909, 1929, 1949, 1968])

plot = px.bar(groupy_stats, x=groupy_stats.index, y=('mean'), title="Mean Wait Time for Permit Issuance by Year")

plot2 = px.bar(groupy_stats, x=groupp_stats.index, y=('count'), title="Number of Permits by Year")

plot.update_layout(xaxis_title="Year", yaxis_title="Mean Wait Time (Days)")
plot2.update_layout(xaxis_title="Year", yaxis_title="Permit Count")

app.layout = html.Div([

    html.H1("Cranes & More Construction Dashboard", style={'text-align': 'center'}),

    dcc.Dropdown(id="select_y",
                 options=[
                     {"label": "1970", "value": 1970},
                     {"label": "1971", "value": 1971},
                     {"label": "1972", "value": 1972},
                     {"label": "1973", "value": 1973},
                     {"label": "1974", "value": 1974},
                     {"label": "1975", "value": 1975},
                     {"label": "1976", "value": 1976},
                     {"label": "1977", "value": 1977},
                     {"label": "1978", "value": 1978},
                     {"label": "1979", "value": 1979},
                     {"label": "1980", "value": 1980},
                     {"label": "1981", "value": 1981},
                     {"label": "1982", "value": 1982},
                     {"label": "1983", "value": 1983},
                     {"label": "1984", "value": 1984},
                     {"label": "1985", "value": 1985},
                     {"label": "1986", "value": 1986},
                     {"label": "1987", "value": 1987},
                     {"label": "1988", "value": 1988},
                     {"label": "1989", "value": 1989},
                     {"label": "1990", "value": 1990},
                     {"label": "1991", "value": 1991},
                     {"label": "1992", "value": 1992},
                     {"label": "1993", "value": 1993},
                     {"label": "1994", "value": 1994},
                     {"label": "1995", "value": 1995},
                     {"label": "1996", "value": 1996},
                     {"label": "1997", "value": 1997},
                     {"label": "1998", "value": 1998},
                     {"label": "1999", "value": 1999},
                     {"label": "2000", "value": 2000},
                     {"label": "2001", "value": 2001},
                     {"label": "2002", "value": 2002},
                     {"label": "2003", "value": 2003},
                     {"label": "2004", "value": 2004},
                     {"label": "2005", "value": 2005},
                     {"label": "2006", "value": 2006},
                     {"label": "2007", "value": 2007},
                     {"label": "2008", "value": 2008},
                     {"label": "2009", "value": 2009},
                     {"label": "2010", "value": 2010},
                     {"label": "2011", "value": 2011},
                     {"label": "2012", "value": 2012},
                     {"label": "2013", "value": 2013},
                     {"label": "2014", "value": 2014},
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021}],
                 multi=False,
                 value=2021,
                 style={'width': "40%"}
                 ),
    html.Div(id='output_container'),
    dcc.Graph(id='plot', figure=plot),
    dcc.Graph(id='plot2', figure=plot2),
    html.Br(),
    dcc.Graph(id='my_map')

])


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_map', component_property='figure')],
    [Input(component_id='select_y', component_property='value')]
)

#function to update the plotly dash app with the selected year

def update_graph(option_slctd):
    if option_slctd is None:
        print("sad")
    else:

        print(option_slctd)
        print(type(option_slctd))

        container = "The year chosen by user was: {}".format(option_slctd)

        long = []
        lat = []

        dfy = bp[bp['Filed Year'] == option_slctd]

        for x in range(len(dfy)):
            loc = str(dfy['Location'].iloc[x])

            ind1 = loc.find(".")
            ind2 = loc.find(".", 20, 42)
            z = loc[ind1 - 4:ind1 + 5]
            y = loc[ind2 - 2:ind2 + 5]

            if z and y != '':
                long.append(float(z))
                lat.append(float(y))
            else:
                long.append('nan')
                lat.append('nan')

        while ('nan' in long):
            long.remove('nan')

        while ('nan' in lat):
            lat.remove('nan')

        frame = {'longitude': long, 'latitude': lat}

        df_coor = pd.DataFrame(frame)

        zvals = [df_coor['longitude'], df_coor['latitude']]

        fig = px.scatter_mapbox(df_coor, lat=zvals[1], lon=zvals[0],
                                title="Location of Building Permits for Year: {}".format(option_slctd),
                                mapbox_style='open-street-map', height=1000, zoom=12)

        return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)
