# """Generate sales report showing total melons each salesperson sold."""

# #create an empty list to hold names of salespeople
# salespeople = []

# #create an empty list to hold number of melons sold
# melons_sold = []

# #create a file object for sales-report.txt
# f = open('sales-report.txt')

# #iterate through lines in our file
# for line in f:
#     #clean our data, stripping whitespace and splitting on |
#     line = line.rstrip()
#     entries = line.split('|')
    
#     #grabbing salesperson name
#     salesperson = entries[0]
#     #grabbing the integer value for melons sold
#     melons = int(entries[2])

#     #setting a condition to check if the name is already in the list
#     if salesperson in salespeople:
#         #if the name is in the list, we want to grab the index position of their name
#         position = salespeople.index(salesperson)
#         #increment the number of melons they sold at their index position
#         melons_sold[position] += melons

#     #else make a new entry to our parallel lists    
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# #using the data in our parallel lists, print sales statements
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# this code could be improved by using a dictionary instead of parallel lists

sales_data = {}

the_file = open("sales-report.txt")

for line in the_file:
    line = line.strip().split("|")
    salesperson = line[0]
    melons_sold = int(line[2])

    sales_data[salesperson] = sales_data.get(salesperson, 0) + melons_sold

print(sales_data)
for key, value in sales_data.items():
    print(f"{key} sold {value} melons.")