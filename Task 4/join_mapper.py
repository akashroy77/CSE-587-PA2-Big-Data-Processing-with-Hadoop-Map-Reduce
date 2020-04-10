#!/usr/bin/env python3
import sys

input_string=""
employee_id_first_table=[]
employee_id_second_table=[]
employee_id_second_table.append("EmployeeID")
name_first_table=[]
salary=[]
salary.append("Salary")
country=[]
country.append("Country")
passcode=[]
passcode.append("Passcode")
for line in sys.stdin:
	total_name=''
	total_country_name=''
	line=line.strip()
	line=line.replace(","," ")
	data=line.split(" ")
	if(len(data)>4):
		first_id=data[0]+data[1]
		employee_id_second_table.append(first_id)
		total_salary=data[2]+data[3]
		salary.append(total_salary)
		for i in range(4,len(data)-1):
			total_country_name+=data[i]+" "
		country.append(total_country_name)
		passcode.append(data[-1])	
	else:
		second_id=data[0]+data[1]
		employee_id_first_table.append(second_id)
		for i in range(2,len(data)):
			total_name+=data[i]+" "
		name_first_table.append(total_name)
for i in range(len(employee_id_first_table)):
	print(employee_id_first_table[i]+" "+name_first_table[i]+"\n")
for i in range(len(employee_id_second_table)):
	print(employee_id_second_table[i]+" "+salary[i]+" "+country[i]+" "+passcode[i]+"\n")
	
