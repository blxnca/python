#Complete the solution so that it splits the string into pairs of two characters. 
#If the string contains an odd number of characters 
#then it should replace the missing second character of the final pair 
#with an underscore ('_').

def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    return ([s[i:i+2] for i in range(0, len(s), 2)])

solution("asdfadsf") # ['as', 'df', 'ad', 'sf']
solution("asdfads") #['as', 'df', 'ad', 's_']
solution("") #[]
solution("x") #["x_"]

'''def split_pairs(s):
    new_lst = []

    if len(s) % 2 != 0:
        s += "_"

    for i in range(0, len(s), 2):
        new_lst.append(s[i : i + 2])
    return new_lst'''