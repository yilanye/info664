import csv
import re

# list_a = []
# with open('the_oscar_award.csv', 'r') as oscar_file:
#     parsed_csv = csv.reader(oscar_file)
#
#     for row in parsed_csv:
#         # print str(row[1])
#         if row[1] > str('2000'):
#             if row[6] == 'True':
#                 m2020 = row[1] + ", " + row[3] + ", " + row [5]
#
#                 if m2020 not in list_a:
#                     print (m2020)
#
#                     list_a.append(m2020)
#
#
#     print(list_a)

list_new = []
with open('OSCAR - 2010-2020ID.csv', 'r') as new_file:
    new_csv = csv.reader(new_file)

    for row in new_csv:
        # print(row[1])

        # if "Drama" in row['Genre']:
        #     list_new.append(row)
        #
        #     print(row)


        # if row[1] == 'BEST PICTURE':
        #     # print (row)
        #     list_new.append(row)

        if row[1] == 'ACTOR IN A SUPPORTING ROLE':
            print(row[1])

            list_new.append(row)

        if row[1] == 'ACTRESS IN A SUPPORTING ROLE':
            print(row[1])

            list_new.append(row)

        if row[1] == 'ACTOR IN A LEADING ROLE':
            print(row[1])

            list_new.append(row)

        if row[1] == 'ACTOR IN A SUPPORTING ROLE':
            print(row[1])

            list_new.append(row)

    print(list_new)



with open('oscar_acting.csv', mode='w') as csv_file:
    fieldnames = ['Year', 'Category', 'Film', "IMDB_ID"]

    writer = csv.writer(csv_file)
    writer.writerow (fieldnames)
    writer.writerows(list_new)


# list_true = []
#     for row in parsed_csv:
#         # print str(row[1])
#         if row[2] =='ACTOR IN A LEADING ROLE':
#             if row[6] == 'True':
#                 actor = row[1] + " " + row[3] + " " + row [5]
#
#                 if actor not in list_a:
#                     print (actor)
#
#                     list_a.append(actor)


# compile_year = re.compile(r'[2]+[0]+[0-2]+[0-9]')
    #
    # for row in parsed_csv:
    #     if row[0] == 'year_film':
    #         continue
    #
    #     result = compile_year.findall(row[0])
    #
    #     if len(result) > 0:
    #         if 'True' in row[6]:
    #     # year = int(row[0])
    #     # if year > 2000 and 'True' in row[6]:
    #             print (row)


    # movies = {'2020': [m2020],
    #     '2019': [m2019]
    #     }
