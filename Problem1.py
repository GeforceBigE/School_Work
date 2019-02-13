#Eric Rivera 179008079
#This function takes the integer and compares it against its palindrome to see if it is true or false.
def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
#This function returns the palindrome of an integer
def reverse_int(n):
    reverse_int =int(n[::-1])
    return reverse_int
#This function takes the input, infers if it is a palindrome or not... then generates a palindrome if needed.
#This is Achieved with the while loop.
def palindrome_generator():
    print("The Palindrome Generator")
    print("--------------------------------------\n")
    num = int(input("Enter a positive integer:  "))
    if  palindrome(num):
        print (num, "is a palindrome")
        print( "No iterations were needed to get a palindrome")
        retry()
    else:
            print(num, "is not a palindrome")
            print("Generating a palindrome...")
            counter = 0
            while palindrome(num)==False:
                num +=  reverse_int(str(num))
                counter += 1
                print(num)
            print( counter, 'iterations were needed to get a palindrome')
    retry()
#This function simply restarts the main generator function.
def retry():
    if str(input("Try Again?: [y/n] " )) == 'y':
           palindrome_generator()
    else:
        print("Goodbye!")
           
    
            
    
    





