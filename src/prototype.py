#Ellen Buckingham, prototype.py for Inventory_sales_tracker.

##Prototype for Week 2
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

##Prototype for Week 3
#Store 3 product's information

#product1 information
product1_SKU = "DRK001"
product1_name = "Latte"
product1_category = "Drink"
product1_unit_price = 3.00
product1_quantity = 2
product1_low_stock_threshold = 3
product1_active_status = True
#product2 information
product2_SKU = "DRK002"
product2_name = "Drip Coffee"
product2_category = "Drink"
product2_unit_price = 2.00
product2_quantity = 20
product2_low_stock_threshold = 5
product2_active_status = True
#product3 information
product3_SKU = "FD001"
product3_name = "Blueberry Scone"
product3_category = "Food"
product3_unit_price = 3.00
product3_quantity = 8
product3_low_stock_threshold = 2
product3_active_status = True

#Display an Inventory Line
print("Inventory for Product 1:")
print(f"{product1_SKU} | {product1_name} | ${product1_unit_price:.2f} | Qty: {product1_quantity}")
print("------------------------")
#Restock one item
print(f"Quantity Before Restock: {product1_quantity}")
print("Amount to Restock: 5")
product1_quantity = product1_quantity + 5
print(f"Latte Quantity after Restock: {product1_quantity}")
print("------------------------")
#Sell one item
sell_quantity = 2
subtotal = product1_unit_price * sell_quantity
product1_quantity = product1_quantity - sell_quantity
#Display Subtotal
print("Sale")
print(f"Item Sold: {product1_name}")
print(f"Unit Price: ${product1_unit_price:.2f}")
print(f"Quantity Sold: {sell_quantity}")
print(f"Subtotal: ${product1_unit_price:.2f} x {sell_quantity} = ${subtotal:.2f}")
print(f"Remaining Latte Quantity: {product1_quantity}")

##Prototype for Week 4

#product1 information
product1_SKU = "DRK001"
product1_name = "Latte"
product1_category = "Drink"
product1_unit_price = 3.00
product1_quantity = 2
product1_low_stock_threshold = 3
product1_active_status = True

#product2 information
product2_SKU = "DRK002"
product2_name = "Drip Coffee"
product2_category = "Drink"
product2_unit_price = 2.00
product2_quantity = 20
product2_low_stock_threshold = 5
product2_active_status = True

#product3 information
product3_SKU = "FD001"
product3_name = "Blueberry Scone"
product3_category = "Food"
product3_unit_price = 3.00
product3_quantity = 8
product3_low_stock_threshold = 2
product3_active_status = True

#Display an Inventory Line
print("Inventory for Product 1:")
print(f"{product1_SKU} | {product1_name} | ${product1_unit_price:.2f} | Qty: {product1_quantity}")
print("------------------------")

#Restock one item
print(f"Quantity Before Restock: {product1_quantity}")
print("Amount to Restock: 0")
product1_quantity = product1_quantity + 0
print(f"Latte Quantity after Restock: {product1_quantity}")
print("------------------------")

    #Sell one item
sell_quantity = int(input("Please enter a sell quantity: "))
subtotal = product1_unit_price * sell_quantity
if sell_quantity > product1_quantity:
    print(f"Error: Sale larger than available quantity")
else:
    product1_quantity = product1_quantity - sell_quantity
    #Display Subtotal
    print("Sale")
    print(f"Item Sold: {product1_name}")
    print(f"Unit Price: ${product1_unit_price:.2f}")
    print(f"Quantity Sold: {sell_quantity}")
    print(f"Subtotal: ${product1_unit_price:.2f} x {sell_quantity} = ${subtotal:.2f}")
    print(f"Remaining Latte Quantity: {product1_quantity}")

#Add a new product
new_productSKU= input("Please input a new SKU:")
if new_productSKU == "":
    print("Error: Empty SKU")
elif new_productSKU == product1_SKU or new_productSKU == product2_SKU or new_productSKU==product3_SKU:
    print("Error: Duplicate SKU")
else:
    new_productSKU = new_productSKU
    print(f"New SKU: {new_productSKU}")
new_productName= input("Please input a new product name:")
if new_productName == "":
    print("Error: Empty Name")
else:
    new_productName = new_productName
    print(f"New Name: {new_productName}")
new_productCategory= input("Please input a new product category:")
if new_productCategory == "":
    print("Error: Empty Category")
else:
    new_productCategory = new_productCategory
    print(f"New Category: {new_productCategory}")
new_productUnitPrice= int(input("Please input a new unit price:"))
if new_productUnitPrice <= 0:
    print("Error: Unit Price Must Be Positive")
else:
    new_productUnitPrice = new_productUnitPrice
    print(f"New Unit Price: {new_productUnitPrice}")
