#Ellen Buckingham, prototype.py for Inventory_sales_tracker.

#Week 2
#store the product's information
product_name = "Latte"
product_price = 3.00
product_quantity = 2

#calculate the subtotal
product_subtotal = product_price * product_quantity

#display the subtotal
print(f"Product Name: {product_name}")
print(f"Product Price: ${product_price:.2f}")
print(f"Product Quantity: {product_quantity}")
print(f"Product Subtotal: ${product_subtotal:.2f}")

#Week 3
#Store 3 product's information
products = [
    {
        "SKU": "DRK001",
        "Name": "Latte",
        "Category": "Drink",
        "Price": 3.00,
        "Quantity": 10,
        "Low_Stock_Threshold": 3,
        "Active": True
    },
    {
        "SKU": "DRK002",
        "Name": "Drip Coffee",
        "Category": "Drink",
        "Price": 2.00,
        "Quantity": 20,
        "Low_Stock_Threshold": 5,
        "Active": True
    },
    {
        "SKU": "FD001",
        "Name": "Blueberry Scone",
        "Category": "Pastry",
        "Price": 3.00,
        "Quantity": 8,
        "Low_Stock_Threshold": 2,
        "Active": True
    }
]
# Display inventory information for one product
def display_inventory(product):
    print(
        f"{product['SKU']} | {product['Name']} | "
        f"${product['Price']:.2f} | "
        f"Qty: {product['Quantity']}"
    )
# Restock a product
def restock_product(product, amount):
    if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
        raise ValueError("Restock amount must be a positive whole number.")
    product["Quantity"] += amount
# Record a sale and update inventory
def record_sale(product, amount):
    if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
        raise ValueError("Sale quantity must be a positive whole number.")
    if not product["Active"]:
        raise ValueError("Cannot sell an inactive product.")
    if amount > product["Quantity"]:
        raise ValueError("Not enough inventory to complete the sale.")
    subtotal = product["Price"] * amount
    product["Quantity"] -= amount
    print(
        f"Receipt: {product['Name']} x {amount} = "
        f"${subtotal:.2f}"
    )
    return subtotal
# Display initial inventory
print("INITIAL INVENTORY")
for product in products:
    display_inventory(product)
# Restock each product
print("\nRESTOCK TRACE")
restock_amounts = {
    "DRK001": 5,
    "DRK002": 10,
    "FD001": 4
}
for product in products:
    amount = restock_amounts[product["SKU"]]
    before = product["Quantity"]
    restock_product(product, amount)
    print(
        f"{product['Name']}: {before} + {amount} "
        f"= {product['Quantity']}"
    )
# Sell each product
print("\nSALES TRACE")
sale_amounts = {
    "DRK001": 3,
    "DRK002": 5,
    "FD001": 2
}
total_sales = 0.0
for product in products:
    amount = sale_amounts[product["SKU"]]
    before = product["Quantity"]
    subtotal = record_sale(product, amount)
    total_sales += subtotal
    print(
        f"Remaining {product['Name']}: "
        f"{before} - {amount} = {product['Quantity']}"
    )
# Display updated inventory
print("\nUPDATED INVENTORY")
for product in products:
    display_inventory(product)
# Display total sales
print(f"\nTotal sales: ${total_sales:.2f}")
