import sqlite3
##
##conn = sqlite3.connect("source.db") # или :memory: чтобы сохранить в RAM
##cursor = conn.cursor()
####
##### Создание таблицы
####cursor.execute("""CREATE TABLE albums
####                  (title text, artist text, release_date text,
####                   publisher text, media_type text)
####               """)
####
####albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
####          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
####          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
####          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
#### 
####cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
####conn.commit()
####
##import random
##tables = ['table_1','table_2','table_3','table_4']
##fruit = ["Яблоки","Груши","Мандарины","Помидоры","Апельсины","Огурцы","Гранаты",]
##city = ["Москва","Красноярск","Рига","Смоленск","Киев","Кишинев","Владивосток"]
##title = ['Fruit','City','Value','Weight','Number']
##
##
##for table in tables:
##
##    #table = 'albums'
##
##    string_1 = 'CREATE TABLE '+table+'('
##    for i in title:
##        string_1 += i+' text, '
##    string_1 = string_1[:-2]
##    string_1 +=')'
##
##    cursor_str = 'INSERT INTO '+table+' VALUES ('
##    for i in title:
##        cursor_str+='?, '
##        
##    cursor_str = cursor_str[:-2]
##    cursor_str +=')'
##
##
##    table_list = []
##    for j in range(1000):
##        table_list.append(( fruit[random.randint(0, len(fruit)-1)],
##                            city[random.randint(0, len(city)-1)],
##                            random.randint(0, 1000),
##                            random.randint(0, 100),
##                            j))
##
##
##
##    
##
##    print(string_1)
##    print(cursor_str)
##    print('____')
##
##    cursor.execute(string_1)
##    cursor.executemany(cursor_str, table_list)
##    conn.commit()
 

conn = sqlite3.connect("source.db")
cursor = conn.cursor()
cursor.execute('SELECT * FROM table_2')
##for row in cursor.execute('SELECT * FROM table_2'):
##    print(row)


#print([column[0] for column in cursor.description])



def from_sql(table_name):
    cursor = sqlite3.connect("source.db").cursor()
    cursor.execute('SELECT * FROM '+table_name)
    list_table = [[i[0] for i in cursor.description]]
    list_table += cursor.fetchall()
    return list_table

t = from_sql('table_2')
    
for i in t:
    print(i)



    
    
