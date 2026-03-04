# step 1 old adapter interface
class OldPrinter:
    def print_text(self, text):
        print(f"Old Printer: {text}")

# step 2 target interface
class Printer:
    def print_data(self, text):
        pass

# step3 adapter class

class PrinterAdapter(Printer):
    def __init__(self, old_printer):
        self._old_printer = old_printer

    def print_data(self, text):
        self._old_printer.print_text(text)

# step 4 use the adapter
if __name__ == "__main__":
    old_printer = OldPrinter()
    old_printer.print_text("Hello, Old Printer!")
    adapter = PrinterAdapter(old_printer)

    adapter.print_data("Hello, Adapter Pattern!")

# output:
# Old Printer: Hello, Old Printer!
# Old Printer: Hello, Adapter Pattern!