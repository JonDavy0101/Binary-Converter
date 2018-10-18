'''
Binary Converter v0.2
by: Jonathan Chapman
date: October 17, 2018
'''

binaryDict = {0:'00110000', 1:'00110001', 2:'00110010', 3:'00110011', 4:'00110100', 5:'00110101', 6:'00110110', 
              7:'00110111', 8:'00111000', 9:'00111001', 
              'A':'01000001', 'B':'01000010', 'C':'01000011', 'D':'01000100', 'E':'01000101', 'F':'01000110', 
              'G':'01000111', 'H':'01001000', 'I':'01001001', 'J':'01001010', 'K':'01001011', 'L':'01001100', 
              'M':'01001101', 'N':'01001110', 'O':'01001111', 'P':'01010000', 'Q':'01010001', 'R':'01010010', 
              'S':'01010011', 'T':'01010100', 'U':'01010101', 'V':'01010110', 'W':'01010111', 'X':'01011000', 
              'Y':'01011001', 'Z':'01011010', 
              'a':'01100001', 'b':'01100010', 'c':'01100011', 'd':'01100100', 'e':'01100101', 'f':'01100110', 
              'g':'01100111', 'h':'01101000', 'i':'01101001', 'j':'01101010', 'k':'01101011', 'l':'01101100', 
              'm':'01101101', 'n':'01101110', 'o':'01101111', 'p':'01110000', 'q':'01110001', 'r':'01110010', 
              's':'01110011', 't':'01110100', 'u':'01110101', 'v':'01110110', 'w':'01110111', 'x':'01111000', 
              'y':'01111001', 'z':'01111010', 
              ' ':'00100000'}

originalInput = ""
breakdownInput = ""

def userInput():
    global originalInput
    originalInput = input(str("\nEnter number, word, or phrase: "))
    global breakdownInput
    breakdownInput = list(originalInput)
    
def convertToBinary():
    print("")
    for x in breakdownInput:
        print(binaryDict[x], end = " ")
    print("\n")
    for x in breakdownInput:
        print(x + " " + binaryDict[x])

def saveResults():
    with open("BinaryConverterResults.txt", "w") as results:
        results.write("Input: " + originalInput)
        results.write("\n\nResults: ")
        for x in breakdownInput:
            results.write(binaryDict[x] + " ")
        results.write("\n\n")
        for x in breakdownInput:
            results.write(x + " " + binaryDict[x] + "\n")
    
userInput()
convertToBinary()
while True:
    try:
        saveQuestion = str(input("\nWould you like to save your results? Type Y or N: "))
        if saveQuestion.isalpha() == True:
            break
        else:
            print("\nSorry, This character cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("\nSorry. This is not a character. You must enter Y or N.")
        pass
saveQuestion = saveQuestion.upper()
if saveQuestion == 'N':
    print("\nOk. Bye!\n")
elif saveQuestion == 'Y':
    saveResults()
    print("\nYour results have been saved in a text file in the same location ")
    print("as this program. Copy and Paste your text file results elsewhere.")
    print("Good bye!\n")
        


