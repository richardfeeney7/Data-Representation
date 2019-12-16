import mysql.connector


class StudentDAO:

    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "datarepresentation"
        )

    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into student (name, age) values (%s, %s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
        print("create done")

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
        print("get all done")

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from student where id = %s"
        values = (id, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def update(self, values):
        cursor = self.db.cursor()
        sql = "update student set name = %s, age = %s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        print("update done")

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from student where id = %s"
        values = (id, )
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done for id", id)
studentDAO = StudentDAO()

