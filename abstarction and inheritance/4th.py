class Laptop:
    def __init__(self, brand, model, ram, storage):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")  # Corrected here

# Example usage:
laptop = Laptop("Dell", "XPS 13", 16, 512)
laptop.display_details()