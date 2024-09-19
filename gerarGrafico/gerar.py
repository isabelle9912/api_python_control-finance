from flask import Flask, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import traceback

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
