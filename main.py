from func import *

# Checks if pie Chart is present or not. If not, creates it
# Checks if file "Common Purchase Grocery.csv" is present or not, If not, creates it
if not (isFile("PieChart Most Purchased Groceries.jpg", True) and isFile("Common Purchase Grocery.csv")):
    groceryDataProcess()

