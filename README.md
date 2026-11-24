# Inventory and Sales Tracker

### Ellen Buckingham, COSC 240

This project is a command-line Python application for a small store. 

A user will be able to manage products, restock inventory, record sales, prevent invalid transactions, save and reload data, and view useful reports.

### **_Store Scenario:_**

For my project, the store will be a small coffee shop that sells various beverages and bakery items. Some of the menu items are drip coffee, lattes, sparkling refreshers, bagels, and scones. 

### **_Individual Work Plan:_**

I will work on this project through the semester, building my Python application in incremental steps, running tests and making meaningful commits as I go.

### **_Expected Actions:_**

Once completed, the application is expected to add products, find products using SKU, restock products, record shop sales, and display the shop's inventory information. The application will also prevent invalid actions such as duplicate SKUs, negative inventory, invalid prices, and sales exceeding the available quantity.

### **_Definition of Done:_**

My project will be considered done when it includes all required tests and my application can perform the expected actions without any problems.

### **_Weekly Progress:_**

_**Week 2**_ — This week, I created the repository with the scr, tests, and data folders. I created a .gitignore and README.md with a project charter. I also created prototype.py. In prototype.py, I stored one product name, price, and quantity and and calculated a subtotal. _**Acceptance Check**_: The repository can be successfully accessed and the prototype run by every member.

---

_**Week 3**_ – This week, I defined the product fields: SKU, name, category, unit price, quantity, low-stock threshold, and active status. I created three synthetic product records for "Latte", "Drip Coffee", and "Blueberry Scone". Expected Inventory Line for Latte: "DRK001 | Latte | $3.00 | Qty: 2". Expected sales receipt line for Latte: "Subtotal: $3.00 x 2 = $6.00". State Trace for one sale and restock: "The initial inventory was 2 lattes. After restocking 5 lattes, the quantity increased to 7. Then, 2 lattes were then sold, leaving 5 lattes in stock." _**Acceptance Check**_: The prototype for this week calculates subtotal and remaining quantity correctly.

---

_**Week 4**_- This week, I added multiple validations to my prototype and saved a test file to my tests folder. I implemented validations for nonempty SKU/name/category, positive price, nonnegative inventory, and positive transaction quantity. I rejected duplicate SKU and sales exceeding available product quantity. I ensured the rejection actions left product information unchanged. _**Acceptance Check**_: I performed and recorded tests for a valid sale, duplicate SKU, blank name, and oversell attempt. I saved the test file to my test folder.

---

_**Week 5**_- This week, I wrote the following pseudocode for various workflows: 

***Add Product:***

Validate that new SKU is not a duplicate, no product information is left empty, price is positive, quantity is nonnegative. Raise ValueError if any of the validation requirements are not met. After validation, store the new product’s information.
Can be broken up into functions like validate_product(), find_by_SKU(), add_product()

***Restock a Product:***

Validate that restock quantity is not negative. Identify the correct product being restocked. Add the restock quantity to the existing product quantity. Return the quantity before and after restocking.
Broken up into functions like find_by_SKU(), validate_quantity(), restock_product()

***Record Sale:***

Identify the product being sold. Validate that the product exists and is active, that the amount being sold is a positive number, that the sale will not result in an oversale. After validation, calculate the subtotal for the sale. Subtract the amount sold from the product quantity. Display the sales receipt and return the subtotal.
Broken up into functions like find_by_SKU(), validate_quantity(), record_sale()

***Inventory report workflows:***

Retrieve products from the current inventory list. Display the SKU, name, category, price, quantity, and active status. Compare product quantities with their low-stock threshold. Display products that need restocked.
Broken up into functions like generate_report(), check_low_stock(), display_report()

**Testing Order**

1. Create and test find_by_SKU() to locate products using their SKU.
2. Create and test validate_product() and validate_quantity() to check product information and transaction quantities.
3. Create and test add_product() to add valid products and reject duplicates.
4. Create and test restock_product() to update inventory quantities.
5. Create and test record_sale() to process sales and prevent overselling.
6. Create and test check_low_stock() to identify products that need restocking.
7. Create and test generate_report() and display_report() to produce the inventory report.

In addition to the pseudocode for workflows, I also created the following menu mock-up:

***Menu Mock-Up***

The following menu will display when the program starts:

1. Product Management
2. Sale Transaction
3. Inventory Report

Enter your choice (1-3):

---
