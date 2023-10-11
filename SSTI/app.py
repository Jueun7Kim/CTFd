from flask import Flask, request, render_template_string

app = Flask(__name__)
app.secret_key= "GSM2023{F@t_s@nG1huyk_Fㅣg}"


@app.route('/', methods=["GET"])
def index():
    get = request.args.get('get')
    if get:
        tem ='''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Wow</title>
                </head>
                <body>
                    <h1>I know what you typed</h1>

                    <form method="get" action="/">
                    <input type="text" name="get" placeholder="Type something">
                    <input type="submit" value="Submit">
                    </form>
                
                    <h3>%s</h3>
                    <h3>
                </body>
            </html>'''%get	
        rt =  render_template_string(tem, get=get)
    else:
        rt = tem ='''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Wow</title>
                </head>
                <body>
                    <h1>I know what you typed</h1>

                    <form method="get" action="/">
                    <input type="text" name="get" placeholder="Type something">
                    <input type="submit" value="Submit">
                    </form>
                
                    <h3>%s</h3>
                    <h3>
                </body>
            </html>'''
        rt =  render_template_string(tem)
    return rt

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8992)