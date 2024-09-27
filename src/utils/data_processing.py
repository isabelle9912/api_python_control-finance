from utils.helpers import calc_value

def process_financial_data(df):
    """
    Processa os dados financeiros e retorna uma lista com os totais de:
    - Saldo Pessoal
    - Gasto Pessoal
    - Saldo Profissional
    - Gasto Profissional

    Parameters
    ----------
    df: DataFrame
        DataFrame Pandas contendo os dados financeiros.

    Returns:
    - Uma lista de totais.
    """
    
    # Definir categorias e tipos
    type_list = ['Entrada', 'Saida']
    category_list = ['Pessoal', 'Profissional']
    values_list = []

    for i in range(2):  # Dois tipos: Pessoal, Profissional
        for j in range(2):  # Entrada e Saída
            total_value = calc_value(df, type_list[j], category_list[i])
            values_list.append(total_value)

    return values_list
