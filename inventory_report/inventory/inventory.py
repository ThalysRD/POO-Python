from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
# import xml


class Inventory:
    def __init__(self, path, type):
        self.path = path
        self.type = type

    @staticmethod
    def import_data(path, type):
        infos = ''
        if "csv" in path:
            infos = Inventory.generate_csv(path)
        if "json" in path:
            infos = Inventory.generate_json(path)
        if "xml" in path:
            infos = Inventory.generate_xml(path)
        if type == "simples":
            return SimpleReport.generate(infos)
        else:
            return CompleteReport.generate(infos)

    def generate_csv(path):
        infos = []
        with open(path, 'r') as file:
            reports = csv.DictReader(file)
            for report in reports:
                infos.append(report)
        return infos

    def generate_json(path):
        infos = []
        with open(path, 'r') as file:
            reports = json.load(file)
            for report in reports:
                infos.append(report)
        return infos

    def generate_xml(path):
        # infos = []
        pass
