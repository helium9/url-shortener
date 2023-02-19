#Set-ExecutionPolicy Unrestricted -Scope Process
from flask import Flask
from flask import request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/json')
def handle_json_request():
    import json
    with open("Files/maps.json", 'r') as f:
        data = json.load(f)
    return data

@app.route('/update', methods=['POST'])
def update_file():
    if request.method == 'POST':
        import json
        f = request.get_json(force=True)
        with open("Files/maps.json", 'r') as p:
            data = json.load(p)
        add_on = f
        data.update(add_on)
        with open("Files/maps.json", 'w') as f:
            json.dump(data, f)
        return ("Your shortened URL is: "+str(list(add_on.keys())[0]))
    
@app.route('/<key>')
def redirect_to_link(key=''):
    import json
    with open("Files/maps.json", 'r') as f:
        data = json.load(f)
    redirect_url = data[str("http://127.0.0.1:5000/"+key)]
    if 'http' not in redirect_url: #to ensure local prefix is not added. something like: "localhost:5000/www.google.com".
        redirect_url = 'http://' + redirect_url
    return redirect(redirect_url)