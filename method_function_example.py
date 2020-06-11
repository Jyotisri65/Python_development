'''

ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
'''
def animal_crackers(a):
    x=[]
    for y in a.split( ):
        x.append(y)
    if x[0][0]==x[1][0]:
        return True
    else:
        return False

animal_crackers('Levelheaded Llama')
