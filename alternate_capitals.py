# Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)

#   Input: “hello, how are your porcupines today?”
#   Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”

def alternate_capitals(input):
    index = 0
    output = ""
    for x in input:
        if index % 2 == 0:
            output += input[index].lower()
        else:
            output += input[index].upper()
        index += 1
    return output


print(alternate_capitals("hello, how are your porcupines today?"))
