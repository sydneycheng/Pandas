import pandas as pd


#pandas Series = a 1D array
#pandas Dataframe = a 2D array

grades = pd.Series([87,100,94])

print(grades)

grades2 = pd.Series(98.6, range(3))

#print(grades2)

print(grades[0])

print(grades.describe())    #.describe method shows all the aggregate functions in the array



#custom indexing with arrays
grades = pd.Series([87,100,94], index = ['Wally', "Eva", "Sam"])

print(grades)

grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})   #when u make a dictionary, the key becomes the index value (eva, walley, sam)

'''
print(grades)

#print Eva's grade
print(grades['Eva'])

#print Wally's grade using "." dot notation
print(grades.Wally)

#gives datatype of the series
print(grades.dtype)

#gives the value fo the series
print(type(grades.values))

'''
#Series of string values
hardware = pd.Series(['hammer', 'Saw', 'Wrench'])

#find which values in the series contain 'a' --output: either True or False
print(hardware.str.contains('a'))

#changes everything in the series to UPPERCASE
print(hardware.str.upper())