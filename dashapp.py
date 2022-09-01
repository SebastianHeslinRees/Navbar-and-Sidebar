import dash
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc
import os

class DashApp:

    def serve_layout(name, numroles): 
        LOGO = 'https://publicappointments.cabinetoffice.gov.uk/wp-content/uploads/2018/02/HMT-logo.png'   
        search_bar = dbc.Row(
        [
            dbc.Col(
                dbc.Input(type="search", placeholder="Search")),
            dbc.Nav([

            ]),
            dbc.Col(
                dbc.Button(
                    "Search", color="black", className="ms-2", n_clicks=0
                ),
                width="auto",
            ),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="center")

        navbar = dbc.Navbar(
            dbc.Container(
            [
                html.A(
                    dbc.Row([
                        dbc.Col(html.Img(src=LOGO, height="60px")),
                        dbc.Col(dbc.NavbarBrand("The HMT Data Hub - " + name, className="ms-2"))],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler"),
                        dbc.Collapse(
                            dbc.Nav(
                                [
                                    dbc.DropdownMenu(
                                        nav=True,
                                        in_navbar=True,
                                        label="Menu",
                                        children=[
                                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                                            for page in dash.page_registry.values()
                                            if page["module"] != "pages.not_found_404"
                                        ],
                                    ),
                                    dbc.NavItem(dbc.NavLink("Help"), style={"font_color": "black"}),
                                    dbc.NavItem(dbc.NavLink("About")),
                                    dbc.Collapse(
                                        search_bar,
                                        id="navbar-collapse1",
                                        is_open=False,
                                        navbar=True,
                                    ),
                                ],
                                # make sure nav takes up the full width for auto
                                # margin to get applied
                                className="w-100",
                            ),
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    # the row should expand to fill the available horizontal space
                    className="flex-grow-1",
                ),
            ],
            fluid=True,
            ),
            dark=True,
            color='#cd3333',
            )
        return dbc.Container(
        [navbar, dash.page_container],
        fluid=True,
    )


