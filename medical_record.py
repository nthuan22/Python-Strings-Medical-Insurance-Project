medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here

#Print medical_data to see the output in the terminal
print(medical_data)

#Replace all instances of # in medical_data with $.
updated_medical_data = medical_data.replace('#', '$')
print(updated_medical_data)

#Create a variable called num_records and initialize it at 0.
num_records = 0

#write a for loop to iterate through the updated_medical_data string. 
for data in updated_medical_data:
  if data == "$":
    num_records += 1

#Outside of the loop, print num_records with the message
print("There are " + str(num_records) + " medical redords in the data.")

#Store the result in a variable called medical_data_split and print this variable.
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

#define an empty list called medical_records
medical_records = []

#Next, iterate through medical_data_split and for each record, split the string after each comma (,) and append the split string to medical_records.Print medical_records after the loop.
for record in medical_data_split:
  medical_records.append(record.split(","))

print(medical_records)

#creating an empty list called medical_records_clean
medical_records_clean = []

#create an empty list called record_clean
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

#Print medical_records_clean outside of the for loops to see the output
print(medical_records_clean)


#Our data is now clean and ready for analysis.
for record in medical_records_clean:
  print(record[0].upper())

#Let’s store each name, age, BMI, and insurance cost in separate lists.
names = []
ages = []
bmis = []
insurance_costs = []

#Next, iterate through medical_records_clean and for each record
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])


#Print names, ages, bmis, and insurance_costs outside of the loop
print(names)
print(ages)
print(bmis)
print(insurance_costs)

#Let’s calculate the average BMI in our dataset.
total_bmi = 0

#use a for loop to iterate through bmis and add each bmi to total_bmi
for bmi in bmis:
  total_bmi += float(bmi)


#After the for loop, create a variable called average_bmi that stores the total_bmi divided by the length of the bmis list
average_bmi = total_bmi / len(bmis)
print("Average BMI: " + str(average_bmi))




