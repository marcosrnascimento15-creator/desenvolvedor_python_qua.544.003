from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        nome = request.form.get('nome', '')
    else:
        nome = request.args.get('nome', '')
    return render_template('index.html', nome=nome)

@app.route('/novaPagina.html', methods=['GET', 'POST'])
def novaPagina():
    if request.method == 'POST':
        nome = request.form.get('nome', '')
        return redirect(url_for('index', nome=nome))
    return render_template('novaPagina.html')

if __name__ == '__main__':
    app.run(debug=True)