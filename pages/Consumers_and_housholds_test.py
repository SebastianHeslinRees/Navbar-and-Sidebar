import dash

dash.register_page(__name__)

from dash import html
import os
import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import json
import urllib
#from .side_bar import sidebar

np.random.seed(2020)

def data_pull(IdList, period="quarters", dataset="", redate=False):
    """ This will collect all the monthly data related to the input serial IDs from the ONS website, and put them into a pandas dataframe"""
    dataDict = {}
    for Id in IdList:
        try:
            with urllib.request.urlopen(fr"https://api.ons.gov.uk/dataset/{dataset}/timeseries/{Id}/data") as url:
                dataDict[Id] = json.loads(url.read())[period]
        except:
            with urllib.request.urlopen(fr"https://api.ons.gov.uk/dataset/pn2/timeseries/{Id}/data") as url:
                dataDict[Id] = json.loads(url.read())[period]

    # Here, we filter the data down to just the monthly value and the date, setting the date as the index.
    DfDict = {}
    for Id, List in dataDict.items():
        DfDict[Id] = pd.DataFrame(List)[["date", "value"]].set_index("date")

    # This concatenates the dataframes into a single dataframe, removes unnecessary columns, and changes the dtypes to numeric.
    collated = pd.concat(DfDict, axis=1).apply(pd.to_numeric)
    collated.columns = collated.columns.droplevel(1)
    if redate == True: collated.index = pd.to_datetime(collated.index).strftime(
        dateFormat)  # pd.to_datetime(pd.to_datetime(collated.index).strftime("%Y-%m-%d %H:%M:%S"))
    return collated


cpi = data_pull(["L55O"], dataset="MM23")


corporate_colors = {
    'dark-blue-grey' : 'rgb(62, 64, 76)',
    'medium-blue-grey' : 'rgb(77, 79, 91)',
    'medium-blue' : 'rgb(27,167,201)',
    'superdark-green' : 'rgb(41, 56, 55)',
  #  'dark-green' : 'rgb(57, 81, 85)',
  #light-grey
    'light-grey' : 'rgb(240,240,240)',
    'medium-green' : 'rgb(51, 153, 102)',
    'black' : 'rgb(0,0,0)',
    'pink-red' : 'rgb(255, 101, 131)',
    'dark-pink-red' : 'rgb(247, 80, 99)',
    'burnt-orange':'rgb(222,139,9)',
    'white' : 'rgb(251, 251, 252)',
#'light-green' : 'rgb(208, 206, 206)',
    'red':'rgb(200, 0, 0)',
    'dark-red': 'rgb(88, 0, 0)'
}
externalgraph_rowstyling = {
    'margin-left' : '15px',
    'margin-right' : '15px'
}

externalgraph_colstyling = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['superdark-green'],
    'background-color' : corporate_colors['superdark-green'],
    'box-shadow' : '0px 0px 17px 0px rgba(186, 218, 212, .5)',
    'padding-top' : '10px'
}

filterdiv_borderstyling = {
    'border-radius' : '0px 0px 10px 10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['dark-red'],
    'background-color' : corporate_colors['dark-red'],
    'box-shadow' : '2px 5px 5px 1px rgba(255, 101, 131, .5)'
    }

filterdiv_borderstyling2 = {
    'border-radius' : '0px 0px 10px 10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['light-grey'],
    'background-color' : corporate_colors['light-grey'],
    'box-shadow' : '2px 5px 5px 1px rgba(255, 101, 131, .5)'
    }

navbarcurrentpage = {
    'text-decoration' : 'underline',
    'text-decoration-color' : corporate_colors['pink-red'],
    'text-shadow': '0px 0px 1px rgb(251, 251, 252)'
    }

recapdiv = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : 'rgb(251, 251, 252, 0.1)',
    'margin-left' : '15px',
    'margin-right' : '15px',
    'margin-top' : '15px',
    'margin-bottom' : '15px',
    'padding-top' : '5px',
    'padding-bottom' : '5px',
    'background-color' : 'rgb(251, 251, 252, 0.1)'
    }

recapdiv_text = {
    'text-align' : 'left',
    'font-weight' : '350',
    'color' : corporate_colors['white'],
    'font-size' : '1.5rem',
    'letter-spacing' : '0.04em'
    }

##################### Corporate chart formatting

corporate_title = {
    'font' : {
        'size' : 16,
        'color' : corporate_colors['white']}
}

corporate_xaxis = {
    'showgrid' : False,
    'linecolor' : corporate_colors['black'],
    'color' : corporate_colors['black'],
    'titlefont' : {
        'size' : 20,
        'color' : corporate_colors['black']},
    'tickfont' : {
        'size' : 11,
        'color' : corporate_colors['black']},
    'zeroline': False
}

