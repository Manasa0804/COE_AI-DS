import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = 'system'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = '6784_coe'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'
# Create an engine
engine = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
df_sql = pd.read_sql('SELECT * FROM courses', engine)
df_csv = pd.read_csv('C:/Users/CVR/PycharmProjects/6784/01-02-25/enrollments.csv')
df_exl = pd.read_excel('instructors.xlsx')
# Display the DataFrame
print("------------SQL Data------------------")
print(df_sql)
print("------------CSV Data------------------")
print(df_csv)
print("------------Excel Data------------------")
print(df_exl)
merged_df=pd.merge(df_sql,df_csv,on='course_id',how='outer')
print("------------Merging SQL and CSV------------------")
print(merged_df)
merged=pd.merge(merged_df,df_exl,on='instructor_id',how='outer')
print("------------Merging all data(sql,csv,excel)------------------")
print(df_sql.dtypes)
print("------Before-------")
print(f'Memory usage:{df_sql.memory_usage(deep=True)}')
df_sql['course_id']=df_sql['course_id'].astype(np.int16)
#df_sql['course_id']=df_sql['course_id'].astype(np.float6) //for float values
print("------After-------")
print(f'Memory usage:{df_sql.memory_usage(deep=True)}')


'''
OUTPUT:
------------SQL Data------------------
   course_id           course_name  credits     semester
0        101    Introduction to AI        3    Fall 2025
1        102       Data Structures        4  Spring 2025
2        103       Web Development        3    Fall 2025
3        104      Database Systems        3  Spring 2025
4        105      Machine Learning        3    Fall 2025
5        106  Software Engineering        4  Spring 2025
6        107       Cloud Computing        3    Fall 2025
7        108      Network Security        3  Spring 2025
------------CSV Data------------------
   enrollment_id  student_id  course_id enrollment_date grade  instructor_id
0           1001         501        101      2025-08-15     A              1
1           1002         502        102      2025-09-01     B              2
2           1003         503        103      2025-08-20     A              3
3           1004         504        104      2025-09-10     C              4
4           1005         505        105      2025-08-25     B              5
5           1006         506        106      2025-09-05     A              6
6           1007         507        107      2025-08-28     A              7
7           1008         508        108      2025-09-15     C              8
------------Excel Data------------------
   instructor_id first_name last_name  ...  hire_date office_location phone_number
0              1       John     Smith  ... 2020-08-15        Room 101     555-1234
1              2       Jane       Doe  ... 2019-05-23        Room 102     555-5678
2              3       Alan     Brown  ... 2018-12-01        Room 103     555-8765
3              4      Emily     Davis  ... 2021-03-18        Room 104     555-4321
4              5    Michael    Wilson  ... 2017-06-12        Room 105     555-6789
5              6      Sarah   Johnson  ... 2022-01-05        Room 106     555-9876
6              7      David    Miller  ... 2015-11-20        Room 107     555-5432
7              8      Laura     Clark  ... 2023-07-10        Room 108     555-2468

[8 rows x 8 columns]
------------Merging SQL and CSV------------------
   course_id           course_name  ...  grade instructor_id
0        101    Introduction to AI  ...      A             1
1        102       Data Structures  ...      B             2
2        103       Web Development  ...      A             3
3        104      Database Systems  ...      C             4
4        105      Machine Learning  ...      B             5
5        106  Software Engineering  ...      A             6
6        107       Cloud Computing  ...      A             7
7        108      Network Security  ...      C             8

[8 rows x 9 columns]
------------Merging all data(sql,csv,excel)------------------
course_id       int64
course_name    object
credits         int64
semester       object
dtype: object
------Before-------
Memory usage:Index          132
course_id       64
course_name    523
credits         64
semester       472
dtype: int64
------After-------
Memory usage:Index          132
course_id       16
course_name    523
credits         64
semester       472
dtype: int64

Process finished with exit code 0
'''