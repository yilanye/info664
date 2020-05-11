import csv
import re

list_a = []
with open('the_oscar_award.csv', 'r') as oscar_file:
    parsed_csv = csv.reader(oscar_file)

    for row in parsed_csv:
        # print str(row[1])
        if row[1] > str('2010'):
            if row[6] == 'True':
                m2020 = row[1] + ", " + row[3] + ", " + row [5]

                if m2020 not in list_a:
                    print (m2020)

                    list_a.append(m2020)


    print(list_a)
