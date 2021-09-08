import re
from array import array

"""
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Salida:

Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756
"""
file = input("Enter file: ").strip()

try:
    with open(f"Expresiones regulares/{file}","r") as file:
        numbers = array('f',[])
        data = file.readlines()
        for line in data:
            numbers.fromlist([float(i) for i in re.findall(r"([\d]+)",line)])
        print("Average: {}".format(int(sum(numbers)/len(numbers))))
except FileNotFoundError:
    print("{} not found!".format(file))
