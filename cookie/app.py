from flask import *

app = Flask(__name__)

flag= "2023BSC{_heeseong_love_robotics_}"

@app.route('/')
def index():
    cookie = request.cookies.get('id')

    if cookie == "admin":
        rt = render_template('index.html', user="admin", flag = flag)
    elif cookie:
        rt = render_template('index.html', user="user")
    else:
        rt=make_response(render_template('index.html', user="guest"))
        rt.set_cookie('id', 'guest')

    return rt

if __name__ == "__main__":
    app.run(use_reloader=True)
