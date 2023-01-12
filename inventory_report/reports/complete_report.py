from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def __init__(self, report):
        super().__init__(report)

    @staticmethod
    def generate(report):
        message = CompleteReport.products(report)
        return (
            f"{SimpleReport.generate(report)}\n"
            f"Produtos estocados por empresa:\n"
            f"{message}")

    def products(report):
        products_list = []
        dicilist = ''
        for product in report:
            products_list.append(product['nome_da_empresa'])
        products_list = Counter(products_list).most_common()
        for company, product in products_list:
            dicilist += f'- {company}: {product}\n'
      
        return dicilist
