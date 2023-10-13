from flask import *

app = Flask(__name__)

flag = "2023GSM{_Th1S_S1t3'S_FE_w@S_m@D3_by_G@0n_}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        money = data.get('money', 0)
        print(money)
        
        if money == 0:
            rt =  redirect(url_for('flag'))
            return rt
        else:
            rt = render_template('index.html')
        
    else:
        rt = render_template('index.html')

    return rt


@app.route('/2023GSM{_Th1S_S1t3_FE_w@S_m@D3_by_G@0n_}', methods = ['GET'])
def flag():
    return render_template('flag.html')

@app.route('/test')
def test():
    if True:
        rt = redirect(url_for('flag'))
    else:
        rt = redirect(url_for('flag'))
    return rt



if __name__ == "__main__":
    app.run(use_reloader=True)