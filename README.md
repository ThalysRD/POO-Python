# Inventory Report — estudo de POO em Python

Relatórios de estoque a partir de CSV, JSON e XML, desenvolvidos na formação Trybe. Este repositório é uma cópia histórica do exercício; a versão curada para apresentação está em [inventory-report](https://github.com/ThalysRD/inventory-report).

## O que o código faz

- Importa produtos com `Inventory.import_data` e importadores específicos por formato.
- Gera relatório simples: fabricação mais antiga, validade futura mais próxima e empresa com mais produtos.
- Gera relatório completo com contagem de produtos por empresa.
- Organiza o comportamento em classes e contratos de importação.

## Usar como biblioteca

Em um ambiente virtual Python ativo:

```sh
python -m pip install -e .
python -m pip install xmltodict
```

Exemplo a partir da raiz:

```python
from inventory_report.inventory.inventory import Inventory
print(Inventory.import_data('seu_estoque.csv', 'completo'))
```

Os registros precisam conter `data_de_fabricacao`, `data_de_validade` e `nome_da_empresa`, com datas no formato `AAAA-MM-DD`.

## Limitações e créditos

O cálculo de validade pressupõe pelo menos um produto ainda válido: dados antigos ou totalmente vencidos podem gerar erro. A CLI em `main.py` não está implementada. Não há Pandas nesta solução.

Thalys implementou importação e relatórios sobre a proposta e estrutura fornecidas pela Trybe. Dados de exercício e testes de avaliação não são de autoria exclusiva do estudante. A execução e a suíte não foram validadas nesta revisão documental.
