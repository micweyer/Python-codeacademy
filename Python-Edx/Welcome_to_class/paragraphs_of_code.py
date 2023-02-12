n = 5
while n > 0 :
    print(n)
    n = n - 1
print("Blastoff!")

#while n is 5, it prints 5 and then continues on to n = n - 1. 
#Then after printing 5, it sends 5 through the next function of 5-1. 4
#Since 4 is greater than 0 it prints 4 and sends it through the next function, lessening 4 to 3, and repeating.
#This is all happening because of the while statement. 
#it leaves the while statement once we get to 1, 1-1, then 0 is not > 0 so it skips the print function under the while statement
#Then it goes to the final print statement of blastoff