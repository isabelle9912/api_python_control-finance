from flask import Flask, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import io
import base64
import traceback

app = Flask(__name__)

@app.route('/formatarJson', methods=['POST'])
def formatar_json():
    data = request.json
    df = pd.DataFrame(data)
    return df.to_json(orient='records')

@app.route('/gerarGrafico', methods=['POST'])
def gerar_grafico():
    try:
        # Obtém os dados enviados pelo método POST
        data = request.json
        
        # Converte os dados em um DataFrame do Pandas
        df = pd.DataFrame(data)
        
        # Imprimir as primeiras linhas e colunas para depuração
        print('DataFrame recebido:')
        print(df.head())
        print('Colunas:', df.columns)
        
        # Verifica se as colunas esperadas existem
        if 'month' not in df.columns or 'value' not in df.columns:
            return jsonify({"error": "Dados inválidos, colunas esperadas: 'month' e 'value'"}), 400

        # Gerar o gráfico
        plt.figure(figsize=(10, 5))
        df.plot(kind='bar', x='month', y='value')
        plt.title('Gráfico de Exemplo')
        plt.xlabel('Mês')
        plt.ylabel('Valor')
        
        # Salvar o gráfico em um objeto de memória
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()
        
        # Codificar a imagem em base64
        img_base64 = base64.b64encode(img.read()).decode('utf-8')

        # Retornar a imagem como uma string base64
        return jsonify({"image": img_base64})

    except Exception as e:
        print(f"Erro: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Erro interno do servidor"}), 500


@app.route('/GerarGraficoCategorias', methods=['POST'])
def gerar_teste():
    # Obtendo os dados enviados pela api
    data = request.json
    # Criando um DataFrame
    df = pd.DataFrame(data)

    # Filtra os dados e calcula os totais
    total_saida_pessoal = df[(df['type'] == 'Saida') & (df['category'] == 'Pessoal')]['value'].sum()
    total_entrada_pessoal = df[(df['type'] == 'Entrada') & (df['category'] == 'Pessoal')]['value'].sum()
    total_saida_profissional = df[(df['type'] == 'Saida') & (df['category'] == 'Profissional')]['value'].sum()
    total_entrada_profissional = df[(df['type'] == 'Entrada') & (df['category'] == 'Profissional')]['value'].sum()

    # Exibe os resultados
    print(f"Total Saída Pessoal: {total_saida_pessoal}")
    print(f"Total Entrada Pessoal: {total_entrada_pessoal}")
    print(f"Total Saída Profissional: {total_saida_profissional}")
    print(f"Total Entrada Profissional: {total_entrada_profissional}")

    # Prepara os dados para o gráfico
    labels = ['S Pessoal', 'E Pessoal', 'S Profissional', 'E Profissional']
    values = [total_saida_pessoal, total_entrada_pessoal, total_saida_profissional, total_entrada_profissional]

    # Gera o gráfico de barras
    plt.bar(labels, values)
    plt.xlabel('Categoria')
    plt.ylabel('Total (R$)')
    plt.title('Totais por Categoria e Tipo')
    
    # Salvar o gráfico em um objeto de memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    
    # Codifica a imagem em base64
    img_base64 = base64.b64encode(img.read()).decode('utf-8')

    # Retornar a imagem como uma string base64
    return jsonify({"image": img_base64})


if __name__ == "__main__":
    app.run(port=5000)
