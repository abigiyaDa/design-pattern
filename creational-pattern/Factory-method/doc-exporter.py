#  product 

from abc import ABC, abstractmethod

class DocExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

# concrete products
class PDFExporter(DocExporter):
    def export(self, data):
        return f"Exporting data to PDF format: {data}"
class WordExporter(DocExporter):
    def export(self, data):
        return f"Exporting data to Word format: {data}"
class ExcelExporter(DocExporter):
    def export(self, data):
        return f"Exporting data to Excel format: {data}"
    
# creator class
class DocExporterFactory(ABC):
    @abstractmethod
    def create_exporter(self) -> DocExporter:
        pass
# concrete creators
class PDFExporterFactory(DocExporterFactory):
    def create_exporter(self) -> DocExporter:
        return PDFExporter()
class WordExporterFactory(DocExporterFactory):
    def create_exporter(self) -> DocExporter:
        return WordExporter()
class ExcelExporterFactory(DocExporterFactory):
    def create_exporter(self) -> DocExporter:
        return ExcelExporter()
    
# client code
def client_code(factory: DocExporterFactory, data):
    exporter = factory.create_exporter()
    print(exporter.export(data))

# testing the code
if __name__ == "__main__":
    data = "Sample data to export"
    
    print("Client: Testing PDF Exporter Factory:")
    client_code(PDFExporterFactory(), data)
    
    print("\nClient: Testing Word Exporter Factory:")
    client_code(WordExporterFactory(), data)

    print("\nClient: Testing Excel Exporter Factory:")
    client_code(ExcelExporterFactory(), data)