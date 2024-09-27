import pandas as pd

def json_to_dataframe(data):
    """
    Converte um JSON para um DataFrame Pandas.

    Esta função aceita um JSON formatado como uma lista de dicionários, onde cada dicionário representa uma linha
    de dados e as chaves representam as colunas. O JSON é então convertido para um DataFrame do Pandas para facilitar
    a manipulação e análise dos dados.

    Parameters
    ----------
    data : list of dict
        Lista de dicionários representando os dados financeiros no formato JSON.
        Cada dicionário deve conter colunas como 'type', 'category' e 'value'.

    Returns
    -------
    pd.DataFrame
        DataFrame Pandas contendo os dados convertidos do JSON.

    Examples
    --------
    >>> json_data = [
    ...     {"type": "Entrada", "category": "Pessoal", "value": 1000},
    ...     {"type": "Saida", "category": "Profissional", "value": 500}
    ... ]
    >>> df = json_to_dataframe(json_data)
    >>> print(df)
          type      category  value
    0  Entrada       Pessoal   1000
    1    Saida  Profissional    500
    """
        
    return pd.DataFrame(data)

def calc_value(dataframe, type, category):
    """
    Calcula o valor total baseado no 'type' (Entrada ou Saída) e 'category' (Pessoal ou Profissional).

    A função filtra os dados no DataFrame Pandas com base nos valores da coluna 'type' e 'category',
    e retorna a soma dos valores presentes na coluna 'value' para essa combinação específica.

    Parameters
    ----------
    dataframe : pd.DataFrame
        O DataFrame contendo os dados financeiros.
    type : str
        Tipo da transação, deve ser 'Entrada' ou 'Saída'.
    category : str
        Categoria da transação, deve ser 'Pessoal' ou 'Profissional'.

    Returns
    -------
    float
        A soma total dos valores para a combinação de 'type' e 'category'.

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     "type": ["Entrada", "Entrada", "Saida", "Saida"],
    ...     "category": ["Pessoal", "Profissional", "Pessoal", "Profissional"],
    ...     "value": [1000, 2000, 500, 1200]
    ... })
    >>> total_pessoal_entrada = calc_value(df, "Entrada", "Pessoal")
    >>> print(total_pessoal_entrada)
    1000.0

    >>> total_profissional_saida = calc_value(df, "Saida", "Profissional")
    >>> print(total_profissional_saida)
    1200.0
    """
    
    filtered_df = dataframe[(dataframe['type'] == type) & (dataframe['category'] == category)]
    return filtered_df['value'].sum()
