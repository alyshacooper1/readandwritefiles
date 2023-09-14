import csv
customer = open('sales.csv', 'r')
sales_file = csv.reader(customer)
report = open('salesreport.csv','w')

next(sales_file)
customer_id = 250
total = 0

report.write(f"Customer ID, Total\n")

for line in sales_file:
    subtotal = float(line[3])
    taxant = float(line[4])
    freight = float(line[5])

    if customer_id == int(line[0]):
        total += subtotal + taxant + freight 

    else:
        report.write(f"{customer_id}, {total:.2f}\n")
        total = round(total,2)

        customer_id = int(line[0])
        total = subtotal + taxant + freight

total = round(total,2)
report.write(f"{customer_id},{total:.2f}\n")
customer.close()
report.close()
    

