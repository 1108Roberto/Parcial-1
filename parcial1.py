import json
import os

DATA_FILE = 'budget_data.json'

# Cargar datos desde el archivo JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Guardar datos en el archivo JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Agregar un nuevo artículo
def add_item(name, amount):
    data = load_data()
    data.append({"name": name, "amount": amount})
    save_data(data)
    print(f"Artículo '{name}' agregado con éxito.")

# Buscar un artículo por nombre
def search_item(name):
    data = load_data()
    for item in data:
        if item["name"] == name:
            return item
    return None

# Editar un artículo existente
def edit_item(name, new_name, new_amount):
    data = load_data()
    for item in data:
        if item["name"] == name:
            item["name"] = new_name
            item["amount"] = new_amount
            save_data(data)
            print(f"Artículo '{name}' editado con éxito.")
            return
    print(f"Artículo '{name}' no encontrado.")

# Eliminar un artículo
def delete_item(name):
    data = load_data()
    data = [item for item in data if item["name"] != name]
    save_data(data)
    print(f"Artículo '{name}' eliminado con éxito.")

# Listar todos los artículos
def list_items():
    data = load_data()
    if data:
        for item in data:
            print(f"Nombre: {item['name']}, Monto: {item['amount']}")
    else:
        print("No hay artículos registrados.")

# Menú principal
def main():
    while True:
        print("\n--- Sistema de Registro de Presupuesto ---")
        print("1. Agregar artículo")
        print("2. Buscar artículo")
        print("3. Editar artículo")
        print("4. Eliminar artículo")
        print("5. Listar artículos")
        print("6. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            name = input("Nombre del artículo: ")
            amount = float(input("Monto del artículo: "))
            add_item(name, amount)
        elif choice == "2":
            name = input("Nombre del artículo a buscar: ")
            item = search_item(name)
            if item:
                print(f"Artículo encontrado: {item}")
            else:
                print(f"Artículo '{name}' no encontrado.")
        elif choice == "3":
            name = input("Nombre del artículo a editar: ")
            new_name = input("Nuevo nombre del artículo: ")
            new_amount = float(input("Nuevo monto del artículo: "))
            edit_item(name, new_name, new_amount)
        elif choice == "4":
            name = input("Nombre del artículo a eliminar: ")
            delete_item(name)
        elif choice == "5":
            list_items()
        elif choice == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
