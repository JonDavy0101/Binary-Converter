'''
Binary Converter v1.0
by: Jonathan Chapman
date: October 13, 2018
'''
x = 0
y = 0
originalArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                 'U', 'V', 'W', 'X', 'Y', 'Z', 
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                 'u', 'v', 'w', 'x', 'y', 'z', 
                 ' ']

binaryArray = ['00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', '00111000', '00111001', 
               '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', '01001000', '01001001', '01001010', 
               '01001011', '01001100', '01001101', '01001110', '01001111', '01010000', '01010001', '01010010', '01010011', '01010100', 
               '01010101', '01010110', '01010111', '01011000', '01011001', '01011010', 
               '01100001', '01100010', '01100011', '01100100', '01100101', '01100110', '01100111', '01101000', '01101001', '01101010', 
               '01101011', '01101100', '01101101', '01101110', '01101111', '01110000', '01110001', '01110010', '01110011', '01110100', 
               '01110101', '01110110', '01110111', '01111000', '01111001', '01111010', 
               '00100000']

originalInput = input(str("\nEnter number, word, or phrase: "))
breakdownInput = list(originalInput)

print("\nResult: ", end = "")
while y < len(breakdownInput):
    breakdownInput[y]
    while True:
        if breakdownInput[y] == originalArray[x]:
            print(binaryArray[x], end = " ")
            x = 0
            break
        else:
            x += 1
    y += 1
y = 0
print("\n")
while y < len(breakdownInput):
    breakdownInput[y]
    while True:
        if breakdownInput[y] == originalArray[x]:
            print(originalArray[x], "=", binaryArray[x])
            x = 0
            break
        else:
            x += 1
    y += 1
y = 0

while True:
    try:
        saveResults = str(input("\nWould you like to save your results? Type Y or N: "))
        if saveResults.isalpha() == True:
            break
        else:
            print("\nSorry, This character cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("\nSorry. This is not a character. You must enter Y or N.")
        pass
saveResults = saveResults.upper()
if saveResults == 'N':
    print("\nOk. Bye!\n")
elif saveResults == 'Y':
    #Save Results on Text File
    file = open("Binary_Conversion_Results.txt", "w")
    file.write("Input: ")
    file.write(originalInput)
    file.write("\n\nResult: ")
    while y < len(breakdownInput):
        breakdownInput[y]
        while True:
            if breakdownInput[y] == originalArray[x]:
                file.write(binaryArray[x])
                file.write(" ")
                x = 0
                break
            else:
                x += 1
        y += 1
    y = 0
    file.write("\n\n")
    while y < len(breakdownInput):
        breakdownInput[y]
        while True:
            if breakdownInput[y] == originalArray[x]:
                file.write(originalArray[x])
                file.write(" = ")
                file.write(binaryArray[x])
                file.write("\n")
                x = 0
                break
            else:
                x += 1
        y += 1
    y = 0
    file.close()
    print("\nYour results have been saved in a text file in the same location as this program.")
    print("Copy and Paste your text file results elsewhere.")
    print("Good bye!\n")
else:
    print("\nOk. Bye!\n")