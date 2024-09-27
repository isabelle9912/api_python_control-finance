# API de Geração de Gráficos Financeiros

Esta API foi desenvolvida em Flask e tem como objetivo gerar gráficos financeiros a partir de dados enviados no formato JSON. A API suporta múltiplos tipos de gráficos, como barras, linhas, pizza, área e dispersão, para representar de forma visual informações financeiras relacionadas a saldo e gastos pessoais e profissionais.

## Funcionalidades

- **Conversão de dados JSON para gráficos financeiros**
- **Geração de diferentes tipos de gráficos**: barra, linha, pizza, área, e dispersão
- **Resposta em formato de imagem base64, pronta para ser exibida diretamente em aplicações web**
  
## Tecnologias Utilizadas

- Python 3.11+
- Flask
- Matplotlib
- Pandas
- JSON
- Base64

## Instalação

### Pré-requisitos

- Python 3.11 ou superior instalado
- Pip (gerenciador de pacotes Python)
- Virtualenv (opcional, mas recomendado)

### Passos de Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/isabelle9912/api_python_control-finance.git
   ```

2. Crie e ative um ambiente virtual (opcional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute a API:

   ```bash
   python app.py
   ```

   A API estará rodando no endereço `http://127.0.0.1:5000`.

## Endpoints

### POST `/gerarGrafico`

Este endpoint gera gráficos financeiros com base em dados fornecidos pelo cliente.

#### Parâmetros

- **data**: Dados financeiros no formato JSON (veja o exemplo abaixo).
- **title**: Título para o gráfico.
- **type_graph**: Tipo de gráfico a ser gerado. Pode ser um dos seguintes valores:
  - `barra`
  - `linha`
  - `pizza`
  - `area`
  - `dispersao`

#### Exemplo de Requisição

```bash
POST /gerarGrafico HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "data": [
    {"type": "Saida", "value": 350.75, "category": "Pessoal"},
    {"type": "Saida", "value": 700.00, "category": "Pessoal"},
    {"type": "Saida", "value": 55.60, "category": "Pessoal"},
    {"type": "Entrada", "value": 1000.00, "category": "Profissional"},
    {"type": "Entrada", "value": 600.00, "category": "Profissional"},
    {"type": "Saida", "value": 129.30, "category": "Profissional"}
  ],
  "title": "Gráfico Financeiro do Mês",
  "type_graph": "pizza"
}
```

#### Exemplo de Resposta

```json
{
  "image": "/9j/4AAQSkZJRgABAQEAAAAAAAD/..."
}
```

A resposta contém a imagem do gráfico codificada em base64.

### Tipos de Gráficos Suportados

- **barra**: Gráfico de barras para comparação direta entre categorias.
- **linha**: Gráfico de linha que conecta pontos de dados ao longo do tempo.
- **pizza**: Gráfico de pizza para representar proporções.
- **area**: Gráfico de área para mostrar o acúmulo de valores ao longo de categorias.
- **dispersao**: Gráfico de dispersão para visualizar a relação entre duas variáveis.

## Exemplos de Utilização

Aqui estão exemplos de como consumir a API em diferentes linguagens de programação.

### Com Python (Usando `requests`)

```python
import requests
import json

url = 'http://127.0.0.1:5000/gerarGrafico?type_graph=barra&title_graph=CategoriaAAA'
data = {
    "data": [
        {"type": "Saida", "value": 350.75, "category": "Pessoal"},
        {"type": "Saida", "value": 700.00, "category": "Pessoal"},
        {"type": "Saida", "value": 55.60, "category": "Pessoal"},
        {"type": "Entrada", "value": 1000.00, "category": "Profissional"},
        {"type": "Entrada", "value": 600.00, "category": "Profissional"},
        {"type": "Saida", "value": 129.30, "category": "Profissional"}
    ],
}

## Estrutura do Projeto

```bash
├── app.py               # Arquivo principal para rodar a API Flask
├── services/
│   ├── graph_service.py  # Contém as funções para geração dos gráficos
│   └── helpers.py        # Funções auxiliares (ex: conversão de JSON para DataFrame)
├── routes.py             # Define as rotas da aplicação
├── requirements.txt      # Dependências do projeto
└── README.md             # Instruções e documentação da API
```

## Melhorias Futuras

- Suporte para novos tipos de gráficos
- Filtragem de dados por período de tempo
- Autenticação de usuários
- Integração com bancos de dados para armazenamento dos gráficos gerados

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório.

---