#!/usr/bin/env python3
import sys

input_string=""
employee_id_first_table=[]
employee_id_second_table=[]
name_first_table=[]
salary=[]
country=[]
passcode=[]
join_table=[]
for line in sys.stdin:
	total_name=''
	total_country_name=''
	line=line.strip()
	if(line!=""):
		data=line.split(" ")
		if(len(data)<=3):
			second_id=data[0]
			employee_id_first_table.append(second_id)
			for i in range(1,len(data)):
				total_name+=data[i]+" "
			name_first_table.append(total_name)
		else:
			first_id=data[0]
			employee_id_second_table.append(first_id)
			total_salary=data[1]
			salary.append(total_salary)
			for i in range(2,len(data)-1):
				total_country_name+=data[i]+" "
			country.append(total_country_name)
			passcode.append(data[-1])	
for i in range(1,len(employee_id_first_table)):
	if(employee_id_first_table[i] in employee_id_second_table):
		index=employee_id_second_table.index(employee_id_first_table[i])
		row=employee_id_second_table[index]+" "+name_first_table[i]+" "+salary[index]+" "+country[index]+" "+passcode[index]+" "
		join_table.append(row)
for i in range(len(join_table)):
	print(join_table[i])