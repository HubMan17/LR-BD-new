from time import sleep
from peewee import *
from PySide6 import QtCore, QtGui, QtWidgets

import Moduls.work_ini

# global db = None


# def initialize():
    # db = SqliteDatabase('D:/LR BD new/Database.db')
    
    # global db
    
# app_second = QtWidgets.QApplication()
# db = SqliteDatabase(QtWidgets.QFileDialog.getOpenFileName(filter="*.db")[0])\
db = SqliteDatabase(Moduls.work_ini.get_db_link(), pragmas={'foreign_keys': "1"})

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    
    class Meta:
        database = db
        order_by = "id"


class Spec(BaseModel):
    name = CharField(unique=True, null=False)
    price = IntegerField(null=False)
    
    class Meta:
        db_table = "specs"


class Teacher(BaseModel):
    name = CharField(unique=True, null=False)
    
    class Meta:
        db_table = "teacher"
        
class Discipline(BaseModel):
    name = CharField(null=False)
    specid = ForeignKeyField(Spec)
    start = IntegerField(null=True) # start semester
    end = IntegerField(null=True) # and semester

    class Meta:
        db_table = "discipline"


class Teacher_discipline(BaseModel):
    teachid = ForeignKeyField(Teacher, on_delete='CASCADE')
    discid = ForeignKeyField(Discipline, on_delete='CASCADE')
    specid = ForeignKeyField(Spec, on_delete='CASCADE') 
    
    class Meta:
        db_table = "teacher_discipline"


class Study_schedule(BaseModel):
    iddisc = ForeignKeyField(Discipline)
    idspec = ForeignKeyField(Spec)
    start = IntegerField()
    end = IntegerField()
    sem1_o = CharField()
    sem1_e = CharField()
    sem2_o = CharField()
    sem2_e = CharField()
    sem3_o = CharField()
    sem3_e = CharField()
    sem4_o = CharField()
    sem4_e = CharField()
    sem5_o = CharField()
    sem5_e = CharField()
    sem6_o = CharField()
    sem6_e = CharField()
    sem7_o = CharField()
    sem7_e = CharField()
    sem8_o = CharField()
    sem8_e = CharField()
    
    class Meta:
        db_table = "study_schedule"
        
        
class Session_sheet(BaseModel):
    diplom = IntegerField(null=False)
    fname = CharField(unique=False, null=False)
    lname = CharField(unique=False, null=False)
    iddisc = ForeignKeyField(Discipline)
    idspec = ForeignKeyField(Spec)
    start = IntegerField()
    end = IntegerField()
    sem1_o = CharField(default= '-')
    sem1_e = CharField(default= '-')
    sem2_o = CharField(default= '-')
    sem2_e = CharField(default= '-')
    sem3_o = CharField(default= '-')
    sem3_e = CharField(default= '-')
    sem4_o = CharField(default= '-')
    sem4_e = CharField(default= '-')
    sem5_o = CharField(default= '-')
    sem5_e = CharField(default= '-')
    sem6_o = CharField(default= '-')
    sem6_e = CharField(default= '-')
    sem7_o = CharField(default= '-')
    sem7_e = CharField(default= '-')
    sem8_o = CharField(default= '-')
    sem8_e = CharField(default= '-')
    
    class Meta:
        db_table = "session_sheet"

        
class Group(BaseModel):
    name = CharField(unique=True, null=False)
    course = IntegerField(null=False)
    curator = CharField()
    specid = ForeignKeyField(Spec, on_delete='CASCADE') 
    
    class Meta:
        db_table = "groups"


class Student(BaseModel):
    diplom = IntegerField(unique=True, null=False)
    fname = CharField(null=False)
    lname = CharField(null=False)
    enrollment = DateField(null=False)
    status = CharField(null=False)
    paid = IntegerField()
    groupid = ForeignKeyField(Group)
    
    class Meta:
        db_table = "students"
        

class Report(BaseModel):
    lname = CharField(null=False)
    diplom = IntegerField(null=False)
    rep_date = DateField(null=False)
    reason = CharField()
    
    class Meta:
        db_table = "reports"
        
        
class Archive(BaseModel):
    diplom = IntegerField()
    name = CharField()
    enrollment = DateField()
    expulsion = DateField()
    course = IntegerField()
    specName = CharField()
    reason = CharField()
    
    class Meta:
        db_table = "archives"


class Qualifying_exam(BaseModel):
    name = CharField(unique=True, null=False)
    specid = ForeignKeyField(Spec)
    list_of_spec = TextField()
    
    class Meta:
        db_table = "qualifying_exam"
        
        
class Session_qualifying_exam(BaseModel):
    q_examid = ForeignKeyField(Qualifying_exam, on_delete='CASCADE')
    specid = ForeignKeyField(Spec, on_delete='CASCADE')
    diplom = IntegerField(null=False)
    fname = CharField()
    lname = CharField()
    grade1 = DoubleField(null=True)
    grade2 = DoubleField(null=True)
    grade3 = DoubleField(null=True)
    grade4 = DoubleField(null=True)
    grade5 = DoubleField(null=True)
    average_grade = DoubleField(null=True)
    recommend_grade = DoubleField(null=True)
    end_grad = DoubleField(null=True)
    
    class Meta:
        db_table = "session_qualifying_exam"


# db.create_tables([Session_qualifying_exam])


# exam = Qualifying_exam.get(Qualifying_exam.id == 2)
# stud = Student.select().join(Group).join(Spec).where(Spec.id == exam.specid)

# for i in stud:
#     Session_qualifying_exam.insert(
#         q_examid=exam.id, specid=exam.id,
#         diplom=i.diplom, fname=i.fname, lname=i.lname
#         ).execute()


# # print(len(exam.list_of_spec.split(";")) - 1)
# print("accept")
# sleep(5)


# Discipline.delete().where(Discipline.id == 21).execute()
        
# Spec.delete().where(Spec.id == 4).execute()

# db.create_tables([Spec_test, Group_test])
# respond = Group_test.select()
# for i in respond:
#     print(i.name)


# db.create_tables([Session_sheet])
# cursor = db.execute_sql("""SELECT * FROM session_sheet ss 
# INNER JOIN groups g ON g.id = ss.idspec_id 
# WHERE g.name = 'ОДЛ-1'""")
# print(len(cursor.fetchall()))

# for row in cursor.fetchall():
#     print(row)