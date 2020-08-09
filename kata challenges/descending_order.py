# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.
def descending_order(num):
    l = (list(map(int, str(num))))
    l.sort(reverse = True)
    strings = [str(i) for i in l]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return(an_integer)

descending_order(0) #0
descending_order(15) #51
descending_order(123456789) #987654321