import dash

dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

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

header = html.H3('Page 2!')

#make dummy gdp data

gdp_array = np.array(
    [['1992 Q1', -0.6],
       ['1992 Q2', -0.1],
       ['1992 Q3', 0.0],
       ['1992 Q4', 0.2],
       ['1993 Q1', 0.3],
       ['1993 Q2', 0.5],
       ['1993 Q3', 0.6],
       ['1993 Q4', 0.8],
       ['1994 Q1', 0.7],
       ['1994 Q2', 1.0],
       ['1994 Q3', 0.9],
       ['1994 Q4', 0.8],
       ['1995 Q1', 0.7],
       ['1995 Q2', 0.5],
       ['1995 Q3', 0.4],
       ['1995 Q4', 0.5],
       ['1996 Q1', 0.4],
       ['1996 Q2', 0.4],
       ['1996 Q3', 0.8],
       ['1996 Q4', 0.8],
       ['1997 Q1', 0.9],
       ['1997 Q2', 0.9],
       ['1997 Q3', 0.9],
       ['1997 Q4', 0.4],
       ['1998 Q1', 0.5],
       ['1998 Q2', 0.5],
       ['1998 Q3', 0.4],
       ['1998 Q4', 0.2],
       ['1999 Q1', 0.0],
       ['1999 Q2', 0.5],
       ['1999 Q3', 0.9],
       ['1999 Q4', 0.8],
       ['2000 Q1', 0.5],
       ['2000 Q2', 0.9],
       ['2000 Q3', 0.7],
       ['2000 Q4', 0.3],
       ['2001 Q1', 0.4],
       ['2001 Q2', 0.3],
       ['2001 Q3', 0.5],
       ['2001 Q4', 0.0],
       ['2002 Q1', 0.0],
       ['2002 Q2', 0.6],
       ['2002 Q3', 0.8],
       ['2002 Q4', 0.4],
       ['2003 Q1', 0.2],
       ['2003 Q2', 0.3],
       ['2003 Q3', 0.7],
       ['2003 Q4', 0.9],
       ['2004 Q1', 0.6],
       ['2004 Q2', 0.9],
       ['2004 Q3', 0.4],
       ['2004 Q4', 0.7],
       ['2005 Q1', 0.5],
       ['2005 Q2', 0.5],
       ['2005 Q3', 0.4],
       ['2005 Q4', 0.6],
       ['2006 Q1', 0.6],
       ['2006 Q2', 0.8],
       ['2006 Q3', 0.7],
       ['2006 Q4', 0.8],
       ['2007 Q1', 0.7],
       ['2007 Q2', 0.8],
       ['2007 Q3', 0.7],
       ['2007 Q4', 0.6],
       ['2008 Q1', 0.4],
       ['2008 Q2', 0.0],
       ['2008 Q3', -0.5],
       ['2008 Q4', -1.5],
       ['2009 Q1', -1.9],
       ['2009 Q2', -0.7],
       ['2009 Q3', -0.3],
       ['2009 Q4', 0.3],
       ['2010 Q1', 0.3],
       ['2010 Q2', 1.2],
       ['2010 Q3', 0.8],
       ['2010 Q4', -0.6],
       ['2011 Q1', 0.5],
       ['2011 Q2', 0.2],
       ['2011 Q3', 0.5],
       ['2011 Q4', -0.2],
       ['2012 Q1', -0.3],
       ['2012 Q2', -0.5],
       ['2012 Q3', 1.0],
       ['2012 Q4', -0.3],
       ['2013 Q1', 0.3],
       ['2013 Q2', 0.7],
       ['2013 Q3', 0.8],
       ['2013 Q4', 0.7],
       ['2014 Q1', 0.8],
       ['2014 Q2', 0.8],
       ['2014 Q3', 0.7],
       ['2014 Q4', 0.5],
       ['2015 Q1', 0.3],
       ['2015 Q2', 0.7],
       ['2015 Q3', 0.5],
       ['2015 Q4', 0.5],
       ['2016 Q1', 0.4],
       ['2016 Q2', 0.6],
       ['2016 Q3', 0.5],
       ['2016 Q4', 0.7],
       ['2017 Q1', 0.2],
       ['2017 Q2', 0.3],
       ['2017 Q3', 0.4],
       ['2017 Q4', 0.4],
       ['2018 Q1', 0.1],
       ['2018 Q2', 0.4],
       ['2018 Q3', 0.6],
       ['2018 Q4', 0.2],
       ['2019 Q1', 0.5],
       ['2019 Q2', -0.2],
       ['2019 Q3', 0.3],
       ['2019 Q4', 0.0],
       ['2020 Q1', -2.0],
       ['2020 Q2', -20.4],
       ['2020 Q3', 15.5],
       ['2020 Q4', 1.0],
       ['2021 Q1', -1.5],
       ['2021 Q2', 4.8],
       ['2021 Q3', 1.3],
       ['2021 Q4', 1.0]])

