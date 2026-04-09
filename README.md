# Análise de Funil de Vendas

Um projeto que desenvolvi para entender melhor onde um funil de vendas perde força — ou seja, em qual etapa os potenciais clientes param de avançar.

---

## Motivação

Trabalhar com dados de vendas sem visualização é difícil. Queria uma forma simples de ver, mês a mês, como os números se comportam entre visitantes, leads e vendas — e principalmente calcular as taxas de conversão entre cada etapa.

---

## O que o projeto faz

- Carrega os dados de um arquivo CSV com os dados mensais do funil
- Calcula a taxa de conversão de visitante para lead
- Calcula a taxa de conversão de lead para venda
- Exibe as médias gerais de conversão
- Gera dois gráficos salvos em PNG:
  - **grafico_volume.png** — mostra a quantidade de visitantes, leads e vendas por mês
  - **grafico_taxas.png** — mostra as taxas de conversão ao longo dos meses

---

## Tecnologias

- Python 3
- Pandas
- Matplotlib

---

## Como rodar

Clone o repositório e instale as dependências:

```bash
pip install pandas matplotlib
```

Depois é só executar:

```bash
python main.py
```

Os gráficos vão ser gerados automaticamente na mesma pasta.

---

## Estrutura dos arquivos

```
├── main.py            # script principal
├── dados_funil.csv    # dados mensais do funil (visitantes, leads, vendas)
├── grafico_volume.png # gerado ao rodar o script
└── grafico_taxas.png  # gerado ao rodar o script
```

---

## Formato esperado do CSV

O arquivo `dados_funil.csv` deve usar `;` como separador e conter as colunas:

```
mes;visitantes;leads;vendas
```

---

## Autor

Lucas Lemos — [github.com/lucaslemos11](https://github.com/lucaslemos11)
