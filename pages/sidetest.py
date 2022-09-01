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
    style=SIDEBAR_STYLE,