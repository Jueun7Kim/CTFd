from flask import *

app = Flask(__name__, template_folder='templates')

flag = "2023GSM{_Th1S_S1t3'S_FE_w@S_m@D3_by_G@0n_}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        money = data.get('money', 0)
        print(money)
        print(data)
        
        if money >= 50000:
            return {'redirectUri': '''/2023GSM{_Th1S_S1t3'S_FE_w@S_m@D3_by_G@0n_}'''}
        else:
            rt = render_template('index.html')
            
    else:
        rt = render_template('index.html')
    return rt


# @app.route('/2023GSM{_Th1S_S1t3_FE_w@S_m@D3_by_G@0n_}', methods = ['GET'])
# def flag():
#     return render_template('flag.html')

@app.route('''/2023GSM{_Th1S_S1t3'S_FE_w@S_m@D3_by_G@0n_}''')
def test():
    return render_template('''2023GSM{_Th1S_S1t3'S_FE_w@S_m@D3_by_G@0n_}.html''')



if __name__ == "__main__":
    app.run(use_reloader=True)