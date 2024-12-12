# Lotofácil - Análise Histórica e Sugestão de Números

Este repositório contém um script em Python para realizar a análise histórica dos resultados da Lotofácil e fornecer uma sugestão de combinação de números baseada em padrões e insights extraídos.

## Funcionalidades

1. **Análise de Dados**
   - Frequência de cada número sorteado.
   - Porcentagem de pares e ímpares em todos os concursos.
   - Distribuição de números por décadas (1-10, 11-20, 21-25).
   - Repetição de números entre concursos consecutivos.

2. **Sugestão de Números**
   - Gera uma lista com os 25 números mais frequentes para serem utilizados em apostas.

3. **Saída Organizada em Excel**
   - O script gera um arquivo Excel chamado `analise_lotofacil.xlsx`, contendo:
     - Frequência de cada número.
     - Análise de pares e ímpares.
     - Distribuição por décadas.
     - Repetição de números entre concursos.
     - Sugestão de números para apostas.

## Requisitos

- Python 3.8+
- Bibliotecas Python:
  - `pandas`
  - `openpyxl`

Para instalar as dependências, execute:
```bash
pip install -r requirements.txt
```

## Como Utilizar

1. **Prepare o arquivo de entrada**:
   - Crie um arquivo Excel chamado `resultados.xlsx` e coloque-o na mesma pasta do script.
   - O formato do arquivo deve ser:
     - **Coluna 1**: Número do concurso.
     - **Colunas 2 a 16**: Números sorteados.

2. **Execute o script**:
   - Navegue até a pasta do projeto:
     ```bash
     cd D:/GitHub/Lottery/Lotofácil
     ```
   - Execute o script:
     ```bash
     python sorteador.py
     ```

3. **Confira a Saída**:
   - O arquivo `analise_lotofacil.xlsx` será gerado na mesma pasta, contendo todas as análises e sugestões.

## Estrutura do Projeto

```
Lottery/
|— Lotofácil/
   |— resultados.xlsx    # Arquivo de entrada com os resultados históricos
   |— sorteador.py       # Script principal
   |— analise_lotofacil.xlsx # Saída gerada pelo script
   |— requirements.txt   # Dependências do projeto
```

## Exemplo de Saída

O arquivo `analise_lotofacil.xlsx` conterá as seguintes abas:

1. **Frequência dos Números**: Tabela com a contagem de vezes que cada número foi sorteado.
2. **Pares e Ímpares**: Percentual de números pares e ímpares sorteados.
3. **Distribuição por Décadas**: Quantidade de números sorteados em cada intervalo (1-10, 11-20, 21-25).
4. **Repetição de Números**: Percentual de números que se repetem em relação ao concurso anterior.
5. **Sugestão de Números**: Lista dos 25 números mais frequentes para a sua aposta.

## Contribuições

Contribuições são bem-vindas! Fique à vontade para abrir uma *issue* ou enviar um *pull request* com melhorias.

## Aviso Legal

Este projeto é apenas para fins educacionais e de entretenimento. Não há garantias de ganho em apostas baseadas nas análises fornecidas.

---
**Boa sorte nas suas apostas!** 🍀