#Ellen Buckingham, prototype.py for Inventory_sales_tracker.
#The purpose of this file is to store one product's information and then calculate and display its subtotal.

#store product's information
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
