from pyairtable import Api, Base, Table

# api = Api('keyMGn202cqBywZH2')
# api.all('appsbvvHn0bnDLXA6', 'tbldwV1o1Z2W8DfLW')

# base = Base('keyMGn202cqBywZH2', 'appsbvvHn0bnDLXA6')
# base.all('tbldwV1o1Z2W8DfLW')

table = Table('keyMGn202cqBywZH2', 'appsbvvHn0bnDLXA6', 'tbldwV1o1Z2W8DfLW')
dic = table.all()

for x in dic: 
    for i in x['fields'].values():
        print(i[1])
