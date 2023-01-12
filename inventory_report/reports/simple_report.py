from datetime import date as datetime
from collections import Counter


class SimpleReport:
    def __init__(self, report):
        self.report = report

    @staticmethod
    def generate(report):
        expiration_date = SimpleReport.expiration(report)
        creation_date = SimpleReport.creation(report)
        enterprise = SimpleReport.more_products(report)
        message = (
            f"Data de fabricação mais antiga: {creation_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {enterprise}"
        )
        return message

    def expiration(report):
        today = str(datetime.today())
        expiration_dates = []
        valid_dates = []
        for document in report:
            expiration_dates.append(document['data_de_validade'])
        for date in expiration_dates:
            if today < date:
                valid_dates.append(date)
        return min(valid_dates)

    def creation(report):
        manufacturing_date = []
        for documentation in report:
            manufacturing_date.append(documentation['data_de_fabricacao'])
        return min(manufacturing_date)

    def more_products(report):
        companys = []
        products = ''
        result = ''
        for company in report:
            companys.append(company['nome_da_empresa'])
        enterprise = Counter(companys).most_common(1)
        for company, product in enterprise:
            result = f'{company}'
            products += f'{product}'
        return result
