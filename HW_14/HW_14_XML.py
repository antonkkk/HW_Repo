# 6. XML
import xml.etree.ElementTree as ET
import os


def calculate_total_cost(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        total_cost = 0

        for product in root.findall('product'):
            price = float(product.find('price').text)
            quantity = int(product.find('quantity').text)
            total_cost += price * quantity

        return total_cost
    except FileNotFoundError:
        print(f"Ошибка: Файл '{xml_file}' не найден.")
        return None
    except ET.ParseError:
        print(f"Ошибка: Файл '{xml_file}' имеет неверный формат XML.")
        return None


if __name__ == "__main__":
    print("Текущая рабочая директория:", os.getcwd())

    xml_file = 'products.xml'

    total_cost = calculate_total_cost(xml_file)
    if total_cost is not None:
        print(f"Общая стоимость всех товаров: {total_cost}")
