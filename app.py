from dash import *
from testapp import *

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1('You Passed'),
    github_info_header(),
    html.Img(src="assets/Screenshot 2022-01-25 193506.png")
])

if __name__ == '__main__':
    app.run_server(debug=True)






