"""
Data Science with Python

Numpy: 1. Multidimensional arrays and matrices
	 2. Mathematical Functions

Pandas: 1. Handle data in a way suited to analysis
	 2. Similar to R


					Numpy
1. Functions useful for statistical analysis: Mean, Median, Standard Deviation

                    Pandas
1. Dataframes --- like 1 excel sheet, rows and columns
2. Series: an one-dimensional object that is similar to
an array, list, or column in a database. By default, it will assign an
index label to each item in the Series ranging from 0 to N, where N is
the number of items in the Series minus one.
"""
import numpy as np
import pandas as pd


# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(np.mean(numbers))
# print(np.median(numbers))
# print(np.std(numbers))

# array = np.array([[1,2,3],[4,5,6]],int)
# print (array)


# series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
# print (series)

'''
You can also manually assign indices to the items in the Series when
creating the series
'''

# Change False to True to see custom index in action

# series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
#                     index=['Instructor', 'Curriculum Manager',
#                             'Course Number', 'Power Level'])
# print (series)

# '''
# You can use index to select specific items from the Series
# '''
# # Change False to True to see Series indexing in action
# if False:
# series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
#                     index=['Instructor', 'Curriculum Manager',
#                             'Course Number', 'Power Level'])
# print (series['Instructor'])
# print ("")
# print (series[['Instructor', 'Curriculum Manager', 'Course Number']])

# '''
# You can also use boolean operators to select specific items from the Series
# '''
# # Change False to True to see boolean indexing in action
# if False:
# cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
#                                                 'Puppy', 'Kitten'])
# print (cuteness > 3)
# print ("")
# print (cuteness[cuteness > 3])


# data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#         'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
#                     'Lions', 'Lions'],
#         'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#         'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
# football = pd.DataFrame(data)
# print (football)

'''
Pandas also has various functions that will help you understand some basic
information about your data frame. Some of these functions are:
1) dtypes: to get the datatype for each column
2) describe: useful for seeing basic statistics of the dataframe's numerical
   columns
3) head: displays the first five rows of the dataset
4) tail: displays the last five rows of the dataset
'''
# Change False to True to see these functions in action
# if False:
#     data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#             'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
#                      'Lions', 'Lions'],
#             'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#             'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
#     football = pd.DataFrame(data)
#     print football.dtypes
#     print ""
#     print football.describe()
#     print ""
#     print football.head()
#     print ""
#     print football.tail()


# def create_dataframe():
    
#     countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
#                  'Netherlands', 'Germany', 'Switzerland', 'Belarus',
#                  'Austria', 'France', 'Poland', 'China', 'Korea', 
#                  'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
#                  'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
#                  'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

#     gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#     silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
#     bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

#     # your code here
#     data = {"country_name)":Series(countries),
#              "gold": Series(gold),
#              "solver":Series(silver),
#              "bronze":Series(bronze)}
#     olympic_medal_counts_df = DataFrame(data)

#     return olympic_medal_counts_df


data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                    'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)
# print (football.iloc[[0]]) #only print the first row of the Data Frame; same with loc

# print (football.loc[[0]]) #only print the first row of the Data Frame

# print (football[3:5])

# print (football[football.wins > 10])

# print (football[(football.wins > 10) & (football.team == "Packers")])

#print(football[["year","team"]] [(football.wins >=10)&(football.losses <=5)])
# 双重选择：print(df[["first column","second column"]] [(df.condition1)&(df.condtion2)&(df.condition3)])

#df.apply(numpy.mean) -- mean for each column
# c= numpy.mean(columan) 可以导出结果
#df['one'].map(lambda x:x>=1)
#df.applymap(lambda x:x>=1)
football_1 = football[["wins", "losses"]]
print(football_1.apply(np.mean))
#print(football_1)

#numpy matrix/vector multiplication
#numpy.dot(matrix1,matrix2)