gdp = pd.DataFrame(gdp_array,
             columns=['Relating to Period',
                      'First Estimate of quarterly GDP (Month 2 delay estimate)'])

gdp['First Estimate of quarterly GDP (Month 2 delay estimate)'] = gdp['First Estimate of quarterly GDP (Month 2 delay estimate)'].astype(float)

#add fake column
gdp['pmi'] = gdp['First Estimate of quarterly GDP (Month 2 delay estimate)'] * 0.25

corporate_colors = {
    'dark-blue-grey' : 'rgb(62, 64, 76)',
    'medium-blue-grey' : 'rgb(77, 79, 91)',
    'medium-blue' : 'rgb(27,167,201)',
    'superdark-green' : 'rgb(41, 56, 55)',
  #  'dark-green' : 'rgb(57, 81, 85)',
  #light-grey
    'light-grey' : 'rgb(240,240,240)',
    'medium-green' : 'rgb(51, 153, 102)',
    #white
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

fig.add_trace(
    go.Scatter(
        name='GDP',
        x=gdp["Relating to Period"],
        y=gdp["First Estimate of quarterly GDP (Month 2 delay estimate)"],
        mode='lines',
        marker=dict(color="red"),
        line=dict(width=4),
        showlegend=True))

fig.add_trace(
    go.Scatter(
        name='PMI',
        x=gdp["Relating to Period"],
        y=gdp['pmi'],
        mode='lines',
        marker=dict(color="orange"),
        opacity=0.75,
        line=dict(width=2),
        showlegend=True
    ))

fig.update_layout(height=750, barmode='overlay',
                  margin=dict(l=20, r=20, t=20, b=70),
                  # title = "GDP estimates",
                  font={
                      'size': 16,
                      'color': corporate_colors['black']},
                  xaxis_title="Quarter",
                  yaxis_title="GDP",
                  legend_title="Please Click to Select Trace(s):",
                  title_y=0.98,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  xaxis=corporate_xaxis,
                  yaxis=corporate_yaxis,
                  legend_font_family='sans-serif',
                  legend_font_color=corporate_colors['black'],
                  legend_font_size=10)

layout = html.Div([

       html.Div([

            html.Div([
                html.H1(children='HMT GDP Estimate Dashboard',
                        style={'color': corporate_colors['light-grey'], 'textAlign': 'center',
                               'font-family': 'sans-serif', 'fontSize': 40})

        ], style=filterdiv_borderstyling),

        dcc.Graph(figure=fig, style={'padding-top': '0.5%'}),

        html.H6("Based on data from ",
        style={'color': corporate_colors['black'], 'font-family': 'sans-serif'}),
#       html.H6("Please be aware that counts below 100 may not be an accurate representation of the population",
#           style={'color' : corporate_colors['black'], 'font-family' : 'sans-serif'}),


        ], style = {'background-color': corporate_colors['light-grey'],
        'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'})])


