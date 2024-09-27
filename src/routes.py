from flask import Blueprint, request, jsonify
from services.graph_service import gerar_grafico

def init_routes(app):
    """
    Inicializa as rotas da API Flask.

    Esta função registra todas as rotas disponíveis na aplicação Flask, vinculando as funções de serviço para
    atender as requisições HTTP recebidas.

    Parameters
    ----------
    app : Flask
        A instância da aplicação Flask na qual as rotas serão registradas.

    Returns
    -------
    None
    """
    @app.route('/gerarGrafico', methods=['POST'])
    def gerar_grafico_route():
        """
        Endpoint para gerar gráficos com base nos dados recebidos.

        Este endpoint aceita uma requisição POST contendo dados em formato JSON. Os dados devem incluir 
        as informações necessárias para gerar o gráfico, como o tipo de gráfico, título e dados a serem plotados.
        
        Exemplo de Payload esperado (JSON):
        ```json
        {
            { 
                type: 'Saida',
                value: 350.75,
                category: 'Pessoal'
            }
            { 
                type: 'Saida',
                value: 55.6,
                category: 'Pessoal'
            },
            { 
                type: 'Entrada',
                value: 5000,
                category: 'Profissional'
             },
        }
        ```

        O gráfico gerado é devolvido na resposta ou salvo no servidor, dependendo da lógica implementada.

        Returns
        -------
        Response
            Um objeto de resposta JSON contendo uma mensagem de sucesso ou erro.

        Responses
        ---------
        200 OK : 
            Quando o gráfico é gerado com sucesso.
        400 Bad Request : 
            Quando os dados fornecidos são inválidos ou insuficientes.
        
        Examples
        --------
        Exemplo de requisição:

        >>> import requests
        >>> url = 'http://localhost:5000/grafico'
        >>> payload = {
        ...     "dados": {"Janeiro": 1000, "Fevereiro": 1500, "Março": 1300},
        ...     "titulo": "Vendas Mensais",
        ...     "tipo_grafico": "barra"
        ... }
        >>> response = requests.post(url, json=payload)
        >>> print(response.json())
        {
            "message": "Gráfico gerado com sucesso!"
        }
        """
        try:
            data = request.json
            titulo = request.args['title_graph']
            tipo_grafico = request.args['type_graph']
            print(tipo_grafico, titulo)
            
            # Validação dos dados recebidos
            if not data or not titulo:
                return jsonify({"error": "Dados ou título ausente"}), 400
            
            # Gera o gráfico
            return gerar_grafico(data, titulo, tipo_grafico)
          
        except Exception as e:
            return jsonify({"error": str(e)}), 400