corporate_yaxis = {
    'showgrid' : True,
    'color' : corporate_colors['light-grey'],
    'gridwidth' : 0.5,
    'gridcolor' : corporate_colors['black'],
    'linecolor' : corporate_colors['light-grey'],
    'titlefont' : {
        'size' : 20,
        'color' : corporate_colors['black']},
    'tickfont' : {
        'size' : 11,
        'color' : corporate_colors['black']},
    'zeroline': False
}

corporate_font_family = 'Dosis'

corporate_legend = {
    'orientation' : 'h',
    'yanchor' : 'bottom',
    'y' : 1.01,
    'xanchor' : 'right',
    'x' : 1.05,
	'font' : {'size' : 9, 'color' : corporate_colors['black']}
} # Legend will be on the top right, above the graph, horizontally

corporate_margins = {'l' : 5, 'r' : 5, 't' : 45, 'b' : 15}  # Set top margin to in case there is a legend

corporate_layout = go.Layout(
    font = {'family' : corporate_font_family},
    title = corporate_title,
    title_x = 0.5, # Align chart title to center
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = corporate_xaxis,
    yaxis = corporate_yaxis,
    height = 270,
    legend = corporate_legend,
    margin = corporate_margins
    )


def get_header():
    header = html.Div([
        html.Div([], className='col-2'),  # Same as img width, allowing to have the title centrally aligned

        html.Div([
            html.Img(
                src=app.get_asset_url('logo_001c.png'),
                height='43 px',
                width='auto')
        ],
            className='col-2',
            style={
                'align-items': 'center',
                'padding-top': '1%',
                'height': 'auto'})
    ],
        className='row',
        style={'height': '4%',
               'background-color': corporate_colors['superdark-green']}
    )
    return header

fig = go.Figure()

cpi = cpi.reset_index()

fig.add_trace(
    go.Scatter(
        name='Consumer price inflation rate',
        x=cpi["date"],
        y=cpi["L55O"],
        mode='lines',
        marker=dict(color="red"),
        line=dict(width=4),
        showlegend=True))

fig.update_layout(height=750, barmode='overlay',
margin=dict(l=20, r=20, t=20, b=70),
#title = "GDP estimates",
font = {
'size' : 16,
'color' : corporate_colors['black']},
xaxis_title = "Quarter",
yaxis_title = "Percentage",
legend_title ="Please Click to Select Trace(s):",
title_y= 0.98,
paper_bgcolor = 'rgba(0,0,0,0)',
plot_bgcolor = 'rgba(0,0,0,0)',
xaxis = corporate_xaxis,
yaxis = corporate_yaxis,
legend_font_family =  'sans-serif',
legend_font_color = corporate_colors['black'],
legend_font_size = 10)

LOGO = 'https://publicappointments.cabinetoffice.gov.uk/wp-content/uploads/2018/02/HMT-logo.png'

# styling the sidebar
# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 140,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "4rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
'''sidebar = navbar2 = html.Div(
    [
        html.H2("Consumer and household", className="display-4"),
        html.Hr(),
        html.P(
            "Select page", className="lead"
        ),
        dbc.Nav([
                dbc.NavLink(
                    [
                        html.Div(page["GDP"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        ),
    ],
    style=SIDEBAR_STYLE)'''

navbar2 = html.Div(
    [
        html.H2("Consumer and household", className="display-4"),
        html.Hr(),
        html.P(
            "Select page", className="lead"
        ),
        dbc.Nav([
                dbc.NavLink(
                    [
                        dbc.NavLink("Consumer and household Home", href="/", active="exact"),
                        dbc.NavLink("Consumer and household Graph 1", href="/page-1", active="exact"),
                        dbc.NavLink("Consumer and household Graph 2", href="/page-2", active="exact"),
                    ])
        ],
            vertical=True,
            pills=True,
            className="bg-light",
        ),
    ],
    style=SIDEBAR_STYLE,)

def layout():
    return html.Div([

        html.Div([navbar2]),

        #html.Div([sidebar(),]),

        html.Div([

            html.Div([
                html.H1(children='HMT Consumer and Household homepage',
                        style={'color': corporate_colors['light-grey'], 'textAlign': 'center',
                               'font-family': 'sans-serif', 'fontSize': 40})

        ], style=filterdiv_borderstyling),

        html.H1(children='Welcome to the consumer and household homepage!',
                        style={'textAlign': 'center',
                               'font-family': 'sans-serif', 'fontSize': 40}),

        #dcc.Graph(figure=fig, style={'padding-top': '0.5%',
         #                            'padding-right': '10rem'}),

        html.H6("Based on data from ",
        style={'color': corporate_colors['black'], 'font-family': 'sans-serif'}),
#       html.H6("Please be aware that counts below 100 may not be an accurate representation of the population",
#           style={'color' : corporate_colors['black'], 'font-family' : 'sans-serif'}),


        ], style = {'background-color': corporate_colors['light-grey'],
        'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'})])

