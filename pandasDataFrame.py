import pandas as pd


#we want to give each student multiple grades

grades_dict = {'Wally':[87,96,70],
                'Eva':[100,87,90],
                'Sam':[94,77,90],
                'Katie':[100,81,82],
                'Bob':[83,65,85]}       #5 Columns(keys), 3 Rows(values)
                                        #for dictionaries, keys become columns and values become rows

#create dataframe
grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)
#print(grades.T) #T stands for transpose -> this does not permenantly change the dataframe


#each column is called a Pandas Series (not a list or a dictionary)

# print(grades['Eva'])

# print(grades.Sam)

#using the loc and iloc methods
# print(grades.loc['Test2'])  #loc = location
#                             #a Series is returned

# print(grades.iloc[1])       #returns the same thing bcs test2 is at index 1
#                             #iloc = index location

#         #if non-consecutive, you must use []

# #for consecutive rows
# print(grades.loc['Test1':'Test3'])
#     #in loc method, the upper bound IS included
#         #the colon: indicates Consecutive
# print(grades.iloc[0:3])
#     #in the iloc method, the upper bound IS NOT included

# #for non-consecutive rows
# print(grades.loc[['Test1','Test3']])    #use brackets because these are non-consecutive
#                                         #we just want Test1 and Test3
# print(grades.iloc[[0,2]])


#View only Eva's and Katie's grades for Test1 and Test2
    #remember: rows come before columns
print(grades.loc[:'Test2',['Eva', 'Katie']])

#View only Sam through Bob's grades for Test1 and Test2
print(grades.loc[['Test1','Test3'],'Sam':'Bob'])


#Select everyone with an A grade
grades_A = grades[grades >= 90]

print(grades_A)
#NaN means Not a Number

#create a dataframe for everyone w/ a B grade
grades_B = [(grades>=80) & (grades < 90)]   #to use an "and" in dataframe, use '&'

#create a dataframe for everyone w/ a A or B grade
grades_A_or_B = [(grades>=90) | (grades>=80)]   # | means or

print(grades_A_or_B)

#this sets it to 2 decimal places
pd.set_option('precision',2)

# print(grades.T.describe())


#SORTING

#puts this in descending order
print(grades.sort_index(ascending=False))

#alphabetical order
print(grades.sort_index(axis=1))

#descending order
print(grades.sort_index(axis=1,ascending=False))

#sort by the value of the dataframe
print(grades.sort_values(by='Test1', axis=1, ascending=False))

#students in descending order and Tests are the Columns
print(grades.T.sort_values(by='Test1', ascending=False))

#gets rid of columns2 and 3; just shows column1
print(grades.loc['Test1'].sort_values(ascending=False))

