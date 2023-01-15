from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" in path:
            return Inventory.generate_json(path)
        else:
            raise ValueError("Arquivo inválido")
