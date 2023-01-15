from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" in path:
            return Inventory.generate_xml(path)
        else:
            raise ValueError("Arquivo inválido")
