import matplotlib
matplotlib.use('Agg')  # Define o backend para renderizar gráficos em segundo plano
import matplotlib.pyplot as plt
import io
import base64
from flask import jsonify
from utils.data_processing import process_financial_data
from utils.helpers import json_to_dataframe

def gerar_grafico(data, title: str, type_graph: str):
    """
    Gera um gráfico a partir dos dados fornecidos.

    Esta função aceita um DataFrame Pandas convertido de JSON e gera gráficos de barra, linha, 
    pizza (pie), área e dispersão (scatter) com base no tipo de gráfico selecionado.

    Parameters
    ----------
    data : dict
        Dados enviados na requisição para gerar o gráfico.
    title : str
        Título do gráfico.
    type_graph : str
        Tipo de gráfico a ser gerado. Pode ser 'barra', 'linha', 'pizza', 'area' ou 'dispersao'.

    Returns
    -------
    Response
        Um objeto JSON com a imagem do gráfico codificada em base64.
    
    Raises
    ------
    ValueError
        Se o tipo de gráfico fornecido não for suportado.
    """
    # 1. Obter os dados da requisição e converter para DataFrame
    df = json_to_dataframe(data)  # Converte o JSON para DataFrame
    print(df)  # Exibe os dados para depuração

    # 2. Processar os dados financeiros
    values_list = process_financial_data(df)

    # 3. Preparar os rótulos e cores para o gráfico
    labels = ['Saldo Pessoal', 'Gasto Pessoal', 'Saldo Profissional', 'Gasto Profissional']
    colors = ['green', 'red', 'green', 'red']  # Verde para saldo (entrada), vermelho para gastos (saída)

    # 4. Geração do gráfico
    if type_graph == "barra":
        plt.bar(labels, values_list, color=colors)
    elif type_graph == "linha":
        plt.plot(labels, values_list, color='blue', marker='o')
    elif type_graph == "pizza":
        explode = [0.1, 0.1, 0.1, 0.1]  # Explode a fatia 1 (Saldo Pessoal) e a fatia 3 (Saldo Profissional)
        plt.pie(values_list, labels=None, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode)
        plt.legend(labels, loc="best", fontsize=12)
    elif type_graph == "area":
        plt.fill_between(range(len(labels)), values_list, color='skyblue', alpha=0.4)
        plt.plot(labels, values_list, color='Slateblue', alpha=0.6, linewidth=2)
    elif type_graph == "dispersao":
        plt.scatter(labels, values_list, color='purple')
        for i, value in enumerate(values_list):
            plt.text(i, value, f'R${value:.2f}', ha='center', va='bottom')
    else:
        raise ValueError(f"Tipo de gráfico '{type_graph}' não suportado.")

    # Adiciona os valores no topo das barras (para barra e dispersão)
    if type_graph in ["barra", "dispersao"]:
        for i, value in enumerate(values_list):
            plt.text(i, value + 50, f'R${value:.2f}', ha='center', va='bottom')

    # Definir títulos e layout
    plt.xlabel('Categorias (Pessoal/Profissional)', fontsize=12)
    plt.ylabel('Total (R$)', fontsize=12)
    plt.title(title, fontsize=14)
    plt.tight_layout()

    # 5. Salvar a imagem em um buffer de memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # 6. Codificar a imagem em base64 para enviar no JSON
    img_base64 = base64.b64encode(img.read()).decode('utf-8')

    return jsonify({"image": img_base64})