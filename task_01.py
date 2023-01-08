#Задача номер 1
#https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad

def invert(lst):
    return list(map(lambda x: -x, lst));

# Хорошо!
# Если использовать пройденный материал, то можно так

def invert(lst):
    arr = []
    for i in lst:
        arr.append(-i)
    return arr

# Или короче (через списковые включения)
def invert(lst):
    return [-i for i in lst]
