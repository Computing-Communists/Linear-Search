# this is a Linear Search

# this takes the value we want to be searching for
user_input = int(input("What number are you searching for? "))

# this is the array, the numbers must be in the correct order 
array = [1,4,6,34,63,79,99,128,173,181,182,198,201,205]

checks = 0 #amount of checks it takes 
i = 0 # iterator
found = False
while i <= len(array) and found == False:
    if user_input == array[i]:
        found = True
    else:
        checks += 1
        i += 1 # this is the same as doing i = i+ 1

if found == False:
    print("the number wasn't found")
else:
    print(str(user_input) + " was found after " + str(checks) + " checks")
    
