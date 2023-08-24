import pymysql
from Util import Database

db = pymysql.connect(host='127.0.0.1',port=3306,user="root",passwd='admin123',db="testsql1",charset='utf8')
database = Database(database=db, table='user')
database.insert(user_name='王金鹏', password='123')
database.show()
#Database.delete(database=db,table='user',user_name='王金鹏')
database.update_password( user_name='王金鹏', new_password="wangjinp")
database.show()
