from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" in path:
            return Inventory.generate_csv(path)
        else:
            raise ValueError("Arquivo inválido")