new_productQuantity= int(input("Please input a new quantity:"))
if new_productQuantity < 0:
    print("Error: Quantity Must Be Nonnegative")
else:
    new_productQuantity = new_productQuantity
    print(f"New Quantity: {new_productQuantity}")

##Repeating Command Line Menu for Week 6
#Store product information
products = [
    {
        "sku": "DRK001",
        "name": "Latte",
        "category": "Drink",
        "unit_price": 3.00,
        "quantity": 2,
        "low_stock_threshold": 3,
        "active_status": True
    },
    {
        "sku": "DRK002",
        "name": "Drip Coffee",
        "category": "Drink",
        "unit_price": 2.00,
        "quantity": 20,
        "low_stock_threshold": 5,
        "active_status": True
    },
    {
        "sku": "FD001",
        "name": "Blueberry Scone",
        "category": "Food",
        "unit_price": 3.00,
        "quantity": 8,
        "low_stock_threshold": 2,
        "active_status": True
    }
]
#Function for find by SKU
def find_by_SKU(sku):
    for product in products:
        if product["sku"] == sku:
            return product
    return None
#Function for product validation
def validate_product(sku, name, category, price, quantity):
    if sku == "":
        raise ValueError("SKU cannot be empty")
    if find_by_SKU(sku) is not None:
        raise ValueError("Duplicate SKU")
    if name == "":
        raise ValueError("Product name cannot be empty")
    if category == "":
        raise ValueError("Category cannot be empty")
    if price <= 0:
        raise ValueError("Price must be positive")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    return True
#Function for quantity validation
def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return True
#Function for adding product
def add_product():
    try:
        sku = input("Enter new SKU: ")
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity: "))
        validate_product(sku, name, category, price, quantity)
        new_product = {
            "sku": sku,
            "name": name,
            "category": category,
            "unit_price": price,
            "quantity": quantity,
            "low_stock_threshold": 3,
            "active_status": True
        }
        products.append(new_product)
        print("Product successfully added!")
        return new_product
    except ValueError as error:
        print(f"Error: {error}")
        return None
#Function for restocking
def restock_product():
    try:
        sku = input("Enter SKU to restock: ")
        product = find_by_SKU(sku)
        if product is None:
            raise ValueError("Product not found")
        quantity_before = product["quantity"]
        amount = int(input("Enter restock quantity: "))
        if amount < 0:
            raise ValueError("Restock quantity cannot be negative")
        product["quantity"] += amount
        quantity_after = product["quantity"]
        print(f"Quantity before restock: {quantity_before}")
        print(f"Quantity after restock: {quantity_after}")
        return quantity_before, quantity_after
    except ValueError as error:
        print(f"Error: {error}")
        return None
#Function for recording sale
def record_sale():
    try:
        sku = input("Enter SKU to sell: ")
        product = find_by_SKU(sku)
        if product is None:
            raise ValueError("Product not found")
        if not product["active_status"]:
            raise ValueError("Product is inactive")
        sell_quantity = int(input("Enter quantity to sell: "))
        validate_quantity(sell_quantity)
        if sell_quantity > product["quantity"]:
            raise ValueError("Sale exceeds available inventory")
        subtotal = product["unit_price"] * sell_quantity
        product["quantity"] -= sell_quantity
        print("\n*** Sales Receipt ***")
        print(f"Product: {product['name']}")
        print(f"Unit Price: ${product['unit_price']:.2f}")
        print(f"Quantity Sold: {sell_quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Remaining Quantity: {product['quantity']}")
        return subtotal
    except ValueError as error:
        print(f"Error: {error}")
        return None
#Function for displaying inventory
def display_inventory():
    print("\n*** Inventory Report ***")
    print("------------------------------------------")
    for product in products:
        print(f"SKU: {product['sku']}")
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Unit Price: ${product['unit_price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Active Status: {product['active_status']}")
        print("------------------------------------------")
#Function for displaying menu
def display_menu():
    print("\n*** Menu Actions ***")
    print("1. Add Product")
    print("2. Find Product by SKU")
    print("3. Restock Product")
    print("4. Sale Transaction")
    print("5. Inventory Report")
    print("6. Exit")
#Function for repeating command line menu
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_product()
        elif choice == "2":
            sku = input("Enter SKU to find: ")
            product = find_by_SKU(sku)
            if product is not None:
                print("\nProduct Found:")
                print(f"SKU: {product['sku']}")
                print(f"Name: {product['name']}")
                print(f"Category: {product['category']}")
                print(f"Unit Price: ${product['unit_price']:.2f}")
                print(f"Quantity: {product['quantity']}")
            else:
                print("Product not found")
        elif choice == "3":
            restock_product()
        elif choice == "4":
            record_sale()
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            print("Exiting Program")
            break
        else:
            print("Invalid choice. Please try again.")
main()
