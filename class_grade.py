
"""Plain English"""
""" 
Start
Create a list to store 5 number (float)
capture users input 5 times for their grades
each time we capture the suers input we append the number to the list 
sort the list ascending then splice the items statring at index 2
once we have three highest number in the list we sum them up and divide by 3
output a message to user
end

"""

""" psudo code
create list
capture input 
append number to list 

capture input 
append number to list 

capture input 
append number to list 

capture input 
append number to list 

capture input 
append number to list 

sort the list then splice out the two lowest number
print message to user

"""

grades = []

grade = input("Enter the 1st grade:")
grades.append(float(grade))

grade = input("Enter the 2st grade:")
grades.append(float(grade))

grade = input("Enter the 3st grade:")
grades.append(float(grade))

grade = input("Enter the 4st grade:")
grades.append(float(grade))

grade = input("Enter the 5st grade:")
grades.append(float(grade))

grades.sort()

grades=grades[2:]
grades = sum(grades)

result = grades / 3

print("Average Grade {0:.2f}%".format(result))
print (grades, 'results', result)
