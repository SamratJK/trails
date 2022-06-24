import csv
a = [[('Note', 7), ('added', 7), ('Services', 4), ('Department', 3), ('211', 2), ('VIRGINIA', 2), ('service', 2), ('Virginia', 2), ('Social', 2), ('provided', 2)], [('Note added', 7), ('211 VIRGINIA', 2), ('VIRGINIA service', 2), ('service Virginia', 2), ('Virginia Department', 2), ('Department Social', 2), ('Social Services', 2), ('Services provided', 2), ('provided partnership', 2), ('partnership Council', 2)], [('211 VIRGINIA service', 2), ('VIRGINIA service Virginia', 2), ('service Virginia Department', 2), ('Virginia Department Social', 2), ('Department Social Services', 2), ('Social Services provided', 2), ('Services provided partnership', 2), ('provided partnership Council', 2), ('Travel Tourism Site', 1), ('Tourism Site Vermont', 1)]]

with open('test.csv','w') as write_file:
    file_writer = csv.writer(write_file,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in a:
        for j in i:
            file_writer.writerow(j)