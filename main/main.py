from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from app import server
from apps import graphQ,graphY,home


button1 =   dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Quarterly", href="/apps/Q"),
             dbc.DropdownMenuItem("Annual", href="/apps/Y"),
            ],
        label="Non-financial companies",color='success',className="m-1")

button2 =  dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Quarterly", href="/apps/bankQ"),
             dbc.DropdownMenuItem("Annual", href="/apps/bankY"),
            ],
        label="Banks",color='success',className="m-1")
button3 =  dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Quarterly", href="/apps/secQ"),
             dbc.DropdownMenuItem("Annual", href="/apps/secY")
            ],
        label="Securities companies",color='success',className="m-1")
button4 =  dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Quarterly", href="/apps/insQ"),
             dbc.DropdownMenuItem("Annual", href="/apps/insY")
            ],
        label="Insurance companies",color='success',className="m-1")


button = html.Div(children=[button1,button2,button3,button4],className='ml-auto',style={"display": "flex", "flexWrap": "wrap"})


app.layout = html.Div([dbc.Navbar(
    children = [html.A(dbc.Row([dbc.Col(html.Img(src=app.get_asset_url('img/THTC Logo 1 Transparent White.png'),height="60px")),
                    ],
                align="center",
                className="g-0"
            ),
            href="/",
        ),
        button
    ],
    color="primary",
    dark=True,
    # sticky="top",
),
dcc.Location(id='url', refresh=False),
html.Div(id='page-content', children=[])
                      ])

@app.callback(Output(component_id='page-content', component_property='children'),
              [Input(component_id='url', component_property='pathname')]
              )
def display_page(pathname):
    if pathname == '/apps/Y':
        return graphY.layout
    if pathname == '/apps/Q':
        return graphQ.layout
#     if pathname == '/apps/bankY':
#         return graphYbank.layout
#     if pathname == '/apps/bankQ':
#         return graphQbank.layout
# #    if pathname == '/apps/secY':
# #        return graphYsec.layout
# #    if pathname == '/apps/secQ':
#         return graphQsec.layout
#     if pathname == '/apps/insY':
#         return graphYins.layout
#     if pathname == '/apps/insQ':
#         return graphQins.layout
#         return graphSQLY.layout
#     if pathname == '/apps/ctyrel':
#         return ctyrel.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)
