from flask import Flask, render_template, request   


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    nome = None
    peso = None
    altura = None
    imc = None
    diagnostico = None
    if request.method == 'POST':
        nome = request.form.get('nome') 
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = peso / (altura ** 2)
        if imc < 18.5:
            diagnostico = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            diagnostico = "Peso normal"
        elif 25 <= imc < 30:
            diagnostico = "Sobrepeso"
        else:
            diagnostico = "Obesidade"
        return render_template('index.html', resultado=imc, nome=nome, peso=peso, altura=altura, diagnostico=diagnostico)

if __name__ == '__main__':
    app.run(debug=True)