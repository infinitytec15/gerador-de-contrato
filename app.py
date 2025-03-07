from flask import Flask, render_template, request, send_file
from docx import Document

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

    # Abrir o template do contrato
    doc = Document('templates/procuração_template.docx')

    # Número de páginas a serem geradas (exemplo: 3 páginas)
    num_paginas = 3

    for _ in range(num_paginas):
        # Substituir placeholders pelos dados
        for paragraph in doc.paragraphs:
            for key, value in dados.items():
                if f'{{{key}}}' in paragraph.text:
                    paragraph.text = paragraph.text.replace(f'{{{key}}}', value)

        # Adicionar uma quebra de página após cada conjunto de dados
        if _ < num_paginas - 1:
            doc.add_page_break()

    # Salvar o contrato gerado
    output_path = 'procuração_gerada.docx'
    doc.save(output_path)

    # Enviar o contrato gerado para o usuário
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)