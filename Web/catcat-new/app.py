import os
import uuid
from flask import Flask, request, session, render_template, Markup
from cat import cat

flag = ''
app = Flask(
    __name__,
    static_url_path='/', 
    static_folder='static' 
)
app.config['SECRET_KEY'] = str(uuid.uuid4()).replace('-', '') + '*abcdefgh'
if os.path.isfile('/flag'):
    flag = cat('/flag')
    os.remove('/flag')

@app.route('/', methods=['GET'])
def index():
    detailtxt = os.listdir('./details/')
    cats_list = []
    for i in detailtxt:
        cats_list.append(i[:i.index('.')])
        
    return render_template('index.html', cats_list=cats_list, cat=cat)



@app.route('/info', methods=['GET', 'POST'])
def info():
    filename = './details/' + request.args.get('file', '')
    start = request.args.get('start', '0')
    end = request.args.get('end', '0')
    name = request.args.get('file', '')[:request.args.get('file', '').index('.')]
    
    return render_template('detail.html', catname=name, info=cat(filename, start, end))
    


@app.route('/admin', methods=['GET'])
def admin_can_list_root():
    if session.get('admin') == 1:
        return flag
    else:
        session['admin'] = 0
        return 'NoNoNo'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5637)