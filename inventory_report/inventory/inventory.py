from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    def __init__(self, path, type):
        self.path = path
        self.type = type
        print(type, path)

    @staticmethod
    def import_data(path, type):
        infos = []
        with open(path, 'r') as file:
            reports = csv.DictReader(file)
            for report in reports:
                infos.append(report)
        if type == "simples":
            return SimpleReport.generate(infos)

        if type == "completo":
            return CompleteReport.generate(infos)
