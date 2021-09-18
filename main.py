from tkinter import *
from tkinter import ttk
import shlex

root = Tk()
root.title('SkyBox')
root.iconbitmap('')
root.geometry("500x500")
num = 0
data2 = []

my_tree = ttk.Treeview(root)

# Define columns
my_tree['columns'] = ("Name", "ID", "Favorite Food")

# Format columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favorite Food", anchor=W, width=120)

# Create Headings
my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Food", text="Favorite Food", anchor=W)

# Load data file into program
my_file = open("data.txt")
data = my_file.read()

# Close file once information is loaded into data element.
my_file.close()

# Remove line breaks from data_list
data_list = data.split('\n')

# Print data to ensure it is working.
print(data)
print(data_list)

# Create new temporary list to store some data in.
temp = []

# For loop to iterate through the data_list and split into
# nested lists for every comma in data.
for elem in data_list:
    data2 = elem.split(', ')
    temp.append(data2)

# List initialization for final output of data.
Output = []

# Iterate through temp list to append data to Output.
for elem in temp:
    # data3 is another temporary list that will be appended
    # to Output.
    data3 = []
    for elem2 in elem:
        data3.append(elem2)
    Output.append(data3)

# Set count values to 0, except the ID which starts at 1.
num = 0
num1 = 0
idNum = 1

# Add ID number to each nested list.
for elem in Output[num1]:
    Output[num].insert(1, int(idNum))
    idNum += 1
    num += 1
    num1 += 1

# Print output to ensure it is working.
print(Output)

# Run through the data and add to GUI for users.
count = 0
for record in Output:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]))
    count += 1

# Pack to the screen
my_tree.pack(pady=20)

root.mainloop()
