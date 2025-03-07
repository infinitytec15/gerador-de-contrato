from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_procuracao', methods=['POST'])
def gerar_procuracao():
    # Coletar dados do formulário
    dados = {
        'nome': request.form['nome'],
        'apelido': request.form['apelido'],
        'nacionalidade': request.form['nacionalidade'],
        'profissao': request.form['profissao'],
        'estado_civil': request.form['estado_civil'],
        'rg_uf': request.form['rg_uf'],
        'cpf': request.form['cpf'],
        'rua': request.form['rua'],
        'numero': request.form['numero'],
        'bairro': request.form['bairro'],
        'municipio_uf': request.form['municipio_uf'],
        'cep': request.form['cep'],
        'telefone': request.form['telefone']
    }

    # Criar um buffer para o PDF
    buffer = BytesIO()

    # Criar o PDF
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Adicionar os dados ao PDF
    y = 750  # Posição inicial no eixo Y
    for key, value in dados.items():
        pdf.drawString(50, y, f"{key.capitalize()}: {value}")
        y -= 20  # Move para a próxima linha

    # Finalizar o PDF
    pdf.showPage()
    pdf.save()

    # Retornar o PDF para o usuário
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='procuração.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)