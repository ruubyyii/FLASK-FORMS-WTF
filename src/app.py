from flask import Flask, render_template,request
from config import config
from form import Persona

app = Flask(__name__)

@app.route('/')
def index():
    return 'esto funciona'

@app.route('/formulario-simple', methods=['GET','POST'])
def formulario_simple():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        telefono = request.form.get('telefono')
        
        print(username,email,password,telefono)
    
    else:
            return render_template('formulario-simple.html')

@app.route('/formulario-simple-objeto', methods=['GET', 'POST'])
def formulario_objeto():
    form = Persona()

    if form.validate() and request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        telefono = request.form.get('telefono')

        print(username, email, password, telefono)
        return 'Datos procesados'
    

@app.route('/formulario-simple-macro', methods=['GET', 'POST'])
def formulario_objeto_macro():
    form = Persona()

    if form.validate() and request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        telefono = request.form.get('telefono')

        print(username, email, password, telefono)
        return 'Datos procesados'

    else:
        return render_template('formulario-simple-macro.html',form=form) 

def status_404(error):
    return '<h1>Pagina no encontrada</h1>'

if __name__ == '__main__':

    app.config.from_object(config['development'])
    app.register_error_handler(404, status_404)
    app.run()