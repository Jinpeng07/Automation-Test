from selenium import webdriver
import random

options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)


class Driver:
    @classmethod
    def get_driver(cls):
        cls.driver = webdriver.Edge(options=options)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()


class Database:
    id = random.randint(1, 10000)

    def __init__(self,database,table):
        self.database = database
        self.table = table

    def insert(self, user_name, password):
        sql = f'insert into {self.table} values({self.id},"{user_name}","{password}")'
        print(sql)
        cursor = self.database.cursor()
        cursor.execute(sql)
        self.database.commit()

    def delete(self, user_name):
        sql = f'delete from {self.table} where UserName="{user_name}"'
        print(sql)
        cursor = self.database.cursor()
        cursor.execute(sql)
        self.database.commit()

    def update_password(self, user_name,new_password):
        sql = f'update {self.table} set Password="{new_password}" where UserName="{user_name}"'
        print(sql)
        cursor = self.database.cursor()
        cursor.execute(sql)
        self.database.commit()

    def show(self):
        sql = 'select * from user'
        print(sql)
        cursor = self.database.cursor()
        cursor.execute(sql)
        print(cursor.fetchall())