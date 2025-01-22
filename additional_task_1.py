#1 Write function RemoveExclamationMarks which removes all exclamation marks from a given string.(https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python)
def remove_exclamation_marks(s):
    return s.replace('!', '')
a = "Hello! World!!"
result = remove_exclamation_marks(a)
print(result)