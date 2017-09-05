import pandas as import pd
import numpy as np

# read csv file: name = pd.read_csv("filename.csv")
# creat new column by adding two columns: name['new_name'] = name['1'] + name['2']
# export to csv file: name.to_csv('filename.csv')

# Writing Queries in Pandas

'''
select * from name_data,
only x rows: limit x
select data1, data2 from name_data LIMIT X,

SYNTAX:
q= """
your queries
"""
n = pandasql.sqldf(q.lower, locals())
return n
'''
# Example:
#     q = '''
#     select
#     gender, district, sum(aadhaar_generated)
#     from 
#     aadhaar_data
#     where
#     age > 50
#     group by
#     gender, district;
#     '''
    
#     # Execute your SQL command against the pandas frame
#     aadhaar_solution = pandasql.sqldf(q.lower(), locals())

''' 
use URL
url = 'http://...... & api_key = ..... '
data = requests.get(url).text
data = json.loads(data)
print data ['topartists']['artist'][0]['name']
'''

# Sanity Chescking Data

data.describe: show the basic stats of the dataset (mean, max, std...)

Missing Value:
    Easy Imputation：mean, median...
    Linear Regression


    #fillna

# 记住 SQL 里求平均数 是avg() not mean()
# SQL 里 convert date to days of the week 用 strftime
# EG:  cast (strftime('%w', column_name ) as integer)



# 删除一个column del df['Name']
# 将 column 里的值像前移 df.column.shift(前移的值)
# create a new column df['new name'] = [.....]


# 改时间 format: date_formatted = datetime.datetime.strptime(date, "%m-%d-%y").strftime("%Y-%m-%d")


