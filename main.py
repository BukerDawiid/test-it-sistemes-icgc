# nom i cognoms: David Rescalvo Rius

import csv
from decimal import Decimal

def read_file(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_file(path, data):
    if not data:
        return

    fieldnames = list(data[0].keys())

    with open(path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

"""
Tasca 1

Actualment `orders.csv` no conté el total del cost de la comanda.

Necessitem utilitzar les dades d’aquests fitxers per generar el fitxer `order_prices.csv` amb les següents columnes:
* `id` número d'identificació de la comanda
* `euros` cost total en euros de la comanda
"""

# Guarda els preus i els IDs dels productes en un diccionari, per cada comanda
# mira els prodctes que hi ha, suma el total dels productes i afegeix a la llista
# l'ID de la comanda i el total, que finalment s'escriu en un fitxer.

def task_one(orders_path, products_path, orders_output_path):
    orders = read_file(orders_path)
    products = read_file(products_path)

    product_prices = {}
    for product in products:
        product_prices[product["id"]] = Decimal(product["cost"])

    orders_prices = []
    for order in orders:
        total = Decimal("0.00")
        for product_id in order["products"].split():
            total += product_prices[product_id]

        orders_prices.append({
            "id": order["id"],
            "euros": total.to_eng_string()
        })

    write_file(orders_output_path, orders_prices)
    return

"""
Tasca 2

El departament de màrqueting vol saber quins clients tenen interès en cada producte. Ens han demanat el fitxer `product_customers.csv` que, per a cada producte, contingui un llistat dels clients que l’han comprat: 
* `id` número d'identificació del producte
* `customer_ids` llistat separat per espais amb els identificadors dels clients que han comprat el producte
"""

# s'utilitza un diccionari auxiliar amb els ID dels productes, relaciona els productes
# de cada comanda amb els compradors evitant duplicats i ho guarda en un fitxer. 

def task_two(orders_path, products_path, product_customers_path):
    orders = read_file(orders_path)
    products = read_file(products_path)

    aux_customers = {}
    for product in products:
        aux_customers[product["id"]] = []

    for order in orders:
        customer_id = order["customer"]
        for product_id in order["products"].split():
            if customer_id not in aux_customers[product_id]:
                aux_customers[product_id].append(customer_id)

    product_customers = []
    for product in products:
        product_customers.append({
            "id": product["id"],
            "customer_ids": " ".join(aux_customers[product["id"]])
        })

    write_file(product_customers_path, product_customers)
    return

"""
Tasca 3

Per tal d’avaluar els nostres clients, necessitem el fitxer `customer_ranking.csv`, que conté les següents columnes, ordenades de forma descendent pel camp `total_euros`:
* `id` número d'identificació del client
* `firstname` nom del client
* `lastname` cognom del client
* `total_euros` total en euros que aquest client ha gastat en productes
"""

# He interpretat que les tasques s'han d'executar seqüencialment, per lo que
# hi ha una dependència directa entre la tasca 1 i la 3: la tasca 3 utilitza
# el fitxer resultant de la 1.

# Es creuen les dades de compradors amb el total gastat utilitzant el fitxer 
# order_prices.csv i s'ordena per la clau total_euros.

def task_three(orders_path, customers_path, order_price_path, customer_ranking_path):
    orders = read_file(orders_path)
    customers = read_file(customers_path)
    order_prices = read_file(order_price_path)

    aux_prices = {}
    for op in order_prices:
        aux_prices[op["id"]] = Decimal(op["euros"])

    aux_totals = {}
    for customer in customers:
        aux_totals[customer["id"]] = Decimal("0.00")

    for order in orders:
        aux_totals[order["customer"]] += aux_prices[order["id"]]

    customer_ranking = []
    for customer in customers:
        customer_ranking.append({
            "id": customer["id"],
            "firstname": customer["firstname"],
            "lastname": customer["lastname"],
            "total_euros": aux_totals[customer["id"]].to_eng_string()
        })

    customer_ranking.sort(key=lambda x: Decimal(x["total_euros"]), reverse=True)
    write_file(customer_ranking_path, customer_ranking)
    return


def main():
    task_one("orders.csv", "products.csv", "order_prices.csv")
    task_two("orders.csv", "products.csv", "product_customers.csv")
    task_three("orders.csv", "customers.csv", "order_prices.csv", "customer_ranking.csv")


if __name__ == "__main__":
    main()