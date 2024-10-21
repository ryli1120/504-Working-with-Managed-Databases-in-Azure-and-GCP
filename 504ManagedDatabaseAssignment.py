!pip install sqlalchemy pymysql pandas

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('NCHS_-_Leading_Causes_of_Death__United_States.csv')
df

username = 'LRyan'
password = '**********'
hostname = '**********'
database = ''

connection_string = f'mysql+pymysql://{ryan}:{**********}}@{hostname}/{database}'

engine = create_engine(connection_string)

df.to_sql('Deaths', engine, if_exists='replace')

query = '''
select *
from Deaths
where Deaths > 5000;
'''

test_query = pd.read_sql(query, engine)
test_query
