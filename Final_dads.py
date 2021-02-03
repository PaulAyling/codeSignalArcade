def almostIncreasingSequence(sequence):
    errors = 0
    under_two_errors = True
    n = 0
    nmax = len(sequence)-2
    print(sequence)
    print("nmax = ",nmax)
    loop = 1
    
    if len(sequence) == 2:
        under_two_errors = True
        return(under_two_errors)
    
    #If the first number is larger than the second set errors to 1 and set counter n to the next entry
    if sequence[n] >= sequence[n +1]:
        errors = 1
    n = n + 1
    print("errors = ",errors)
    
    #The While loop checks as far as comparing the 3rd from last with the 2nd from last number
    #The while loop executes while the number to remove from the sequence is less than 2
    #and still numbers to check

    while (under_two_errors == True) and (n<nmax):
        print("loop = ",loop,"   n = ",n)
        
    #If the current number is bigger or equal to the nextand there is already an error
    #see if a sequence can continue without the value at n and do the same for n+1
    #set "remove_n" and "remove_after_n" flags True or False
    
    
        if sequence[n] >= sequence[n +1]:
            print("Failed n to n+1  ",sequence[n],"   ",sequence[n+1])
            if errors < 1:
                errors = 1  #set
                if sequence[n-1] < sequence[n +1]:
                    remove_n = True
                    print("Remove ",sequence[n])
                else:
                    remove_n = False
                if sequence[n] < sequence[n + 2]:
                    remove_after_n = True
                    print("Remove ",sequence[n+1])
                else:
                    remove_after_n = False

    #If neither way will continue the sequence, two numbers would have to be removed
    
                if (remove_n==False)and(remove_after_n==False):
                    under_two_errors = False

                loop = loop + 1
                n = n + 1
                
    #If there was already an error the new one is too many
                
            else:
                under_two_errors = False
        else:
            n = n + 1
            loop = loop + 1
    
    #If we have already had to remove a number, check to see if the 2nd to last number
    #is larger than the last, if so the test has failed
    
    if errors == 1:
        if sequence[nmax] >= sequence[nmax+1]:
            under_two_errors = False
    
    return(under_two_errors)

            


# a = [1,2,3,4,8,3] # Pass
# b = [1,2,5,1,7,8] # Pass
# c = [1,2,5,3,4,5] # Pass
# d = [1,2,5,1,2,3] # Pass
# e = [1,2,3,4,5,6] # Pass
# f = [1,4,3,4,5,6] # Pass
# g = [4,5,6,1,2,3] # Fail



# result = almostIncreasingSequence(e)
# print(result)

