# Deniz Kaya 280201033
# Kürşat Çağrı Yakıcı 290201098

inProgramLoop = True # setting a flag in order to keep the program in loop

while inProgramLoop:
    print("\nWelcome to the Full Adder!")
    print("(1) Compute and Display the Outputs")
    print("(2) Quit")
    userMenuInput = input("You choose: ")

    if userMenuInput == "2": 
        print("Byee!!")
        inProgramLoop = False # the program will end if the user chooses 2 because while statement will be false at the beginning
        
    elif userMenuInput == "1":
        baseFlag = True # setting a flag to bring the user into a loop until a valid base is chosen
        
        while baseFlag: # the program will ask for a base until a valid one is given
            base = input("Which base will you use to enter data lines (base 16/8/2): ")
            
            if base == "2" or base == "8" or base == "16":
                baseFlag = False # if 2, 8 or 16 is entered, since these are the valid bases for the program, the loop to ask for a base will end

            else:
                print("You have to choose 2, 8 or 16 as base!") # error message if the user enters an invalid input for base choice

        if base == "2": # the program will advance in this if statement's path if base is chosen as 2
            computeFlag = True # setting a flag for the loop until a valid input is given

            while computeFlag: # loop for the user in order to ask until a valid binary input in base 2 is entered
                userComputeInput = input("Please enter input: ")
                
                if len(userComputeInput) != 3: # valid inputs are only of length three, anything else will be rejected
                    print("The input must be 3 bits long")

                else: # checking whether the input is valid when it is of length 3
                    if userComputeInput == "000" or userComputeInput == "001" or userComputeInput == "010" or (
                        userComputeInput == "011" or userComputeInput == "100" or userComputeInput == "101" or (
                        userComputeInput == "110" or userComputeInput == "111")): 
                        computeFlag = False # when the input is valid, flag will be set to false, the program will move on in order to do the calculations

                    else: # if the length of the input is 3 but is not acceptable in binary notation
                        print("Input must consist of only 0's and 1's")

            # mathematical operations to determine the values of a, b and c_IN
            userComputeInput = int(userComputeInput)
            a = userComputeInput // 100 # since the input must be three digits, this integer division will obtain the digit on the left hand side
            b = (userComputeInput // 10) - a * 10 # this is to obtain the middle digit from the input
            cIn = userComputeInput % 10 # using mod of 10 is equal to obtaining the digit on the right hand side.
            
            # converting a, b and c_In to boolean to be able to use the operators
            if a == 1:
                boola = True
            else:
                boola = False

            if b == 1:
                boolb = True
            else:
                boolb = False

            if cIn == 1:
                boolcIn = True
            else:
                boolcIn = False

            sum = boolcIn != (boola != boolb) # the formula for sum
            cOut = (boola and boolb) or (boolcIn and (boola != boolb)) # the formula for c_OUT

            # converting sum and c_Out from boolean to binary
            if sum == True:
                sum = 1
            else:
                sum = 0

            if cOut == True:
                cOut = 1
            else:
                cOut = 0
            print("sum is:", sum, "C_Out is:", cOut)

        elif base == "8": # the program will advance in this if statement's path if base is 8
            computeFlag = True # setting a flag for the loop until a valid input is given

            while computeFlag: # loop for the user in order to ask until a valid input in base 8 is entered
                userComputeInput = input("Please enter input: ")
                
                isBase8 = True # assuming the input is in base 8
                # condition when the user enters an input which is not an octal representation at all
                for number in userComputeInput: # checking the numbers in the input one by one
                    if number != "0" and number != "1" and number != "2" and (
                        number != "3" and number != "4" and number != "5") and (
                        number != "6" and number != "7"):
                        isBase8 = False
                
                if not isBase8 or userComputeInput == "": # "" is included to keep the program running if the user presses enter without writing anything
                    print("This is not an Octal representation! Please enter a valid number in base 8.")
                        
                else: # if the input is an Octal representation
                    userComputeInput = int(userComputeInput) # getting rid of the zeros if user enters something like "00000000007"

                    if len(str(userComputeInput)) != 1: # anything longer than 1 character cannot be represented with 3 bits (for example: 77 is octal but longer than 3 bits)
                        print(f"Octal {userComputeInput} cannot be represented with 3 bits! Please try again!")

                    # mathematical operation for the input to be converted into binary representation, knowing that it is in base 8
                    else:
                        quotient = 1 # initally set to 1 to be able to enter into the while statement
                        binary = 0 # initally set so, to use inside the while loop
                        digit = 1 # this value is used to jump left while writing the remainders as digits in base 2
                        
                        while quotient != 0: # continue to divide until quotient is 0 to convert into base 2 representation.
                            quotient = userComputeInput // 2 # integer division to find quotient
                            remainder = userComputeInput - quotient * 2 # operation to find the remainder after the division
                            binary = binary + remainder*digit # remainder is saved
                            digit *= 10 # digit will be multiplied by 10 to write the next remainder on the left of the previous remainder every time
                            userComputeInput = quotient # quotient is set as the number with which the same operations will be executed until while statement stops

                        # mathematical operations to determine the values of a, b and c_IN
                        a = binary // 100 # since the input must be three digits, this integer division will obtain the digit on the left hand side
                        b = (binary // 10) - a * 10 # this is to obtain the middle digit from the input
                        cIn = binary % 10 # using mod of 10 is equal to obtaining the digit on the right hand side.
                        
                        # converting a, b and c_In to boolean to be able to use the operators
                        if a == 1:
                            boola = True
                        else:
                            boola = False

                        if b == 1:
                            boolb = True
                        else:
                            boolb = False

                        if cIn == 1:
                            boolcIn = True
                        else:
                            boolcIn = False

                        sum = boolcIn != (boola != boolb) # the formula for sum
                        cOut = (boola and boolb) or (boolcIn and (boola != boolb)) # the formula for c_OUT

                        # converting sum and c_Out from boolean to binary
                        if sum == True:
                            sum = 1
                        else:
                            sum = 0

                        if cOut == True:
                            cOut = 1
                        else:
                            cOut = 0
                        print("sum is:", sum, "C_Out is:", cOut)

                        computeFlag = False # flag is set to false to return to the main menu


        elif base == "16": # the program will advance in this if statement's path if base is 16
            computeFlag = True # setting a flag for the loop until a valid input is given

            while computeFlag: # loop for the user in order to ask until a valid input in base 8 is entered
                userComputeInput = input("Please enter input: ")
                isBase16 = True # flag to check if the input is a Hexadecimal representation
                not3Bits = False # flag to check if the input can be represented using 3 bits
                for number in userComputeInput: # checking the numbers in the input one by one

                    # condition when the user enters an input which is not a Hexadecimal representation at all
                    if  (number != "0" and number != "1" and number != "2" and (
                        number != "3" and number != "4" and number != "5" and number != "6") and (
                        number != "7" and number != "8" and number != "9" and number != "A") and (
                        number != "B" and number != "C" and number != "D" and number != "E") and (
                        number != "F" and number != "a" and number != "b" and number != "c") and (
                        number != "d" and number != "e" and number != "f")):
                        isBase16 = False

                    # conditions when 3 bits wouldn't be enough to convert the base into binary
                    if  number == "8" or number == "9" or number == "A" or (
                        number == "B" or number == "C" or number == "D" or number == "E") or (
                        number == "F" or number == "a" or number == "b" or number == "c") or (
                        number == "d" or number == "e" or number == "f"):
                        not3Bits = True

                if not isBase16 or userComputeInput == "": # "" is included to keep the program running if the user presses enter without writing anything
                    print("This is not a Hexadecimal representation! Please enter a valid number in base 16.")
                        
                else: # input is Hexadecimal representation at this point
                    if not3Bits or (not not3Bits and int(userComputeInput) > 7): # when the input is Hexadecimal representation but greater than 7
                        print(f"Hexadecimal {userComputeInput} cannot be represented with 3 bits! Please try again!")
                    
                    else:

                        # mathematical operation for the input to be converted into binary representation, knowing that it is valid in base 16
                        userComputeInput = int(userComputeInput) # getting rid of the zeros if user enters something like "00000000007"
                        quotient = 1 # initally set to 1 to be able to enter into the while statement
                        binary = 0 # initally set so, to use inside the while loop
                        digit = 1 # this value is used to jump left while writing the remainders as digits in base 2
                        
                        while quotient != 0: # continue to divide until quotient is 0 to convert into base 2 representation.
                            quotient = userComputeInput // 2 # integer division to find quotient
                            remainder = userComputeInput - quotient * 2 # operation to find the remainder after the division
                            binary = binary + remainder*digit # remainder is saved
                            digit *= 10 # digit will be multiplied by 10 to write the next remainder on the left of the previous remainder every time
                            userComputeInput = quotient # quotient is set as the number with which the same operations will be executed until while statement stops

                        # mathematical operations to determine the values of a, b and c_IN
                        a = binary // 100 # since the input must be three digits, this integer division will obtain the digit on the left hand side
                        b = (binary // 10) - a * 10 # this is to obtain the middle digit from the input
                        cIn = binary % 10 # using mod of 10 is equal to obtaining the digit on the right hand side.

                        # converting a, b and c_In to boolean to be able to use the operators
                        if a == 1:
                            boola = True
                        else:
                            boola = False

                        if b == 1:
                            boolb = True
                        else:
                            boolb = False

                        if cIn == 1:
                            boolcIn = True
                        else:
                            boolcIn = False

                        sum = boolcIn != (boola != boolb) # the formula for sum
                        cOut = (boola and boolb) or (boolcIn and (boola != boolb)) # the formula for c_OUT

                        # converting sum and c_Out from boolean to binary
                        if sum == True:
                            sum = 1
                        else:
                            sum = 0

                        if cOut == True:
                            cOut = 1
                        else:
                            cOut = 0
                        print("sum is:", sum, "C_Out is:", cOut)

                        computeFlag = False # flag is set to false to return to the main menu

    else: # menu error when something else than 1 or 2 is chosen
        print("You must type 1 or 2 in order to move inside the menu!")
