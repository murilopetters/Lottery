# Sorteador de Números para Lotofácil

Este projeto fornece uma ferramenta automatizada para análise de dados históricos da Lotofácil e geração de combinações de números para apostas. Utilizando bibliotecas do Python, como `pandas` e `openpyxl`, o script analisa a frequência de números sorteados em concursos anteriores e gera sugestões de combinações baseadas em padrões observados.

## Funcionalidades

1. **Análise de Dados**:
   - Frequência dos números mais sorteados.
   - Frequência dos números menos sorteados.
   - Porcentagem de números pares e ímpares sorteados.
   - Outras análises baseadas em distribuições históricas.

2. **Sugestão de Combinações**:
   - Top 15 números mais sorteados.
   - Top 15 números menos sorteados.
   - Combinação balanceada de pares e ímpares.
   - Combinação de números mais e menos sorteados.
   - Distribuição equilibrada baseada em frequências.

3. **Exportação para Excel**:
   - As análises e combinações são exportadas para um arquivo Excel, com abas organizadas por tipo de análise.

## Como Usar

### Pré-requisitos

Certifique-se de ter instalado:
- Python 3.x
- Bibliotecas `pandas` e `openpyxl`.

### Instalação de Bibliotecas

No terminal, execute:
```bash
pip install pandas openpyxl
```

### Estrutura do Projeto

O script está configurado para ser executado dentro do repositório, com os seguintes arquivos:

```
Lottery/
├── Lotofácil/
│   ├── resultados.xlsx
│   ├── sorteador.py
│   └── Combinacoes_Lotofacil.xlsx
└── README.md
```

- **resultados.xlsx**: Contém os resultados históricos da Lotofácil, organizados conforme o formato esperado pelo script.
- **sorteador.py**: Script Python que realiza as análises e gera as combinações.
- **Combinacoes_Lotofacil.xlsx**: Arquivo gerado pelo script contendo as análises e combinações sugeridas.

### Formato do Arquivo de Entrada (`resultados.xlsx`)

- O arquivo deve conter:
  - **Coluna 1**: Número do concurso.
  - **Colunas 2 a 16**: Números sorteados em cada concurso.

Exemplo:
```
Concurso   Dezena 1   Dezena 2   ...   Dezena 15
1          1          3                25
2          2          5                22
...
```

### Executando o Script

1. Navegue até a pasta `Lotofácil`:
```bash
cd D:\GitHub\Lottery\Lotofácil
```

2. Execute o script:
```bash
python sorteador.py
```

3. O arquivo `Combinacoes_Lotofacil.xlsx` será gerado na pasta `Lotofácil` com as seguintes abas:
   - **Mais Sorteados**: Lista dos 15 números mais sorteados.
   - **Menos Sorteados**: Lista dos 15 números menos sorteados.
   - **Pares**: Lista dos 15 números pares mais sorteados.
   - **Ímpares**: Lista dos 15 números ímpares mais sorteados.
   - **Top e Menos**: Combinação de 7 números mais sorteados e 8 menos sorteados.
   - **Balanceada**: Combinação equilibrada baseada nas frequências.
   - **Frequência**: Frequência completa de todos os números.

## Modificações Recentes

- **Alteração do Script**: Agora, o script salva diretamente o arquivo Excel na pasta `Lotofácil`.
- **Redução dos Números Gerados**: A combinação principal foi ajustada para gerar apenas 15 números, com base em frequência histórica.
- **Novas Combinações**: Adicionadas 9 combinações diferentes, incluindo distribuição balanceada e combinações de pares e ímpares.

## Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.