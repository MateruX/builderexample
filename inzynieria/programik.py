## Klasa reprezentująca komputer
#  Umożliwia konfigurację komponentów komputera
class Computer:
    def __init__(self):
        ## Słownik przechowujący komponenty komputera
        self.components = {}

    ## Dodaje komponent do komputera
    #  @param key Nazwa komponentu
    #  @param value Wartość/specyfikacja komponentu
    def add_component(self, key, value):
        self.components[key] = value

    def __str__(self):
        return '\n'.join(f'{key}: {value}' for key, value in self.components.items())

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_component(self, component_type, options):
        print(f"Choose {component_type}:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("4. Enter your own specification.")

        choice = input("Enter your choice (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            selection = options[int(choice) - 1]
        elif choice == '4':
            selection = input("Enter your specification: ")
        else:
            print("Invalid input, defaulting to first option.")
            selection = options[0]

        self.computer.add_component(component_type, selection)

    def build(self):
        return self.computer

def main():
    builder = ComputerBuilder()
    cpu_options = ['Intel i9', 'AMD Ryzen 9', 'Intel i7']
    ram_options = ['16GB DDR4', '32GB DDR4', '64GB DDR4']
    storage_options = ['1TB SSD', '2TB HDD', '512GB NVMe SSD']
    graphics_options = ['NVIDIA RTX 3080', 'AMD Radeon RX 6800', 'NVIDIA GTX 1660']
    motherboard_options = ['ASUS ROG X570', 'MSI MAG B550 TOMAHAWK', 'Gigabyte Z390 AORUS']
    power_supply_options = ['650W Corsair', '850W Thermaltake', '750W EVGA']

    builder.add_component('CPU', cpu_options)
    builder.add_component('RAM', ram_options)
    builder.add_component('Storage', storage_options)
    builder.add_component('Graphics Card', graphics_options)
    builder.add_component('Motherboard', motherboard_options)
    builder.add_component('Power Supply', power_supply_options)

    custom_computer = builder.build()
    print("\nYour custom computer configuration:")
    print(custom_computer)

if __name__ == "__main__":
    main()
