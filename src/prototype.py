#Ellen Buckingham, prototype.py for Inventory_sales_tracker.

#Prototype for Week 2
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

#Prototype for Week 3
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
print(f"{product1_SKU} | {product1_name} | ${product1_unit_price:.2f} | {product1_quantity}")
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
