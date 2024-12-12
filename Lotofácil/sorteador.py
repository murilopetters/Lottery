import pandas as pd
from openpyxl import Workbook

# Caminho do arquivo de resultados
file_path = r"D:\GitHub\Lottery\Lotofácil\resultados.xlsx"

# Lê o arquivo de resultados
df = pd.read_excel(file_path)

# Análise dos dados
frequencia = df.iloc[:, 1:].stack().value_counts()

mais_sorteados = frequencia.nlargest(15).index.tolist()
menos_sorteados = frequencia.nsmallest(15).index.tolist()
pares = [num for num in frequencia.index if num % 2 == 0][:15]
impares = [num for num in frequencia.index if num % 2 != 0][:15]
combinados_top_menos = mais_sorteados[:7] + menos_sorteados[:8]
distribuicao_balanceada = frequencia.nlargest(8).index.tolist() + frequencia.nsmallest(7).index.tolist()

# Criação do Excel
output_file = r"D:\GitHub\Lottery\Lotofácil\Combinacoes_Lotofacil.xlsx"
with pd.ExcelWriter(output_file) as writer:
    pd.DataFrame({"Top 15 Mais Sorteados": mais_sorteados}).to_excel(writer, index=False, sheet_name="Mais Sorteados")
    pd.DataFrame({"Menos Sorteados": menos_sorteados}).to_excel(writer, index=False, sheet_name="Menos Sorteados")
    pd.DataFrame({"Pares": pares}).to_excel(writer, index=False, sheet_name="Pares")
    pd.DataFrame({"Ímpares": impares}).to_excel(writer, index=False, sheet_name="Ímpares")
    pd.DataFrame({"Combinados": combinados_top_menos}).to_excel(writer, index=False, sheet_name="Top e Menos")
    pd.DataFrame({"Distribuição Balanceada": distribuicao_balanceada}).to_excel(writer, index=False, sheet_name="Balanceada")
    pd.DataFrame({"Frequência": frequencia}).to_excel(writer, index=True, sheet_name="Frequência")

print(f"Arquivo salvo em: {output_file}")