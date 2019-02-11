#sales_reporter.py
# goal output:
    #SALES REPORT (MARCH 2018)
    #TOTAL SALES: $12,000.71
    #TOP SELLING PRODUCTS:
        #1. Button-Down Shirt: $6,960.35
        #2. Super Soft Hoodie: $1,875.00
        #3. etc.

#source adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_solution_further.py

import operator #need this for line 57
import os   
import csv
import pandas
import matplotlib.pyplot as plt

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

#
# INFO INPUTS
#

csv_filename = "sales-201710.csv" #TODO allow user to specify (WITH FILEPATH!)

#csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename) #use this to adapt a file in the data directory
    # ^ use for project
csv_data = pandas.read_csv(csv_filename) #read csv into panda dataframe

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

#get unique products
product_names = csv_data["product"]
#print(product_names)
#print(type(product_names)) > this is a series
unique_product_names = product_names.unique()
#print(type(unique_product_names))
unique_product_names = unique_product_names.tolist() #convert to list because NOT a list

#accumulate total sales per product

top_sellers = []

for product_name in unique_product_names:
    matching_rows = csv_data[csv_data["product"] == product_name] #define matching_rows as any duplicate
    product_monthly_sales = matching_rows["sales price"].sum()
    #now adding in product name and monthly sales
    top_sellers.append(
        {"name": product_name, "monthly_sales": product_monthly_sales})
    #print(top_sellers)

top_sellers = sorted(top_sellers, key=operator.itemgetter(
    "monthly_sales"), reverse=True)
#print(top_sellers)

#
# OUTPUTS
#

print("-----------------------")
print("MONTH: March 2018")  # TODO: get month and year

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

rank = 1
for d in top_sellers:
    print("  " + str(rank) + ") " +
          d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")

chart_title = "Top Selling Products (March 2018)"  # TODO: get month and year

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

plt.bar(sorted_products, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")
plt.show()
