#sales_reporter.py
# goal output
    #SALES REPORT (MARCH 2018)
    #TOTAL SALES: $12,000.71
    #TOP SELLING PRODUCTS:
        #1. Button-Down Shirt: $6,960.35
        #2. Super Soft Hoodie: $1,875.00
        #3. etc.

#print("SALES REPORT (MONTH YEAR)")

import os
import csv
import pandas as pd


#
# INFO INPUTS
#

csv_filename = "sales-201710.csv"
data = pd.read_csv(csv_filename)

print(data)