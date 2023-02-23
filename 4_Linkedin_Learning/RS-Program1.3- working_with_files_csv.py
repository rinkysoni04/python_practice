import csv

#Reading:

with open("working_with_files_example_csv_doc.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    # next(reader)    #Deleted first row from current file & goes on.
    for row in reader:
        print(row)

print()



#Convert data into list:

with open("working_with_files_example_csv_doc.csv", "r") as f:
    reader1 = list(csv.reader(f, delimiter = ","))
    for row in reader1[1:]:   #We can choose which row to skip using list index as reader1 converted to list
        print(row)

print()



#Convert into dictionary:

with open("working_with_files_example_csv_doc.csv", "r") as f:
    reader2 = csv.DictReader(f, delimiter = ",")  #DictReader creates data in dictionary format. First row converted to key.
    for row in reader2:
        print(row)

print()



#Working with file by doing some operations:

with open("working_with_files_example_csv_doc.csv", "r") as f:
    data = list(csv.DictReader(f, delimiter = ","))
    data = [row for row in data if row['Country'] == 'India']
    #print(len(data))

print()



# Writing:

with open("working_with_files_example_csv_writing.csv", "w") as f:
    writer = csv.writer(f, delimiter = ",")
    for row in data:
        writer.writerow([row['Name'], row['Country']])

print()













