import csv
employee = open('EmployeePay.csv', 'r')

csv_file = csv.reader(employee)

next(csv_file)

for record in csv_file:
    salary = int(record[3])
    bonus_rate = float(record[4])
    bonus = (salary * bonus_rate)
    pay = (salary + bonus)
    
print(f'First Name: {record[1]}')
print(f'Last  Name: {record[2]}')
print(f'Salary:\t${salary:10,.2f}')
print(f'Bonus:\t${bonus: 10,.2f}')
print(f'Pay:\t${pay:10,.2f}')

input()