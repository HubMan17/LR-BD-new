from peewee import *
from Moduls.models import *
import datetime

        
def create_start_db():
    with db:
        db.create_tables([Spec, Group, Student, Report, Archive])
        
        # create spec
        specs = [
            {'name': "Логистика", 'price': 42000},
            {'name': "Программирование", 'price': 46000},
            {'name': "Дизайн", 'price': 40000}
        ]
        Spec.insert_many(specs).execute()
        
        # create groups
        specs = Spec.select()
        groups = [
            {'name': "ОДЛ-1", 'course': 1, 'curator': "Маянэ Георгиевна", 'specid':specs[0].id},
            {'name': "ОДЛ-2", 'course': 2, 'curator': "Маянэ Георгиевна", 'specid':specs[0].id},
            {'name': "ИСиП-1", 'course': 1, 'curator': "Марина Александровна", 'specid':specs[1].id},
            {'name': "ИСиП-2", 'course': 2, 'curator': "Марина Александровна", 'specid':specs[1].id},
            {'name': "ДИЗ-1", 'course': 1, 'curator': "Татьяна Рут", 'specid':specs[2].id},
            {'name': "ДИЗ-2", 'course': 2, 'curator': "Татьяна Рут", 'specid':specs[2].id}
        ]
        Group.insert_many(groups).execute()
        
        # create student
        groups = Group.select()
        students = [
            {'diplom': 1, 'fname': "Мортынюк", 'lname': "Алексей", 'enrollment': datetime.date(2023, 2, 7), 'status': "Очно", 'paid': 1, 'groupid': groups[0].id},
            {'diplom': 2, 'fname': "Назаров", 'lname': "Михаил", 'enrollment':datetime.date(2023, 2, 7), 'status': "Заочно", 'paid': 1, 'groupid':groups[0].id},
            {'diplom': 3, 'fname': "Кривич", 'lname': "Алёна", 'enrollment':datetime.date(2023, 2, 7), 'status': "Очно", 'paid': 1, 'groupid':groups[1].id},
            {'diplom': 4, 'fname': "Конский", 'lname': "Андрей", 'enrollment':datetime.date(2023, 2, 7), 'status': "Очно", 'paid': 1, 'groupid':groups[2].id},
            {'diplom': 5, 'fname': "Лурина", 'lname': "Маша", 'enrollment':datetime.date(2023, 2, 7), 'status': "Заочно", 'paid': 1, 'groupid':groups[2].id},
            {'diplom': 6, 'fname': "Невзорова", 'lname': "Алина", 'enrollment':datetime.date(2023, 2, 7), 'status': "Очно", 'paid': 1, 'groupid':groups[3].id},
            {'diplom': 7, 'fname': "Краснов", 'lname': "Юрий", 'enrollment':datetime.date(2023, 2, 7), 'status': "Очно", 'paid': 1, 'groupid':groups[3].id},
            {'diplom': 8, 'fname': "Ягодная", 'lname': "Олеся", 'enrollment':datetime.date(2023, 2, 7), 'status': "Очно", 'paid': 1, 'groupid':groups[3].id},
            {'diplom': 9, 'fname': "Фу", 'lname': "Нурьям", 'enrollment':datetime.date(2023, 2, 7), 'status': "Очно", 'paid': 1, 'groupid':groups[4].id},
            {'diplom': 10, 'fname': "Явиров", 'lname': "Владимир", 'enrollment':datetime.date(2023, 2, 7), 'status': "Заочно", 'paid': 1, 'groupid':groups[4].id},
            {'diplom': 11, 'fname': "Ягодин", 'lname': "Юлий", 'enrollment':datetime.date(2023, 2, 7), 'status': "Заочно", 'paid': 1, 'groupid':groups[5].id},
            {'diplom': 12, 'fname': "Лязгова", 'lname': "Химина", 'enrollment':datetime.date(2023, 2, 7), 'status': "Заочно", 'paid': 1, 'groupid':groups[5].id}
        ]
        Student.insert_many(students).execute()