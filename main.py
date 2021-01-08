import sqlite3

# os.remove("school.db") if os.path.exists("school.db") else None
con = sqlite3.connect("school.db")

cur = con.cursor()

sql_create = 'create table if not exists school('\
             'id integer primary key,'\
             'titulo varchar(100),'\
             'categoria varchar(50))'

cur.execute(sql_create)

sql_insert = 'insert into school values (?,?,?)'

recset = [(10080, 'Ciência de Dados', 'Data Science'),
          (10081, 'Big Data Fundamentos', 'Big Data'),
          (10802, 'Python Fundamentos', 'Análise de Dados')]

for rec in recset:
    cur.execute(sql_insert, rec)

con.commit()

sql_select = "select * from school"

datas = cur.execute(sql_select)

for data in datas:
    print(data)

con.close()
