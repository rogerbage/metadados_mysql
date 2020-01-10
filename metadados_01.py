import mysql.connector as mysql

endereco = input('Endereço ou Ip do servidor Mysql: ')
usuario = input ('Nome do usuario do banco Mysql: ')
senha = input('Senha do banco de dados: ')

db = mysql.connect(
    host = endereco,
    user = usuario,
    passwd = senha
)

cursor = db.cursor()

## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")

## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

todas = '''<?xml version="1.0" encoding="UTF-8"?>
            <metadata>
                '''

for database in databases:
    cursor.execute('USE ' + database[0])
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall() 
    todas += '''<''' + database[0] + '''>
                        '''

    for table in tables:
        cursor.execute('show fields from ' + table[0])
        rows = cursor.fetchall() 
        todas += '''<''' + table[0] + '''>
                            '''
        for row in rows:
            todas +=  '''<''' + str(row[0]) + '''>
                                <tipo>''' + str(row[1]) + '''</tipo>
                                <nulo>''' + str(row[2]) + '''</nulo>
                                <prim>''' + str(row[3]) + '''</prim>
                                <defalt>''' + str(row[4]) + '''</defalt>
                                <extra>''' + str(row[5]) + '''</extra>
                            </''' + str(row[0]) + '''>
                            '''
        
        todas += '''
                        </''' + table[0] + '''>
                        '''
    todas += '''</''' + database[0] + '''>
                    '''
    
todas += '''</metadata>
            </xml>'''

text_file = open("Output.txt", "w")
text_file.write(todas)
text_file.close()