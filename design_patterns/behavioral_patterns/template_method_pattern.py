from abc import ABC, abstractmethod


# -----------------------------
# Abstract Template
# -----------------------------
class DataImporter(ABC):

    def process(self) -> None:
        """Template Method (fixed algorithm)"""
        self.read_data()
        self.validate_data()
        self.save_data()
        self.after_save_hook()

    @abstractmethod
    def read_data(self) -> None:
        pass

    def validate_data(self) -> None:
        print("✅ Validating data")

    @abstractmethod
    def save_data(self) -> None:
        pass

    def after_save_hook(self) -> None:
        """Optional hook"""
        pass


# -----------------------------
# Concrete Implementations
# -----------------------------
class CSVImporter(DataImporter):
    def read_data(self) -> None:
        print("📄 Reading CSV file")

    def save_data(self) -> None:
        print("💾 Saving CSV data to database")

    def after_save_hook(self) -> None:
        print("📧 Sending CSV import email")


class JSONImporter(DataImporter):
    def read_data(self) -> None:
        print("📄 Reading JSON file")

    def save_data(self) -> None:
        print("💾 Saving JSON data to database")


# -----------------------------
# Client Code
# -----------------------------
def main():
    print("\n--- CSV Import ---")
    csv_importer = CSVImporter()
    csv_importer.process()

    print("\n--- JSON Import ---")
    json_importer = JSONImporter()
    json_importer.process()


if __name__ == "__main__":
    main()
