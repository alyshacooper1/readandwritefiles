import csv

customers = open('customers.csv', 'r')

outfile = open('customer_country.csv','w')

csv_file = csv.reader(customers)

next(csv_file)


for record in csv_file:
    outfile.write(record[1] + ' ' + record[2] + ' ,' + record[4] + '\n')
    print(record) 
    

outfile.close()
