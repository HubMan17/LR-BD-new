import datetime
import time
from PySide6 import QtCore, QtGui, QtWidgets
from Moduls.models import *

from UI.ui import Ui_Form

from Moduls.report import *

import UI.more_info_ui
import UI.find_info_ui

import UI.add_spec_ui
import UI.add_group_ui
import UI.add_stud_ui
import UI.add_rep_ui
import UI.add_arch_ui
import UI.choise_group_ui
import UI.report_more_func_ui
import UI.change_group_ui
import UI.add_stud_sheduls
import UI.add_disc_ui
import UI.add_teacher_ui
import UI.add_teach_disc_ui
import UI.more_info_qexam_ui
import UI.add_exam_ui
import UI.change_qexam_ui


class ChangePage2(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = parent
        
        # test = QtWidgets.QFileDialog.getOpenFileName()[0]
        # print(test)
        
        self.more_info_window = QtWidgets.QWidget()
        

        self.ui.comboBox_7.currentTextChanged.connect(self.show_table)
        self.ui.comboBox_7.currentTextChanged.connect(self.clear_com)
        self.ui.comboBox_8.currentTextChanged.connect(self.show_table)
        self.ui.comboBox_9.currentTextChanged.connect(self.show_table)
        self.ui.comboBox_11.currentTextChanged.connect(self.show_table)
        self.ui.pushButton_5.clicked.connect(self.more_info)
        self.ui.pushButton_6.clicked.connect(self.find_info)
        self.ui.pushButton_7.clicked.connect(self.add_new_data)
        self.ui.pushButton_8.clicked.connect(self.change_data)
        self.ui.pushButton_9.clicked.connect(self.delete_data)
        self.ui.pushButton_10.clicked.connect(self.create_rep)
        
        self.ui.lineEdit_5.textChanged[str].connect(self.dynamic_search)


    def create_rep(self):
        table = self.ui.comboBox_7.currentText()
        rep = self.ui.comboBox_10.currentText()
        
        if table == "Студенты":
            id = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())
            
            data = Student.select().join(Group).join(Spec).where(Student.id == id).get()

            if rep == "Справка об обучении":
                
                def bp():
                    student = str(data.fname).title() + " " + str(data.lname).title()
                    spec_name = data.groupid.specid.name
                    date = str(data.enrollment).split('-')
                    open_status = self.ui_choice.checkBox.isChecked()
                    print_status = self.ui_choice.checkBox_2.isChecked()
                    pdf_status = self.ui_choice.checkBox_3.isChecked()
                    email_status = self.ui_choice.checkBox_4.isChecked()
            
                                
                    about_student(student=student,
                                date=datetime.date(int(date[0]), int(date[1]), int(date[2])).strftime("%d.%m.%Y"),
                                spec=spec_name, id_rep=id,
                                open_status=open_status, print_status=print_status,
                                pdf_status=pdf_status, email_status=email_status,
                                more_stud_status=False)
                    
                    self.add_data_window.close()
                    
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tОтчёт №{id} успешно создан!\n")
                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                
                self.add_data_window = QtWidgets.QWidget()
                self.ui_choice = UI.report_more_func_ui.Ui_Form()
                self.ui_choice.setupUi(self.add_data_window)
                self.add_data_window.show() 
                self.ui_choice.pushButton.clicked.connect(bp)
                
                
            elif rep == "Карточка студента":
                
                def bp():
                    lname = data.lname.title()
                    fname = data.fname.title()
                    enroll = str(data.enrollment).split('-')
                    group = data.groupid.name
                    spec = data.groupid.specid.name
                    id_rep = id
                    diplom = int(data.diplom)
                    status = data.status.title()
                    course = data.groupid.course
                    open_status = self.ui_choice.checkBox.isChecked()
                    print_status = self.ui_choice.checkBox_2.isChecked()
                    pdf_status = self.ui_choice.checkBox_3.isChecked()
                    email_status = self.ui_choice.checkBox_4.isChecked()
                    
                    student_card(lname=lname, fname=fname,
                                enroll=datetime.date(int(enroll[0]), int(enroll[1]), int(enroll[2])).strftime("%d.%m.%Y"),
                                group=group, spec=spec, id_rep=id_rep,
                                diplom=diplom, status=status, course=course,
                                open_status=open_status, print_status=print_status,
                                pdf_status=pdf_status, email_status=email_status,
                                more_stud_status=False)
                    
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tОтчёт №{id} успешно создан!\n")
                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                    self.add_data_window.close()
                
                self.add_data_window = QtWidgets.QWidget()
                self.ui_choice = UI.report_more_func_ui.Ui_Form()
                self.ui_choice.setupUi(self.add_data_window)
                self.add_data_window.show() 
                self.ui_choice.pushButton.clicked.connect(bp)


        elif table == "Группы":
            
            def bp():
                group_name = self.ui_choice.comboBox.currentText()
                data = Student.select().join(Group).join(Spec).where(Group.name == group_name)
                open_status = self.ui_choice.checkBox.isChecked()
                print_status = self.ui_choice.checkBox_2.isChecked()
                pdf_status = self.ui_choice.checkBox_3.isChecked()
                email_status = self.ui_choice.checkBox_4.isChecked()

                cur_data = ""
                if rep == "Задолжность по группе":
                    
                    for i in data:
                        cur_data += i.fname + " " + i.lname + " " + str(int(i.groupid.specid.price) - int(i.paid)) + "\n"
                    
                    debt_group(group=group_name, data=cur_data,
                               open_status=open_status, print_status=print_status,
                                pdf_status=pdf_status, email_status=email_status,
                                more_stud_status=False)
                    
                    
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tОтчёт \"Задолжность по {group_name}\" успешно создан!\n")
                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                elif rep == "Наполнение группы":
                    count = data.count()
                    
                    for i in data:
                        cur_data += i.fname + " " + i.lname + "\n"
                    
                    student_list_of_group(group=group_name, data=cur_data, count=count,
                                        open_status=open_status, print_status=print_status,
                                        pdf_status=pdf_status, email_status=email_status,
                                        more_stud_status=False)
                    
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tОтчёт \"Наполнение группы {group_name}\" успешно создан!\n")
                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)

                self.add_data_window.close()

            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_choice = UI.choise_group_ui.Ui_Form()
            self.ui_choice.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            with db:
                tmp = Group.select()
                
                data = ["<--Не выбран-->"] 
                for i in tmp:
                    data.append(i.name)
                
                self.ui_choice.comboBox.addItems(data)
            
            self.ui_choice.pushButton.clicked.connect(bp)



    def delete_data(self):
        id = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())
    
        table = self.ui.comboBox_7.currentText()
        
        if table == "Специальности":
            # delete from session
            # diplom = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 1).text())
            # Session_sheet.delete().where(Session_sheet.diplom == diplom).execute()
            
            Spec.delete().where(Spec.id == id).execute()
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно удалена!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            
        elif table == "Квалификационный экзамен":
            Qualifying_exam.delete().where(Qualifying_exam.id == id).execute()
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно удалена!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            
        elif table == "Дисциплины":
            Discipline.delete().where(Discipline.id == id).execute()
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно удалена!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            
        elif table == "Преподаватели":
            Teacher.delete().where(Teacher.id == id).execute()
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно удалена!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            
        elif table == "Загрузка преподавателей":
            Teacher_discipline.delete().where(Teacher_discipline.id == id).execute()
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно удалена!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            
        elif table == "Преподаватели":
            Teacher.delete().where(Teacher.id == id).execute()
            
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно удалена!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            
        elif table == "Группы":
            stud_list = Student.select().join(Group).where(Group.id == id)
            
            # create report
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Создание приказов")
            msg.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok|
                        QtWidgets.QMessageBox.StandardButton.No
                        )
            msg.setText("Создать приказы на перевод студентов?")
            ret = msg.exec()
            
            if ret == 1024:
            
                if stud_list:
                    
                    def bp():
                        new_group = self.ui_del.comboBox.currentText()
                        old_group = Group.select().where(Group.id == id).get().name
                        rep_date = self.ui_del.lineEdit_3.text()
                        open_status = self.ui_del.checkBox.isChecked()
                        print_status = self.ui_del.checkBox_2.isChecked()
                        pdf_status = self.ui_del.checkBox_3.isChecked()
                        email_status = self.ui_del.checkBox_4.isChecked()
                        
                        new_group_id = Group.select().where(Group.name == new_group).get().id

                        link = QtWidgets.QFileDialog.getExistingDirectory()
                        
                        max_len = len(stud_list)
                        count = 1
                        
                        for i in stud_list:
                            
                            student = i.fname + " " + i.lname
                            id_rep = i.id
                            diplom = i.diplom
                            
                            cur_exp = rep_date.split('.')
                
                            # write table report 
                            data = [
                                {'lname': student, 'diplom': diplom,
                                'rep_date': datetime.date(int(cur_exp[2]), int(cur_exp[1]), int(cur_exp[0])),
                                'reason': 'Перевод'}
                            ]
                            
                            # create reports
                            if count == max_len:
                                change_group(old_group=old_group, new_group=new_group,
                                    student=student, id_rep=id_rep, link=link,
                                    diplom=diplom, rep_date=rep_date, more_stud_status=True,
                                    open_status=open_status, print_status=print_status,
                                    pdf_status=pdf_status, email_status=email_status,
                                    send_status=True)
                            else:
                                change_group(old_group=old_group, new_group=new_group,
                                    student=student, id_rep=id_rep, link=link,
                                    diplom=diplom, rep_date=rep_date, more_stud_status=True,
                                    open_status=open_status, print_status=print_status,
                                    pdf_status=pdf_status, email_status=email_status,
                                    send_status=False)

                            count += 1
                            Report.insert(data).execute()
                        
                        for i in stud_list:
                            Student.update(groupid = new_group_id).where(Student.id == i.id).execute()
                        
                        self.add_data_window.close()
                        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tПриказы о переводе созданы!\n")
                        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tОтчёты добавлены!\n")
                        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                        Group.delete().where(Group.id == id).execute()
                        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tГруппа '{old_group}' удалена!\n")
                        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                        self.show_table()
                    
                
                    self.add_data_window = QtWidgets.QWidget()
                    self.ui_del = UI.change_group_ui.Ui_Form()
                    self.ui_del.setupUi(self.add_data_window)
                    self.add_data_window.show() 
                    self.ui_del.pushButton.clicked.connect(bp)
                    self.ui_del.lineEdit_3.setInputMask("00.00.0000")
                    self.ui_del.lineEdit_3.setToolTip("ДД.ММ.ГГГГ")
                    self.ui_del.lineEdit_3.setToolTipDuration(-1)
                
                    with db:
                        groups = Group.select()
                        
                        group_names = ["<--Не выбрана-->"]
                        for group in groups:
                            
                            if group.id == id:
                                continue
                            else:
                                group_names.append(group.name)
                        self.ui_del.comboBox.addItems(group_names)    
                
                
                else:
                    old_group = Group.select().where(Group.id == id).get().name
                    Group.delete().where(Group.id == id).execute()
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tГруппа '{old_group}' удалена!\n")
                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                    self.show_table()
            
            
            
            # Group.delete().where(Group.id == id).execute()
            # self.msg_error("Удаление записи", "Запись успешно удалена!")
            
        elif table == "Студенты":
            
            def bp():
                temp_stud = Student.select().where(Student.id == id).get()
                
                rep_id = int(self.ui_add.lineEdit_9.text())
                diplom = int(self.ui_add.lineEdit_2.text())
                name = str(self.ui_add.lineEdit_4.text())
                enrollment = str(self.ui_add.lineEdit_5.text())
                expulsion = str(self.ui_add.lineEdit_8.text())
                course = int(self.ui_add.comboBox_3.currentText())
                specName = str(self.ui_add.comboBox.currentText())
                reason = str(self.ui_add.comboBox_2.currentText())
                open_status = self.ui_add.checkBox.isChecked()
                print_status = self.ui_add.checkBox_2.isChecked()
                pdf_status = self.ui_add.checkBox_3.isChecked()
                email_status = self.ui_add.checkBox_4.isChecked()
                
                cur_enr = enrollment.split('.')
                cur_exp = expulsion.split('.')
                
                # write table report 
                data = [
                    {'lname': name, 'diplom': diplom,
                     'rep_date': datetime.date(int(cur_exp[2]), int(cur_exp[1]), int(cur_exp[0])),
                     'reason': reason}
                ]
                Report.insert(data).execute()
                
                # write table archive 
                data = [
                    {'diplom': diplom, 'name': name, 
                     'enrollment': datetime.date(int(cur_enr[2]), int(cur_enr[1]), int(cur_enr[0])),
                     'expulsion': datetime.date(int(cur_exp[2]), int(cur_exp[1]), int(cur_exp[0])),
                     'course': course, 'specName': specName, 'reason': reason}
                ]
                Archive.insert(data).execute()
                
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно удалена!\n")
                
                
                # create report
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Создание отчёта")
                msg.setStandardButtons(
                            QtWidgets.QMessageBox.StandardButton.Ok|
                            QtWidgets.QMessageBox.StandardButton.No
                            )
                msg.setText("Создать приказ об отчислении студента?")
                ret = msg.exec()

                if ret == 1024:
                    group_name = Student.select().join(Group).where(Student.id == id).get().groupid.name
                    
                    delete_rep(student=name, id_rep=rep_id, group=group_name,
                               open_status=open_status, print_status=print_status,
                               pdf_status=pdf_status, email_status=email_status,
                               more_stud_status=False)
                    
                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tПриказ №{rep_id} успешно создан!\n")
                
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                Student.delete().where(Student.id == id).execute()
                self.add_data_window.close()
                self.show_table()
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_arch_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            self.ui_add.lineEdit_9.setMaxLength(4)
            self.ui_add.lineEdit_2.setMaxLength(6)
            self.ui_add.lineEdit_5.setInputMask("00.00.0000")
            self.ui_add.lineEdit_5.setToolTip("ДД.ММ.ГГГГ")
            self.ui_add.lineEdit_5.setToolTipDuration(-1)
            self.ui_add.lineEdit_8.setInputMask("00.00.0000")
            self.ui_add.lineEdit_8.setToolTip("ДД.ММ.ГГГГ")
            self.ui_add.lineEdit_8.setToolTipDuration(-1)
            
            with db:
                temp_stud = Student.select().join(Group).join(Spec).where(Student.id == id).get()
                
                self.ui_add.comboBox_3.addItem(str(temp_stud.groupid.course))
                self.ui_add.comboBox_2.addItems(["<--Не выбран-->", "Отчисление", "Перевод", "Академ. отпуск"])
                self.ui_add.comboBox.addItem(temp_stud.groupid.specid.name)
                
                    
                self.ui_add.lineEdit_2.setText(str(temp_stud.diplom))
                self.ui_add.lineEdit_4.setText(str(temp_stud.fname).title() + " " + str(temp_stud.lname).title())

                temp_date = str(temp_stud.enrollment).split('-')

                self.ui_add.lineEdit_5.setText(str(temp_date[2] + "." + temp_date[1] + "." + temp_date[0]))
                self.ui_add.lineEdit_8.setText(str(datetime.date.today().strftime("%d.%m.%Y")))
            
            self.ui_add.pushButton.clicked.connect(bp)
            
            
            # msg = QtWidgets.QMessageBox()
            # msg.setWindowTitle("Создание отчёта")
            # msg.setStandardButtons(
            #                QtWidgets.QMessageBox.StandardButton.Ok|
            #                QtWidgets.QMessageBox.StandardButton.No
            #                )
            # msg.setText("Создать приказ о зачислении студента?")
            # ret = msg.exec()

            # if ret == 1024:
            #     pass
                
            
            # Student.delete().where(Student.id == id).execute()
            # self.msg_error("Удаление записи", "Запись успешно удалена!")
            
        elif table == "Приказы":
            Report.delete().where(Report.id == id).execute()
            self.msg_error("Удаление записи", "Запись успешно удалена!")
            
        elif table == "Архив":
            Archive.delete().where(Archive.id == id).execute()
            self.msg_error("Удаление записи", "Запись успешно удалена!")

        self.show_table()


    def msg_error(self, title, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()
    

    def change_data(self): 
        id = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())
        id_change_data = self.ui.tableWidget_3.currentColumn()
        new_data = self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), id_change_data).text()
        
        if id_change_data == 0:
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tВы пытались изменить поле id! Поля с меткой id нельзя изменять!\n")
            self.show_table()
            return None
        
        
        table = self.ui.comboBox_7.currentText()
        
        if table == "Специальности":
            
            if id_change_data == 1:
                Spec.update(name = str(new_data).title()).where(Spec.id == id).execute()
            elif id_change_data == 2:
                Spec.update(price = int(new_data)).where(Spec.id == id).execute()
                
        elif table == "Квалификационный экзамен":
            
            def set_disc():
                
                spec_name = Spec.get(Spec.id == exam_data.specid).name
                if self.ui_change.comboBox.currentText() == spec_name:
                    list_disc = exam_data.list_of_spec.split(";")
                    list_disc.remove("")
                    text = ""
                    for i in list_disc:
                        disc_name = Discipline.get(Discipline.id == i).name
                        text += f"{disc_name};"
                    self.ui_change.textEdit.setPlainText(text)
                else:
                    self.ui_change.textEdit.clear()
                
                for i in reversed(range(self.ui_change.verticalLayout.count())): 
                    self.ui_change.verticalLayout.itemAt(i).widget().setParent(None)
                
                
                def foo(name, no):
                    if no == 2:
                        self.ui_change.textEdit.append(f"{name};")
                    
                    elif no == 0:
                        text = self.ui_change.textEdit.toPlainText()
                        text = text.replace(f"\n{name};", "")
                        
                        if f"{name};" in text:
                            text = text.replace(f"{name};\n", "")
                            text = text.replace(f"{name};", "")
                        
                        self.ui_change.textEdit.clear()
                        self.ui_change.textEdit.setPlainText(f"{text}")

                
                spec_id = Spec.get(Spec.name == self.ui_change.comboBox.currentText())
                
                list_disc = Discipline.select().where(Discipline.specid == spec_id.id)

                check_list_disc = self.ui_change.textEdit.toPlainText()
                for i in list_disc:
                    # print(i.name)
                    cheak_box = QtWidgets.QCheckBox(i.name)
                    self.ui_change.verticalLayout.addWidget(cheak_box)
                    
                    if i.name in check_list_disc:
                        cheak_box.setCheckState(QtCore.Qt.CheckState.Checked)
                    else:
                        cheak_box.setCheckState(QtCore.Qt.CheckState.Unchecked)
                    cheak_box.stateChanged.connect(
                        lambda no=1, name=i.name: foo(name, no)
                    ) 
                    
                    
            def bp():
                spec = self.ui_change.comboBox.currentText()
                
                name = self.ui_change.lineEdit_2.text()
                spec_id = Spec.get(Spec.name == spec).id
                
                list_of_disc = self.ui_change.textEdit.toPlainText()
                list_of_disc = list_of_disc.replace("\n", "")
                list_of_disc = list_of_disc.split(";")
                list_of_disc.pop()

                text = ""
                spec_id = Spec.get(Spec.name == self.ui_change.comboBox.currentText())

                for i in list_of_disc:
                    
                    try:
                        name_disc = Discipline.get(
                            Discipline.name == i,
                            Discipline.specid == spec_id.id
                        )
                        
                        text += str(name_disc.id) + ";"
                    except: pass
            
                Qualifying_exam.update(
                    name=name, specid=spec_id, list_of_spec=text
                    ).where(Qualifying_exam.id == exam_data.id).execute()
                self.add_data_window.close()
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tЗапись успешно обнавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_change = UI.change_qexam_ui.Ui_Form()
            self.ui_change.setupUi(self.add_data_window)
            self.add_data_window.show() 

            
            exam_data = Qualifying_exam.get(Qualifying_exam.id == id)
            
            self.ui_change.lineEdit_2.setText(exam_data.name)
            
            spec_name = Spec.select()
            cur_spec_name = Spec.get(Spec.id == exam_data.specid)
            
            self.ui_change.comboBox.addItems([i.name for i in spec_name])     
            self.ui_change.comboBox.setCurrentText(cur_spec_name.name)
            set_disc()          
                
            self.ui_change.comboBox.currentTextChanged.connect(set_disc)
            self.ui_change.pushButton.clicked.connect(bp)

            
                
        elif table == "Преподаватели":
            
            if id_change_data == 1:
                Teacher.update(name = str(new_data).title()).where(Teacher.id == id).execute()
        
        elif table == "Дисциплины":
            
            if id_change_data == 1:
                Discipline.update(name = str(new_data).title()).where(Discipline.id == id).execute()                             
                
        elif table == "Группы":
            
            if id_change_data == 1:
                Group.update(name = str(new_data).title()).where(Group.id == id).execute()
            elif id_change_data == 2:
                
                if new_data in ["1", "2", "3", "4"]:
                    Group.update(course = int(new_data)).where(Group.id == id).execute()
                else:
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНеверное значение! Проверьте правильность ввода!\n")
                    # self.msg_error("Изменение данных", "Неверное значение! Проверьте правильность ввода!")
                    self.show_table()
                    return None
                    
            if id_change_data == 3:
                Group.update(curator = str(new_data).title()).where(Group.id == id).execute()
            elif id_change_data == 4:
                
                with db:
                    temp_data = Spec.select()
                    
                    data = []
                    for i in temp_data:
                        data.append(int(i.id))
                
                    if int(new_data) in data:
                        Group.update(specid = int(new_data)).where(Group.id == id).execute()
                    else:
                        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНеверное значение! Проверьте правильность ввода!\n")
                        # self.msg_error("Изменение данных", "Неверное значение! Проверьте правильность ввода!")
                        self.show_table()
                        return None
                    
        elif table == "Студенты":
            
            if id_change_data == 1:
                Student.update(diplom = int(new_data)).where(Student.id == id).execute()
            elif id_change_data == 2:
                Student.update(fname = str(new_data).title()).where(Student.id == id).execute()
            elif id_change_data == 3:
                Student.update(lname = str(new_data).title()).where(Student.id == id).execute()
            elif id_change_data == 4:
                
                cur_data = new_data.split("-")
                Student.update(enrollment = datetime.date(int(cur_data[0]), int(cur_data[1]), int(cur_data[2]))).where(Student.id == id).execute()
            
            elif id_change_data == 5:
                
                if new_data in ["Очно", "Заочно"]:
                    Student.update(status = str(new_data).title()).where(Student.id == id).execute()
                else:
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНеверное значение! Проверьте правильность ввода!\n")
                    # self.msg_error("Изменение данных", "Неверное значение! Проверьте правильность ввода!")
                    self.show_table()
                    return None
            
            elif id_change_data == 6:
                Student.update(paid = int(new_data)).where(Student.id == id).execute()
            elif id_change_data == 7:
                with db:
                    temp_data = Group.select()
                    
                    data = []
                    for i in temp_data:
                        data.append(int(i.id))
                
                    if int(new_data) in data:                            
                        
                        def bp():
                            lname = self.ui_add.lineEdit_2.text()
                            diplom = int(self.ui_add.lineEdit_4.text())
                            rep_date = self.ui_add.lineEdit_5.text()
                            reason = str(self.ui_add.comboBox.currentText())
                            open_status = self.ui_add.checkBox.isChecked()
                            print_status = self.ui_add.checkBox_2.isChecked()
                            pdf_status =  self.ui_add.checkBox_3.isChecked()
                            email_status = self.ui_add.checkBox_4.isChecked()

                            with db:
                                
                                cur_date = rep_date.split('.')
                                
                                data = [
                                    {'lname': lname, 'diplom': diplom,
                                     'rep_date': datetime.date(int(cur_date[2]), int(cur_date[1]), int(cur_date[0])),
                                      'reason': reason,}
                                ]
                                
                                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() 
                                                         + f"{datetime.datetime.now()}\tИзменение поля произошло успешно!\n")                
                                
                                # create raport
                                msg = QtWidgets.QMessageBox()
                                msg.setWindowTitle("Создание отчёта")
                                msg.setStandardButtons(
                                            QtWidgets.QMessageBox.StandardButton.Ok|
                                            QtWidgets.QMessageBox.StandardButton.No
                                            )
                                msg.setText("Создать отчёт о переводе в другую группу?")
                                ret = msg.exec()

                                if ret == 1024:
                                    self.add_data_window.close()
                                    
                                    temp = Student.select().join(Group).where(Student.id == id)
                                    for i in temp:
                                        old_group = i.groupid.name                                        
                                    
                                    new_group = Group.select().where(Group.id == int(new_data)).get().name
                                    student = lname
                                    id_rep = int(self.ui_add.lineEdit_7.text())
                                    diplom = diplom
                                    rep_date = self.ui_add.lineEdit_5.text()
                                    
                                    change_group(old_group=old_group, new_group=new_group,
                                                 student=student, id_rep=id_rep,
                                                 diplom=diplom, rep_date=rep_date, more_stud_status=False,
                                                 open_status=open_status, print_status=print_status,
                                                 pdf_status=pdf_status, email_status=email_status)
                                    
                                    Report.insert(data).execute()
                                    self.add_data_window.close()
                                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tОтчёт №{id_rep} успешно создан!\n")
                                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                                    
                                else:
                                    self.add_data_window.close()
                                
                                Student.update(groupid = int(new_data)).where(Student.id == id).execute()
                                self.show_table()
                                return None
            
                        self.add_data_window = QtWidgets.QWidget()
                        self.ui_add = UI.add_rep_ui.Ui_Form()
                        self.ui_add.setupUi(self.add_data_window)
                        self.add_data_window.show() 
                        
                        self.ui_add.comboBox.addItem("Перевод")
                        self.ui_add.lineEdit_5.setInputMask("00.00.0000")            
                        self.ui_add.lineEdit_5.setToolTip("ДД.ММ.ГГГГ")
                        self.ui_add.lineEdit_5.setToolTipDuration(-1)
                        self.ui_add.lineEdit_7.setMaxLength(4)
                        
                        # write data in field
                        with db:
                            data = Student.get(Student.id == id)
                            
                            self.ui_add.lineEdit_2.setText(str(data.fname).title() + 
                                " " + str(data.lname).title())
                            self.ui_add.lineEdit_4.setText(str(data.diplom))
                            
                        self.ui_add.pushButton.clicked.connect(bp)
                        
                    else:
                        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНеверное значение! Проверьте правильность ввода!\n")
                        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                        # self.msg_error("Изменение данных", "Неверное значение! Проверьте правильность ввода!")
                        self.show_table()
                        return None
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                    
        elif table == "Приказы":
            
            if id_change_data == 1:
                Report.update(lname = str(new_data).title()).where(Report.id == id).execute()
            elif id_change_data == 2:
                Report.update(diplom = int(new_data)).where(Report.id == id).execute()
            elif id_change_data == 3:
                
                cur_data = new_data.split("-") 
                # cur_data = new_data.split("-") 
                Report.update(rep_date = datetime.date(int(cur_data[0]), int(cur_data[1]), int(cur_data[2]))).where(Report.id == id).execute()
            
            elif id_change_data == 4:
                Report.update(reason = str(new_data).title()).where(Report.id == id).execute()
        
        elif table == "Архив":
            
            if id_change_data == 1:
                Archive.update(diplom = int(new_data)).where(Archive.id == id).execute()
            elif id_change_data == 2:
                Archive.update(name = str(new_data).title()).where(Archive.id == id).execute()
            elif id_change_data == 3:
                
                # ???? cur_data = new_data.split("-" or "." or "/") 
                cur_data = new_data.split("-") 
                Archive.update(enrollment = datetime.date(int(cur_data[0]), int(cur_data[1]), int(cur_data[2]))).where(Archive.id == id).execute()
            
            elif id_change_data == 4:
                
                # ???? cur_data = new_data.split("-" or "." or "/") 
                cur_data = new_data.split("-") 
                Archive.update(expulsion = datetime.date(int(cur_data[0]), int(cur_data[1]), int(cur_data[2]))).where(Archive.id == id).execute()
                 
            elif id_change_data == 5:
                
                if new_data in ["1", "2", "3", "4"]:
                    Archive.update(course = int(new_data)).where(Archive.id == id).execute()
                else:
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНеверное значение! Проверьте правильность ввода!\n")
                    # self.msg_error("Изменение данных", "Неверное значение! Проверьте правильность ввода!")
                    self.show_table()
                    return None
                
            elif id_change_data == 6:
                
                with db:
                    temp_data = Spec.select()
                    
                    data = []
                    for i in temp_data:
                        data.append(str(i.name))
                        
                    if new_data in data:
                        Archive.update(specName = str(new_data).title()).where(Archive.id == id).execute() 
                    else:
                        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНеверное значение! Проверьте правильность ввода!\n")
                        # self.msg_error("Изменение данных", "Неверное значение! Проверьте правильность ввода!")
                        self.show_table()
                        return None 
                        
            elif id_change_data == 7:
                
                if str(new_data).lower() in ["отчисление", "перевод", "академ. отпуск"]:
                    Archive.update(reason = str(new_data).capitalize()).where(Archive.id == id).execute()
                else:
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНеверное значение! Проверьте правильность ввода!\n")
                    # self.msg_error("Изменение данных", "Неверное значение! Проверьте правильность ввода!")
                    self.show_table()
                    return None
        
        self.show_table()
        
        if table == "Студенты" and id_change_data == 7:
            return None
        else: 
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tИзменение поля произошло успешно!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            # msg = QtWidgets.QMessageBox()
            # msg.setWindowTitle("Изменение данных")
            # msg.setText("Изменение поля произошло успешно!")
            # msg.exec_()


    def add_new_data(self):
        table = self.ui.comboBox_7.currentText()
        
        if table == "Специальности":
            
            def bp():
                name = self.ui_add.lineEdit_2.text().capitalize()
                price = int(self.ui_add.lineEdit_4.text())
                
                with db:
                    data = [
                        {'name': name, 'price': price}
                    ]
                    Spec.insert(data).execute()
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_spec_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            self.ui_add.pushButton.clicked.connect(bp)
            
        elif table == "Квалификационный экзамен":
            # id = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())
            
            def set_disc():
                self.ui_add.textEdit.clear()
                
                for i in reversed(range(self.ui_add.verticalLayout.count())): 
                    self.ui_add.verticalLayout.itemAt(i).widget().setParent(None)
                
                
                def foo(name, no):
                    if no == 2:
                        self.ui_add.textEdit.append(f"{name};")
                    
                    elif no == 0:
                        text = self.ui_add.textEdit.toPlainText()
                        text = text.replace(f"\n{name};", "")
                        
                        if f"{name};" in text:
                            text = text.replace(f"{name};\n", "")
                            text = text.replace(f"{name};", "")
                        
                        self.ui_add.textEdit.clear()
                        self.ui_add.textEdit.setPlainText(f"{text}")

                
                spec_id = Spec.get(Spec.name == self.ui_add.comboBox.currentText())
                
                list_disc = Discipline.select().where(Discipline.specid == spec_id.id)

                for i in list_disc:
                    # print(i.name)
                    cheak_box = QtWidgets.QCheckBox(i.name)
                    self.ui_add.verticalLayout.addWidget(cheak_box)
                    cheak_box.stateChanged.connect(
                        lambda no=1, name=i.name: foo(name, no)
                    ) 
                    
                    
            def bp():
                name = self.ui_add.lineEdit_2.text()
                
                list_of_disc = self.ui_add.textEdit.toPlainText()
                list_of_disc = list_of_disc.replace("\n", "")
                list_of_disc = list_of_disc.split(";")
                list_of_disc.pop()

                
                text = ""
                spec_id = Spec.get(Spec.name == self.ui_add.comboBox.currentText())
                print(list_of_disc)
                for i in list_of_disc:
                    
                    try:
                        name_disc = Discipline.get(
                            Discipline.name == i,
                            Discipline.specid == spec_id.id
                        )
                        
                        text += str(name_disc.id) + ";"
                    except: pass
                    

                # print(text)
                
                Qualifying_exam.insert(
                    name=name, specid=spec_id, list_of_spec=text
                    ).execute()
                
                exam = Qualifying_exam.get(Qualifying_exam.name == name)
                stud = Student.select().join(Group).join(Spec).where(Spec.id == spec_id)
                for i in stud:
                    Session_qualifying_exam.insert(
                        q_examid=exam.id, specid=spec_id,
                        diplom=i.diplom, fname=i.fname, lname=i.lname
                        ).execute()
                                
                
                self.add_data_window.close()
            
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
                    
                    
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_exam_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            spec_name = Spec.select()
            
            self.ui_add.comboBox.addItem("<--Не выбрана-->")
            self.ui_add.comboBox.addItems([i.name for i in spec_name])     
            
            self.ui_add.comboBox.currentTextChanged.connect(set_disc)
            
            self.ui_add.pushButton.clicked.connect(bp)
            # def foo():
            #     print("press")
            
            # cheak_box = QtWidgets.QCheckBox("test", self)
            # self.ui_add.verticalLayout.addWidget(cheak_box)
            # cheak_box.stateChanged.connect(foo)
              
            
        elif table == "Преподаватели":
            
            def bp():
                name = self.ui_add.lineEdit_2.text().title()
                
                Teacher.insert(name=name).execute()
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
                
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_teacher_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            self.ui_add.pushButton.clicked.connect(bp)
            
        elif table == "Дисциплины":
            
            def bp():
                disc_name = self.ui_add.lineEdit_2.text().title()
                spec_name = self.ui_add.comboBox.currentText()
                start = self.ui_add.lineEdit_3.text()
                end = self.ui_add.lineEdit_6.text()
                
                spec_id = Spec.select(Spec.id).where(Spec.name == spec_name).get().id
                
                Discipline.insert(name=disc_name, specid=spec_id, start=start, end=end).execute()
                
                disc_id = Discipline.select(Discipline.id).where(
                        Discipline.name == disc_name,
                        Discipline.specid == spec_id
                    ).get().id
                Study_schedule.insert(iddisc=disc_id, idspec=spec_id, start=start, end=end).execute()
                
                stud = Session_sheet.select(Session_sheet.diplom, Session_sheet.fname, Session_sheet.lname)\
                    .distinct()
                    
                for item in stud:
                    Session_sheet.insert(
                        diplom=item.diplom, fname=item.fname, lname=item.lname,
                        iddisc=disc_id, idspec=spec_id, start=start, end=end
                        ).execute()
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
                
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_disc_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            self.ui_add.pushButton.clicked.connect(bp)
            
            self.ui_add.lineEdit_3.setInputMask("0")
            self.ui_add.lineEdit_6.setInputMask("0")
            self.ui_add.lineEdit_3.setToolTip("Число от 1 до 8")
            self.ui_add.lineEdit_6.setToolTip("Число от 1 до 8")
            self.ui_add.lineEdit_3.setToolTipDuration(-1)
            self.ui_add.lineEdit_6.setToolTipDuration(-1)
            
            specs = Spec.select(Spec.name)
            self.ui_add.comboBox.addItems([i.name for i in specs])
            
        
        elif table == "Загрузка преподавателей":
            
            def bp():
                spec_name = self.ui_add.comboBox.currentText()
                disc_name = self.ui_add.comboBox_2.currentText()
                name = self.ui_add.comboBox_3.currentText()
                
                teach_id = Teacher.select(Teacher.id).where(Teacher.name == name).get().id
                spec_id = Spec.select(Spec.id).where(Spec.name == spec_name).get().id
                disc_id = Discipline.select(Discipline.id).where(
                        Discipline.name == disc_name,
                        Discipline.specid == spec_id
                    ).get().id
                
                Teacher_discipline.insert(teachid=teach_id, discid=disc_id, specid=spec_id).execute()
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
                
            
            def set_disc():
                spec_id = Spec.select(Spec.id).where(Spec.name == self.ui_add.comboBox.currentText()).get().id
                
                disc = Discipline.select(Discipline.name).where(
                    Discipline.specid == spec_id
                    )
                self.ui_add.comboBox_2.clear()
                self.ui_add.comboBox_2.addItem("<--Не выбрана-->")
                self.ui_add.comboBox_2.addItems([i.name for i in disc])
                
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_teach_disc_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            self.ui_add.pushButton.clicked.connect(bp)
            
            self.ui_add.comboBox.setEditable(True)
            self.ui_add.comboBox_2.setEditable(True)
            self.ui_add.comboBox_3.setEditable(True)
            
            self.ui_add.comboBox.blockSignals(True)
            specs = Spec.select(Spec.name)
            self.ui_add.comboBox.addItem("<--Не выбрана-->")
            self.ui_add.comboBox.addItems([i.name for i in specs])
            self.ui_add.comboBox.blockSignals(False)
            
            self.ui_add.comboBox.currentTextChanged.connect(set_disc)
            
            self.ui_add.comboBox_2.addItem("<--Не выбрана-->")
            self.ui_add.comboBox_3.addItem("<--Не выбран-->")
            teachers = Teacher.select(Teacher.name)
            self.ui_add.comboBox_3.addItems([i.name for i in teachers])
            
            
        elif table == "Учебный график":
            
            def bp():
                name = self.ui_add.lineEdit_2.text().capitalize()
                price = int(self.ui_add.lineEdit_4.text())
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_stud_sheduls.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            def add_disc():
                spec = self.ui_add.comboBox_17.currentText()
                
            
            names = ["<--Не выбрана-->"]
            spec_name = Spec.select(Spec.name)
            for i in spec_name:
                names.append(i.name)
            
            self.ui_add.comboBox_17.addItems(names)
            
            self.ui_add.comboBox_17.currentTextChanged.connect(add_disc())
            
            self.ui_add.pushButton.clicked.connect(bp)
            
            
            
        elif table == "Группы":
            
            def bp():
                name = self.ui_add.lineEdit_2.text()
                course = int(self.ui_add.comboBox_2.currentText())
                curator = self.ui_add.lineEdit_6.text().title()
                
                global temp_id
                with db:
                    temp_id = Spec.select().where(Spec.name == str(self.ui_add.comboBox.currentText())).get()
                
                specid = temp_id.id
                
                with db:
                    data = [
                        {'name': name, 'course': course, 
                            'curator': curator, 'specid': specid}
                    ]
                    Group.insert(data).execute()
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_group_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            with db:
                specs = Spec.select()
                
                data =["<--Не выбран-->"]
                for i in specs:
                    data.append(i.name)
                self.ui_add.comboBox.addItems(data)
            
            self.ui_add.comboBox_2.addItems(["<--Не выбран-->", "1", "2", "3", "4"])            
            self.ui_add.pushButton.clicked.connect(bp)

        elif table == "Студенты":
            
            def bp():
                diplom = int(self.ui_add.lineEdit_2.text())
                fname = str(self.ui_add.lineEdit_4.text()).capitalize()
                lname = str(self.ui_add.lineEdit_8.text()).capitalize()
                enrollment = self.ui_add.lineEdit_6.text()
                status = str(self.ui_add.comboBox_2.currentText())
                paid = int(self.ui_add.lineEdit_10.text())
                open_status = self.ui_add.checkBox.isChecked()
                print_status = self.ui_add.checkBox_2.isChecked()
                pdf_status = self.ui_add.checkBox_3.isChecked()
                email_status = self.ui_add.checkBox_4.isChecked()
                
                rep_id = int(self.ui_add.lineEdit_13.text())
                
                global temp_id
                with db:
                    temp_id = Group.select().where(Group.name == str(self.ui_add.comboBox.currentText())).get()
                
                groupid = temp_id.id
                
                with db:
                    date = enrollment.split(".")
                    
                    data = [
                        {'diplom': diplom, 'fname': fname, 'lname': lname,
                            'enrollment': datetime.date(int(date[2]), int(date[1]), int(date[0])), 'status': status, 
                            'paid': paid,  'groupid': groupid}
                    ]
                
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Создание отчёта")
                msg.setStandardButtons(
                               QtWidgets.QMessageBox.StandardButton.Ok|
                               QtWidgets.QMessageBox.StandardButton.No
                               )
                msg.setText("Создать приказ о зачислении студента?")
                ret = msg.exec()

                if ret == 1024:
                    spec_name = Group.select().join(Spec).where(Group.id == groupid).get().specid.name
                    group_name = str(self.ui_add.comboBox.currentText())
                    
                    append_rep(student=fname + " " + lname, spec=spec_name, 
                               group=group_name, enrollment=enrollment, id_rep=rep_id,
                               open_status=open_status, print_status=print_status,
                               pdf_status=pdf_status, email_status=email_status,
                               more_stud_status=False)
                    
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tПриказ №{rep_id} успешно создан!\n")
                    self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                # add data in reports
                rep_name = fname + " " + lname
                rep_diplom = diplom
                rep_date = enrollment
                rep_reason = "Зачисление"
                
                date = enrollment.split(".")
                
                rep_data = [
                    {'lname': rep_name, 'diplom': rep_diplom,
                     'rep_date': datetime.date(int(date[2]), int(date[1]), int(date[0])),
                     'reason':rep_reason
                    }
                ]
                
                Report.insert(rep_data).execute()
                Student.insert(data).execute()
                
                
                # add new student in session table
                
                spec_id = Group.select().where(Group.name == str(self.ui_add.comboBox.currentText())).get().specid
                discs = Discipline.select().where(Discipline.specid == spec_id)
                for item in discs:
                    session_data = [
                        {
                        "diplom":diplom, "fname":fname, "lname":lname,
                        "iddisc":item.id, "idspec":item.specid,
                        "start":item.start, "end":item.end
                        }
                    ]
                    Session_sheet.insert(session_data).execute()
                
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_stud_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            with db:
                specs = Group.select()
                
                data =["<--Не выбран-->"]
                for i in specs:
                    data.append(i.name)
                self.ui_add.comboBox.addItems(data)

            self.ui_add.lineEdit_2.setMaxLength(6)
            self.ui_add.lineEdit_13.setMaxLength(4)
            self.ui_add.lineEdit_6.setInputMask("00.00.0000")            
            self.ui_add.lineEdit_6.setToolTip("ДД.ММ.ГГГГ")
            self.ui_add.lineEdit_6.setToolTipDuration(-1)
            
            self.ui_add.comboBox_2.addItems(["<--Не выбран-->", "Очно", "Заочно"])            
            self.ui_add.pushButton.clicked.connect(bp)
        
        elif table == "Приказы":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Новая запись")
            msg.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Ok
                )
            msg.setText("Ошибка! В данную таблицу нельзя добавить запись напрямую!")
            msg.exec()
            
            return None
            
            def bp():
                lname = str(self.ui_add.lineEdit_2.text()).capitalize()
                diplom = int(self.ui_add.lineEdit_4.text())
                rep_date = self.ui_add.lineEdit_5.text()
                reason = str(self.ui_add.comboBox.currentText())
                
                with db:
                    date = rep_date.split(".")
                    
                    data = [
                        {'lname': lname, 'diplom': diplom,
                            'rep_date': datetime.date(int(date[2]), int(date[1]), int(date[0])), 'reason': reason}
                    ]
                    Report.insert(data).execute()
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                
                self.show_table()
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_rep_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 

            self.ui_add.lineEdit_4.setMaxLength(6)
            self.ui_add.lineEdit_5.setInputMask("00.00.0000")            
            self.ui_add.lineEdit_5.setToolTip("ДД.ММ.ГГГГ")
            self.ui_add.lineEdit_5.setToolTipDuration(-1)
            
            self.ui_add.comboBox.addItems(["<--Не выбран-->", "Зачисление", "Перевод", "Отчисление"])            
            self.ui_add.pushButton.clicked.connect(bp)
            
            
        elif table == "Архив":
            # msg = QtWidgets.QMessageBox()
            # msg.setWindowTitle("Новая запись")
            # msg.setStandardButtons(
            #     QtWidgets.QMessageBox.StandardButton.Ok
            #     )
            # msg.setText("Ошибка! В данную таблицу нельзя добавить запись напрямую!")
            # msg.exec()
            
            def bp():
                diplom = int(self.ui_add.lineEdit_2.text())
                name = str(self.ui_add.lineEdit_4.text()).title()
                enrollment = self.ui_add.lineEdit_5.text()
                expulsion = self.ui_add.lineEdit_8.text()
                course = int(self.ui_add.comboBox_3.currentText())
                specName = str(self.ui_add.comboBox.currentText()).capitalize()
                reason = str(self.ui_add.comboBox_2.currentText())
                
                with db:
                    enrl_date = enrollment.split(".")
                    expul_date = expulsion.split(".")
                    
                    data = [
                        {'diplom': diplom, 'name': name, 
                            'enrollment': datetime.date(int(enrl_date[2]), int(enrl_date[1]), int(enrl_date[0])),
                            'expulsion': datetime.date(int(expul_date[2]), int(expul_date[1]), int(expul_date[0])),
                            'course': course, 'specName': specName, 'reason': reason}
                    ]
                    Archive.insert(data).execute()
                
                self.add_data_window.close()
                
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.datetime.now()}\tНовая запись успешно добавлена!\n")
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
                # msg = QtWidgets.QMessageBox()
                # msg.setWindowTitle("Новая запись")
                # msg.setStandardButtons(
                #     QtWidgets.QMessageBox.StandardButton.Ok
                #     )
                # msg.setText("Новая запись успешно добавлена!")
                # msg.exec()
                
                self.show_table()
            
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.add_arch_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 

            self.ui_add.lineEdit_2.setMaxLength(6)
            self.ui_add.lineEdit_5.setInputMask("00.00.0000")            
            self.ui_add.lineEdit_5.setToolTip("ДД.ММ.ГГГГ")
            self.ui_add.lineEdit_5.setToolTipDuration(-1)
            
            self.ui_add.lineEdit_8.setInputMask("00.00.0000")            
            self.ui_add.lineEdit_8.setToolTip("ДД.ММ.ГГГГ")
            self.ui_add.lineEdit_8.setToolTipDuration(-1)
            
            self.ui_add.comboBox_3.addItems(["<--Не выбран-->", "1", "2", "3", "4"])
            self.ui_add.comboBox_2.addItems(["<--Не выбран-->", "Отчислен", "Академ. отпуск", "Перевод"])     
            
            with db:
                temp_data = Spec.select()
                
                data = ["<--Не выбран-->"]
                for i in  temp_data:
                    data.append(i.name)
                    
                self.ui_add.comboBox.addItems(data)
                   
            self.ui_add.pushButton.clicked.connect(bp)

    
    def dynamic_search(self):
        find_str = self.ui.lineEdit_5.text()
        text = self.ui.tableWidget_3.findItems(find_str, QtCore.Qt.MatchFlag.MatchFixedString|QtCore.Qt.MatchFlag.MatchContains)
        for i in text:
            self.ui.tableWidget_3.setCurrentItem(i)
            self.ui.tableWidget_3.selectRow(self.ui.tableWidget_3.currentRow())

    
    def search(self, fild):
        text = self.ui.tableWidget_3.findItems(fild, QtCore.Qt.MatchFlag.MatchFixedString)
        
        for i in text:            
            self.ui.tableWidget_3.setCurrentItem(i)
            self.ui.tableWidget_3.selectRow(self.ui.tableWidget_3.currentRow())
    
    
    def find_info(self):
        self.find_info_window = QtWidgets.QWidget()
        self.ui_find = UI.find_info_ui.Ui_Form()
        self.ui_find.setupUi(self.find_info_window)
        self.find_info_window.show()
        
        if self.ui.comboBox_7.currentText() == "Специальности" or \
            self.ui.comboBox_7.currentText() == "Группы":
            
            def bp():
                find_id = self.ui_find.lineEdit_2.text()
                find_name = self.ui_find.lineEdit_4.text()
                
                self.search(find_id)
                self.search(find_name)
                self.find_info_window.close()        
                
            
            self.ui_find.lineEdit.setText("id")
            self.ui_find.lineEdit_3.setText("name")
            
            self.ui_find.lineEdit_5.setVisible(False)
            self.ui_find.lineEdit_6.setVisible(False)
            self.ui_find.lineEdit_7.setVisible(False)
            self.ui_find.lineEdit_8.setVisible(False)
        
            self.ui_find.pushButton.clicked.connect(bp)
            
        elif self.ui.comboBox_7.currentText() == "Студенты" or \
            self.ui.comboBox_7.currentText() == "Архив" or self.ui.comboBox_7.currentText() == "Приказы":
            
            def bp():
                find_id = self.ui_find.lineEdit_2.text()
                find_name = self.ui_find.lineEdit_4.text()
                find_diplom = self.ui_find.lineEdit_6.text()
                
                self.search(find_id)
                self.search(find_name)
                self.search(find_diplom)
                self.find_info_window.close()        
                
            
            self.ui_find.lineEdit.setText("id")
            self.ui_find.lineEdit_3.setText("diplom")
            self.ui_find.lineEdit_5.setText("name")
            
            self.ui_find.lineEdit_7.setVisible(False)
            self.ui_find.lineEdit_8.setVisible(False)
        
            self.ui_find.pushButton.clicked.connect(bp)
        
    
    def show_more_info(self, column_list, data):
        """Create table for needed info and column"""
        
        self.ui_ins = UI.more_info_ui.Ui_Form()
        self.ui_ins.setupUi(self.more_info_window)
        self.more_info_window.show()
                
        self.ui_ins.tableWidget.setRowCount(1)
        self.ui_ins.tableWidget.setColumnCount(len(column_list))
        self.ui_ins.tableWidget.setHorizontalHeaderLabels(
            column_list
        )
    
    
    def more_info(self):
        id = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())
        
        if self.ui.comboBox_7.currentText() == "Специальности":
            column_list = ["id", "name", "price", "countGroup", "countStudent"]
            
            with db:
                data = Spec.select().where(Spec.id == id)
                group_count = Group.select(Group.id).join(Spec).where(Spec.id == id).count()
                student_count = Student.select(Student.id).join(Group).join(Spec).where(Spec.id == id).count()
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.price)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(group_count)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(student_count)))
                
        elif self.ui.comboBox_7.currentText() == "Квалификационный экзамен":
        
            self.add_data_window = QtWidgets.QWidget()
            self.ui_add = UI.more_info_qexam_ui.Ui_Form()
            self.ui_add.setupUi(self.add_data_window)
            self.add_data_window.show() 
            
            exam_data = Qualifying_exam.get(Qualifying_exam.id == id)
            spec_name = Spec.get(Spec.id == exam_data.specid)
            
            all_spec_name = Spec.select()
            
            self.ui_add.comboBox.addItem(spec_name.name)            
            self.ui_add.lineEdit_2.setText(exam_data.name)
            
            text_disc_name = ""
            for i in exam_data.list_of_spec.split(";"):
                try:
                    disc_list_name = Discipline.get(
                        Discipline.id == i
                    )
                    
                    text_disc_name += f"{disc_list_name.name}; "
                
                except: pass

            self.ui_add.textEdit.setPlainText(text_disc_name)

                
        elif self.ui.comboBox_7.currentText() == "Группы":
            column_list = ["id", "name", "course", "curator", "specName", "countStudent"]
            
            with db:
                data = Group.select().where(Group.id == id)
                spec_name = Group.select().join(Spec).where(Group.id == id).get()
                student_count = Student.select(Student.id).join(Group).where(Group.id == id).count()
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.curator)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(spec_name.name)))
                self.ui_ins.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(student_count)))
                
        elif self.ui.comboBox_7.currentText() == "Студенты":
            column_list = ["id", "diplom", "fname", "lname",
                           "enrollment", "status", "paid", "groupName", "specName"]
            
            with db:
                data = Student.select().where(Student.id == id)
                group_name = Student.select().join(Group).where(Student.id == id).get()
                spec_name = Student.select().join(Group).join(Spec).where(Student.id == id).get()
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.fname)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui_ins.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(i.status)))
                self.ui_ins.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(i.paid)))
                self.ui_ins.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(str(group_name.groupid.name)))
                self.ui_ins.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem(str(spec_name.groupid.specid.name)))
            
        elif self.ui.comboBox_7.currentText() == "Приказы":
            column_list = ["id", "lname", "diplom", "rep_date", "reason"]
            
            with db:
                data = Report.select().where(Report.id == id)
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.rep_date)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(i.reason)))
               
        elif self.ui.comboBox_7.currentText() == "Архив":
            column_list = ["id", "diplom", "name", "enrollment",
                           "expulsion", "course", "specName", "reason"]
            
            with db:
                data = Archive.select().where(Archive.id == id)
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(i.expulsion)))
                self.ui_ins.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui_ins.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(i.specName)))
                self.ui_ins.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(str(i.reason)))
    
    
    def clear_com(self):
        """Clear old data from filter combobox for new data"""
        self.ui.comboBox_8.clear()
        self.ui.comboBox_9.clear()
        
    
    def press(self):
        table = self.ui.comboBox_7.currentText()
        
        id = str(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())
        value = self.ui.tableWidget_3.cellWidget(self.ui.tableWidget_3.currentRow(), self.ui.tableWidget_3.currentColumn()).currentText()
        print(f"row - {id}; value - {value}")
                    
                    
        if table == "Загрузка преподавателей":
            
            if self.ui.tableWidget_3.currentColumn() == 1:
            
                teac_id = Teacher.select().where(Teacher.name == value).get().id
                Teacher_discipline.update(teachid=teac_id).where(Teacher_discipline.id == id).execute()
                
            elif self.ui.tableWidget_3.currentColumn() == 2:
            
                dics_id = Discipline.select().where(Discipline.name == value).get().id
                Teacher_discipline.update(discid=dics_id).where(Teacher_discipline.id == id).execute()
    
        elif table == "Учебный график":
            column = self.ui.tableWidget_3.currentColumn()
            
            if value == "<--Не указано-->":
                value = "-"
            
            request = Study_schedule.select().where(Study_schedule.id == id).get()
            
            if column == 5: Study_schedule.update(sem1_o=value).where(Study_schedule.id == id).execute()
            if column == 6: Study_schedule.update(sem1_e=value).where(Study_schedule.id == id).execute()
            if column == 7: Study_schedule.update(sem2_o=value).where(Study_schedule.id == id).execute()
            if column == 8: Study_schedule.update(sem2_e=value).where(Study_schedule.id == id).execute()
            if column == 9: Study_schedule.update(sem3_o=value).where(Study_schedule.id == id).execute()
            if column == 10: Study_schedule.update(sem3_e=value).where(Study_schedule.id == id).execute()
            if column == 11: Study_schedule.update(sem4_o=value).where(Study_schedule.id == id).execute()
            if column == 12: Study_schedule.update(sem4_e=value).where(Study_schedule.id == id).execute()
            if column == 13: Study_schedule.update(sem5_o=value).where(Study_schedule.id == id).execute()
            if column == 14: Study_schedule.update(sem5_e=value).where(Study_schedule.id == id).execute()
            if column == 15: Study_schedule.update(sem6_o=value).where(Study_schedule.id == id).execute()
            if column == 16: Study_schedule.update(sem6_e=value).where(Study_schedule.id == id).execute()
            if column == 17: Study_schedule.update(sem7_o=value).where(Study_schedule.id == id).execute()
            if column == 18: Study_schedule.update(sem7_e=value).where(Study_schedule.id == id).execute()
            if column == 19: Study_schedule.update(sem8_o=value).where(Study_schedule.id == id).execute()
            if column == 20: Study_schedule.update(sem8_e=value).where(Study_schedule.id == id).execute()
            
        elif table == "Сессионная ведомость":
            column = self.ui.tableWidget_3.currentColumn()
            
            if value == "<--Не выбрана-->":
                value = "-"
            
            request = Session_sheet.select().where(Session_sheet.id == id).get()
            
            if column == 8: Session_sheet.update(sem1_o=value).where(Session_sheet.id == id).execute()
            if column == 9: Session_sheet.update(sem1_e=value).where(Session_sheet.id == id).execute()
            if column == 10: Session_sheet.update(sem2_o=value).where(Session_sheet.id == id).execute()
            if column == 11: Session_sheet.update(sem2_e=value).where(Session_sheet.id == id).execute()
            if column == 12: Session_sheet.update(sem3_o=value).where(Session_sheet.id == id).execute()
            if column == 13: Session_sheet.update(sem3_e=value).where(Session_sheet.id == id).execute()
            if column == 14: Session_sheet.update(sem4_o=value).where(Session_sheet.id == id).execute()
            if column == 15: Session_sheet.update(sem4_e=value).where(Session_sheet.id == id).execute()
            if column == 16: Session_sheet.update(sem5_o=value).where(Session_sheet.id == id).execute()
            if column == 17: Session_sheet.update(sem5_e=value).where(Session_sheet.id == id).execute()
            if column == 18: Session_sheet.update(sem6_o=value).where(Session_sheet.id == id).execute()
            if column == 19: Session_sheet.update(sem6_e=value).where(Session_sheet.id == id).execute()
            if column == 20: Session_sheet.update(sem7_o=value).where(Session_sheet.id == id).execute()
            if column == 21: Session_sheet.update(sem7_e=value).where(Session_sheet.id == id).execute()
            if column == 22: Session_sheet.update(sem8_o=value).where(Session_sheet.id == id).execute()
            if column == 23: Session_sheet.update(sem8_e=value).where(Session_sheet.id == id).execute()
    

            disc_name = self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 4).text()
            spec_name = self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 5).text()
            
            diplom = self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 1).text()
            spec_id = Spec.get(Spec.name == spec_name).id
            disc_id = Discipline.get(
                Discipline.name == disc_name,
                Discipline.specid == spec_id
                ).id
            
            list_qexam = Qualifying_exam.select().where(Qualifying_exam.specid == spec_id)
            for item in list_qexam:
                    
                # print(len(item.list_of_spec.split(";"))-1)
                for i in range(len(item.list_of_spec.split(";")) - 1):
                    
                    if str(disc_id) == item.list_of_spec.split(";")[i]:
                        
                        avg_count = 0
                        avg_sum = 0
                        request = Session_sheet.get(
                            Session_sheet.diplom == diplom,
                            Session_sheet.iddisc == disc_id
                        )
                        
                        list_grade = [request.sem1_o, request.sem1_e, request.sem2_o, request.sem2_e,
                            request.sem3_o, request.sem3_e, request.sem4_o, request.sem4_e,
                            request.sem5_o, request.sem5_e, request.sem6_o, request.sem6_e,
                            request.sem7_o, request.sem7_e, request.sem8_o, request.sem8_e]
                        
                        for s_grade in list_grade:
                            if s_grade != "-":
                                avg_sum += int(s_grade)
                                avg_count += 1
                                
                        
                        if avg_count != 0:
                            # print(f"avg grade = {avg_sum/avg_count}")    
                            avg_grade = avg_sum/avg_count
                        else:
                            avg_grade = "-"                    
                        
                        # print("yes")
                        if i == 0:
                            Session_qualifying_exam.update(grade1=avg_grade).where(
                                Session_qualifying_exam.diplom == diplom
                                ).execute()
                            
                        elif i == 1:
                            Session_qualifying_exam.update(grade2=avg_grade).where(
                                Session_qualifying_exam.diplom == diplom
                                ).execute()
                            
                        elif i == 2:
                            Session_qualifying_exam.update(grade3=avg_grade).where(
                                Session_qualifying_exam.diplom == diplom
                                ).execute()
                            
                        elif i == 3:
                            Session_qualifying_exam.update(grade4=avg_grade).where(
                                Session_qualifying_exam.diplom == diplom
                                ).execute()

                        elif i == 4:
                            Session_qualifying_exam.update(grade5=avg_grade).where(
                                Session_qualifying_exam.diplom == diplom
                                ).execute()


                        request = Session_qualifying_exam.get(
                            Session_qualifying_exam.diplom == diplom
                        )
                        
                        list_grade = [request.grade1, request.grade2, request.grade3,
                                      request.grade4, request.grade5]
                        
                        avg_count = 0
                        avg_sum = 0
                        for grade in list_grade:
                            
                            if grade not in [None, "", "-"]:
                                avg_sum += float(grade)
                                avg_count += 1
                                print("yes")
                        
                        avg_grade = round(avg_sum / avg_count, 1)
                        Session_qualifying_exam.update(average_grade=avg_grade).where(
                                Session_qualifying_exam.diplom == diplom
                                ).execute()
                        
                        Session_qualifying_exam.update(recommend_grade=round(avg_grade)).where(
                                Session_qualifying_exam.diplom == diplom
                                ).execute()
    
        elif table == "Дисциплины":
            column = self.ui.tableWidget_3.currentColumn()
            
            if column == 2:
                
                spec_id = Spec.select(Spec.id).where(Spec.name == value).get().id
                Discipline.update(specid=spec_id).where(Discipline.id == id).execute()
                
            elif column == 3:
                Discipline.update(start=value).where(Discipline.id == id).execute()
                
                Study_schedule.update(start=value).where(Study_schedule.iddisc == id).execute()
                Session_sheet.update(start=value).where(Session_sheet.iddisc == id).execute()
                
            elif column == 4:
                Discipline.update(end=value).where(Discipline.id == id).execute()
                
                Study_schedule.update(end=value).where(Study_schedule.iddisc == id).execute()
                Session_sheet.update(end=value).where(Session_sheet.iddisc == id).execute()
            
        # self.show_table()
            
    
    def create_combobox(self, data, current_data):
        combobox = QtWidgets.QComboBox()
        combobox.blockSignals(True)
        combobox.addItems(data)
        combobox.setCurrentText(current_data)
        combobox.setEditable(True)
        combobox.blockSignals(False)
        
        combobox.currentTextChanged.connect(self.press)
        return combobox
    
        
    def show_table(self):
        
        if self.ui.comboBox_7.currentText() == "Специальности":
            self.ui.comboBox_10.clear()
            
            self.ui.lineEdit_8.setVisible(False)
            self.ui.comboBox_8.setVisible(False)

            self.ui.lineEdit_9.setVisible(False)
            self.ui.comboBox_9.setVisible(False) 
            
            with db:
                spec = Spec.select()
            column_list = ["id", "name", "price"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(spec.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in spec:
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.price)))
                count += 1
                
        elif self.ui.comboBox_7.currentText() == "Квалификационный экзамен":
            self.ui.comboBox_10.clear()
            
            self.ui.lineEdit_8.setVisible(False)
            self.ui.comboBox_8.setVisible(False)

            self.ui.lineEdit_9.setVisible(False)
            self.ui.comboBox_9.setVisible(False) 
            
            self.ui.lineEdit_17.setVisible(False)
            self.ui.comboBox_11.setVisible(False)
            
            with db:
                q_exam = Qualifying_exam.select()
            column_list = ["id", "name", "specid"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(q_exam.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in q_exam:
                spec_name = Spec.get(Spec.id == i.specid).name
                
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(spec_name)))
                count += 1
                
        elif self.ui.comboBox_7.currentText() == "Сессия квалификационный экзамен":
            self.ui.tableWidget_3.clear()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.tableWidget_3.setColumnCount(0)
            
            self.ui.comboBox_10.clear()
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Специальность")
            self.ui.comboBox_8.setVisible(True)

            self.ui.lineEdit_9.setVisible(True)
            self.ui.lineEdit_9.setText("Экзамен")
            self.ui.comboBox_9.setVisible(True) 
            
            def bp():
                spec_name = self.ui.comboBox_8.currentText()
                
                self.ui.comboBox_9.blockSignals(True)
                
                self.ui.comboBox_9.clear()
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
                disc = Qualifying_exam.select().join(Spec).where(Spec.name == spec_name)
                self.ui.comboBox_9.addItems([i.name for i in disc])
                
                self.ui.comboBox_9.blockSignals(False)
                
            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]:
                self.ui.comboBox_8.addItem("<--Не выбрана-->")
                specs = Spec.select(Spec.name)
                self.ui.comboBox_8.addItems([i.name for i in specs])
                
            if not [self.ui.comboBox_9.itemText(i) for i in range(self.ui.comboBox_9.count())]:
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
                
            self.ui.comboBox_8.currentTextChanged.connect(bp)
            

            if self.ui.comboBox_9.currentText() == "<--Не выбрана-->":            
                return None
            
            else:
                q_exam = Qualifying_exam.get(
                    Qualifying_exam.name == self.ui.comboBox_9.currentText()
                    )
                
                s_q_exam = Session_qualifying_exam.select().where(
                    Session_qualifying_exam.q_examid == q_exam.id
                )

                    
                column_list = ["id", "q_examid", "specid", "diplom", "fname", "lname"]
                
                disc = Discipline.select().where(Discipline.id == q_exam.list_of_spec)
                list_disc = []
                
                for i in range(len(q_exam.list_of_spec.split(";")) - 1):
                    disc = Discipline.get(Discipline.id == q_exam.list_of_spec.split(";")[i]).name
                    column_list.append(str(disc))
                
                for i in ["average", "recommend", "end"]:
                    column_list.append(str(i))
                
                
                
                count_column = 9 + len(q_exam.list_of_spec.split(";")) - 1
                
                self.ui.tableWidget_3.setColumnCount(count_column)
                self.ui.tableWidget_3.setRowCount(s_q_exam.count())
                self.ui.tableWidget_3.setHorizontalHeaderLabels(
                    column_list
                )
                
                
                count = 0
                for i in s_q_exam:
                    
                    grade_list = [i.grade1, i.grade2,
                                  i.grade3, i.grade4, i.grade5]
                    
                    self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                    self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.q_examid)))
                    self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.specid)))
                    self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.diplom)))
                    self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.fname)))
                    self.ui.tableWidget_3.setItem(count, 5, QtWidgets.QTableWidgetItem(str(i.lname)))
                    self.ui.tableWidget_3.setItem(count, len(column_list)-3, QtWidgets.QTableWidgetItem(str(i.average_grade)))
                    self.ui.tableWidget_3.setItem(count, len(column_list)-2, QtWidgets.QTableWidgetItem(str(i.recommend_grade)))
                    self.ui.tableWidget_3.setItem(count, len(column_list)-1, QtWidgets.QTableWidgetItem(str(i.end_grad)))


                    if i.average_grade is None:
                        self.ui.tableWidget_3.setItem(count, len(column_list)-3, QtWidgets.QTableWidgetItem(str("-")))
                    else:
                        self.ui.tableWidget_3.setItem(count, len(column_list)-3, QtWidgets.QTableWidgetItem(str(i.average_grade)))

                    if i.recommend_grade is None:
                        self.ui.tableWidget_3.setItem(count, len(column_list)-2, QtWidgets.QTableWidgetItem(str("-")))
                    else:
                        self.ui.tableWidget_3.setItem(count, len(column_list)-2, QtWidgets.QTableWidgetItem(str(i.recommend_grade)))

                    if i.end_grad is None:
                        self.ui.tableWidget_3.setItem(count, len(column_list)-1, QtWidgets.QTableWidgetItem(str("")))
                    else:
                        self.ui.tableWidget_3.setItem(count, len(column_list)-1, QtWidgets.QTableWidgetItem(str(i.end_grad)))

                    grade_count = 0
                    for index in range(6, len(column_list) - 3):

                        if grade_list[grade_count] is None:
                            self.ui.tableWidget_3.setItem(count, index, QtWidgets.QTableWidgetItem(str("-")))
                        else:
                            self.ui.tableWidget_3.setItem(count, index, QtWidgets.QTableWidgetItem(str(grade_list[grade_count])))
                        grade_count += 1     
                        # print(grade_list[grade_count])
                    

                    count += 1
        
        elif self.ui.comboBox_7.currentText() == "Преподаватели":
            
            self.ui.tableWidget_3.clear()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.tableWidget_3.setColumnCount(0)
            
            self.ui.lineEdit_8.setVisible(False)
            self.ui.comboBox_8.setVisible(False)

            self.ui.lineEdit_9.setVisible(False)
            self.ui.comboBox_9.setVisible(False) 
            
            with db:
                spec = Teacher.select()
            column_list = ["id", "name"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(spec.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in spec:
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                count += 1
                
        elif self.ui.comboBox_7.currentText() == "Дисциплины":
            
            self.ui.tableWidget_3.clear()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.tableWidget_3.setColumnCount(0)
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Специальности")
            self.ui.comboBox_8.setVisible(True)
            
            # self.ui.comboBox_8.clear()
            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]:
                self.ui.comboBox_8.addItems(["<--Не выбрана-->"])
                
                spec = Spec.select()
                spec_list = [i.name for i in spec]
                self.ui.comboBox_8.addItems(spec_list) 

            self.ui.lineEdit_9.setVisible(False)
            self.ui.comboBox_9.setVisible(False) 
            
            if self.ui.comboBox_8.currentText() == "<--Не выбрана-->":
                return None
            
            else:
                spec_name = self.ui.comboBox_8.currentText()
            
                with db:
                    disc = Discipline.select().join(Spec).where(Spec.name == spec_name)
                column_list = ["id", "name", "specid", "start", "end"]
                
                self.ui.tableWidget_3.setColumnCount(len(column_list))
                self.ui.tableWidget_3.setRowCount(disc.count())
                self.ui.tableWidget_3.setHorizontalHeaderLabels(
                    column_list
                )
                
                count = 0
                
                spec_names = Spec.select(Spec.name)
                semesters = [str(i) for i in range(1, 10)]
                
                for i in disc:
                    spec_name = Spec.select().where(Spec.id == i.specid).get().name
                    
                    self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                    self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                    
                    # self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(spec_name)))
                    combobox = self.create_combobox([item.name for item in spec_names], spec_name)
                    self.ui.tableWidget_3.setCellWidget(count, 2, combobox)
                    
                    # self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.start)))
                    combobox = self.create_combobox(semesters, str(i.start))
                    self.ui.tableWidget_3.setCellWidget(count, 3, combobox)
                    
                    # self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.end)))
                    combobox = self.create_combobox(semesters, str(i.end))
                    self.ui.tableWidget_3.setCellWidget(count, 4, combobox)
                    
                    count += 1
                
        elif self.ui.comboBox_7.currentText() == "Загрузка преподавателей":
            
            self.ui.tableWidget_3.clear()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.tableWidget_3.setColumnCount(0)
            
            
            def data_set_disc():
                spec_name = self.ui.comboBox_8.currentText()
                
                self.ui.comboBox_9.blockSignals(True)
                
                self.ui.comboBox_9.clear()
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
                disc = Discipline.select().join(Spec).where(Spec.name == spec_name)
                self.ui.comboBox_9.addItems([i.name for i in disc])
                
                self.ui.comboBox_9.blockSignals(False)
                
                
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Специальность")
            self.ui.comboBox_8.setVisible(True)
            
            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]:
            
                self.ui.comboBox_8.addItem("<--Не выбрана-->")
                spec = Spec.select()
                self.ui.comboBox_8.addItems([i.name for i in spec])
            self.ui.comboBox_8.currentTextChanged.connect(data_set_disc)
            
            self.ui.lineEdit_9.setVisible(True)
            self.ui.lineEdit_9.setText("Дисциплина")
            self.ui.comboBox_9.setVisible(True) 
            
            if not [self.ui.comboBox_9.itemText(i) for i in range(self.ui.comboBox_9.count())]:
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
            
            
            self.ui.lineEdit_17.setVisible(True)
            self.ui.lineEdit_17.setText("Преподаватель")
            self.ui.comboBox_11.setVisible(True)
            
            if not [self.ui.comboBox_11.itemText(i) for i in range(self.ui.comboBox_11.count())]:
                self.ui.comboBox_11.addItem("<--Не выбрана-->")
                teachers = Teacher.select()
                self.ui.comboBox_11.addItems([i.name for i in teachers])

            
            
            if self.ui.comboBox_8.currentText() != "<--Не выбрана-->" and \
                self.ui.comboBox_9.currentText() != "<--Не выбрана-->" and \
                    self.ui.comboBox_11.currentText() != "<--Не выбрана-->":
                spec = Teacher_discipline.select().join(Teacher).switch(Teacher_discipline).join(Discipline).join(Spec) \
                    .where(
                        Spec.name == self.ui.comboBox_8.currentText(),
                        Discipline.name == self.ui.comboBox_9.currentText(),
                        Teacher.name == self.ui.comboBox_11.currentText()
                        )
            
            elif self.ui.comboBox_8.currentText() != "<--Не выбрана-->" and \
                self.ui.comboBox_9.currentText() != "<--Не выбрана-->":
                spec = Teacher_discipline.select().join(Discipline).join(Spec) \
                    .where(
                        Spec.name == self.ui.comboBox_8.currentText(),
                        Discipline.name == self.ui.comboBox_9.currentText()
                        )
                    
            elif self.ui.comboBox_8.currentText() != "<--Не выбрана-->" and \
                self.ui.comboBox_11.currentText() != "<--Не выбрана-->":
                spec = Teacher_discipline.select().join(Teacher).switch(Teacher_discipline).join(Discipline).join(Spec) \
                    .where(
                        Spec.name == self.ui.comboBox_8.currentText(),
                        Teacher.name == self.ui.comboBox_11.currentText()
                        )
                
            elif self.ui.comboBox_11.currentText() != "<--Не выбрана-->":
                spec = Teacher_discipline.select().join(Teacher) \
                    .where(Teacher.name == self.ui.comboBox_11.currentText())
            
            elif self.ui.comboBox_8.currentText() != "<--Не выбрана-->":
                spec = Teacher_discipline.select().join(Discipline).join(Spec) \
                    .where(Spec.name == self.ui.comboBox_8.currentText())
            
            else:
                spec = Teacher_discipline.select()
            
            column_list = ["id", "teachid", "discid", "specid"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(spec.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            
            count = 0
            teach_names =  [i.name for i in Teacher.select()] 
            
            for i in spec:
                
                teach_name = Teacher.select().where(Teacher.id == i.teachid).get().name
                disc_name = Discipline.select().where(Discipline.id == i.discid).get().name
                spec_name = Spec.select().where(Spec.id == i.specid).get().name
                
                disc_names =  set([i.name for i in Discipline.select().where(Discipline.specid == i.specid)]) 
                
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                
                combobox = self.create_combobox(teach_names, teach_name)
                self.ui.tableWidget_3.setCellWidget(count, 1, combobox)
                
                combobox = self.create_combobox(disc_names, disc_name)
                self.ui.tableWidget_3.setCellWidget(count, 2, combobox)
                
                self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(spec_name)))
                count += 1
                
                
        elif self.ui.comboBox_7.currentText() == "Учебный график":
            """!!!!!!!!!!!!!!"""
            
            self.ui.tableWidget_3.clear()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.tableWidget_3.setColumnCount(0)
            
            
            def data_set_disc():
                spec_name = self.ui.comboBox_8.currentText()
                
                self.ui.comboBox_9.blockSignals(True)
                
                self.ui.comboBox_9.clear()
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
                disc = Discipline.select().join(Spec).where(Spec.name == spec_name)
                self.ui.comboBox_9.addItems([i.name for i in disc])
                
                self.ui.comboBox_9.blockSignals(False)
            
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Специальности")
            self.ui.comboBox_8.setVisible(True)

            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]:
                self.ui.comboBox_8.addItem("<--Не выбрана-->")
                
                spec = Spec.select()
                spec_list = [i.name for i in spec]
                self.ui.comboBox_8.addItems(spec_list)
            self.ui.comboBox_8.currentTextChanged.connect(data_set_disc)
            
            
            self.ui.lineEdit_9.setVisible(True)
            self.ui.lineEdit_9.setText("Дисциплина")
            self.ui.comboBox_9.setVisible(True) 
            
            if not [self.ui.comboBox_9.itemText(i) for i in range(self.ui.comboBox_9.count())]:
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
            
            
            self.ui.lineEdit_17.setVisible(False)
            self.ui.comboBox_11.setVisible(False)

            
            if self.ui.comboBox_9.currentText() != "<--Не выбрана-->" and \
                self.ui.comboBox_8.currentText() != "<--Не выбрана-->":
                
                choice_current_spec = Spec.select().where(Spec.name == self.ui.comboBox_8.currentText()).get().name
                choice_current_disc = Discipline.select().where(Discipline.name == self.ui.comboBox_9.currentText()).get().name
                
                spec = Study_schedule.select().join(Discipline).join(Spec).where(
                    Spec.name == choice_current_spec,
                    Discipline.name == choice_current_disc
                )
                    
            
            elif self.ui.comboBox_8.currentText() != "<--Не выбрана-->":
                
                choice_current_spec = Spec.select().where(Spec.name == self.ui.comboBox_8.currentText()).get().id
                spec = Study_schedule.select().where(Study_schedule.idspec == choice_current_spec)
                # print("test")
            
            elif self.ui.comboBox_8.currentText() == "<--Не выбрана-->":
                return None
            
            
            column_list = ["id", "iddisc", "idspec", "start", "end",
                        "sem1_o", "sem1_e", "sem2_o", "sem2_e",
                        "sem3_o", "sem3_e", "sem4_o", "sem4_e",
                        "sem5_o", "sem5_e", "sem6_o", "sem6_e",
                        "sem7_o", "sem7_e", "sem8_o", "sem8_e"]
                
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(spec.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
                  
                  
            def check_status(data):
                data_for_combobox = ["<--Не указано-->", "Да", "Нет"]
                
                if data == '-':
                    result = data_for_combobox[0]
                elif data == data_for_combobox[1]:
                    result = data_for_combobox[1]
                elif data == data_for_combobox[2]:
                    result = data_for_combobox[2]
                return result
                  
                  
            data_for_combobox = ["<--Не указано-->", "Да", "Нет"]
            count = 0
            
            for i in spec:
                test_list = [i.sem1_o, i.sem1_e, i.sem2_o, i.sem2_e,
                         i.sem3_o, i.sem3_e, i.sem4_o, i.sem4_e,
                         i.sem5_o, i.sem5_e, i.sem6_o, i.sem6_e,
                         i.sem7_o, i.sem7_e, i.sem8_o, i.sem8_e]
                
                disc = Discipline.select().where(Discipline.id == i.iddisc).get().name
                spec = Spec.select().where(Spec.id == i.idspec).get().name
                
                
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(disc)))
                
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(spec)))
                self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.start)))
                self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.end)))
                
                count_exm = 0
                count_exm2 = 1
                for k in range(5, 21):
                    
                    if count_exm2 >= i.start and count_exm2 <= i.end + 0.5:
                        combobox = self.create_combobox(data_for_combobox, check_status(test_list[count_exm]))
                        self.ui.tableWidget_3.setCellWidget(count, k, combobox)
                    
                    else:
                        self.ui.tableWidget_3.setItem(count, k, QtWidgets.QTableWidgetItem("-"))
                    
                    count_exm += 1
                    count_exm2 += 0.5

                count += 1
            
        
        elif self.ui.comboBox_7.currentText() == "Сессионная ведомость":
            """!!!!!!!!!!!!!!"""
            
            self.ui.tableWidget_3.clear()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.tableWidget_3.setColumnCount(0)
            
            
            def data_set_group():
                spec_name = self.ui.comboBox_8.currentText()
                
                self.ui.comboBox_9.blockSignals(True)
                self.ui.comboBox_9.clear()
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
                groups = Group.select().join(Spec).where(Spec.name == spec_name)
                self.ui.comboBox_9.addItems([i.name for i in groups])
                self.ui.comboBox_9.blockSignals(False)
            
            
            def data_set_student():
                group_name = self.ui.comboBox_9.currentText()
                
                self.ui.comboBox_11.blockSignals(True)
                self.ui.comboBox_11.clear()
                self.ui.comboBox_11.addItem("<--Не выбрана-->")
                groups = Student.select().join(Group).where(
                    Group.name == group_name
                )
                self.ui.comboBox_11.addItems([f"{i.fname} {i.lname}" for i in groups])
                self.ui.comboBox_11.blockSignals(False)
            
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Специальности")
            self.ui.comboBox_8.setVisible(True)

            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]:
                self.ui.comboBox_8.addItem("<--Не выбрана-->")
                
                spec = Spec.select()
                spec_list = [i.name for i in spec]
                self.ui.comboBox_8.addItems(spec_list)
            self.ui.comboBox_8.currentTextChanged.connect(data_set_group)
            
            
            """!!!!!!!!!!!!!!"""
            self.ui.lineEdit_9.setVisible(True)
            self.ui.lineEdit_9.setText("Группы")
            self.ui.comboBox_9.setVisible(True) 
            
            if not [self.ui.comboBox_9.itemText(i) for i in range(self.ui.comboBox_9.count())]:
                self.ui.comboBox_9.addItem("<--Не выбрана-->")
            self.ui.comboBox_9.currentTextChanged.connect(data_set_student)
            
            self.ui.lineEdit_17.setVisible(True)
            self.ui.lineEdit_17.setText("Студенты")
            self.ui.comboBox_11.setVisible(True)
            
            if not [self.ui.comboBox_11.itemText(i) for i in range(self.ui.comboBox_11.count())]:
                self.ui.comboBox_11.addItem("<--Не выбрана-->")
            
            
            if self.ui.comboBox_11.currentText() != "<--Не выбрана-->":
                spec = Session_sheet.select().where(
                    Session_sheet.fname == self.ui.comboBox_11.currentText().split(" ")[0]
                )
            
            elif self.ui.comboBox_8.currentText() != "<--Не выбрана-->" and \
                self.ui.comboBox_9.currentText() != "<--Не выбрана-->":
                group_name = self.ui.comboBox_9.currentText()
                
                spec = Session_sheet.select().where(
                    Session_sheet.fname << [i.fname for i in Student.select(Student.fname).join(Group).where(Group.name == group_name)]
                )
                
                # spec = Session_sheet.select().where(
                #     Session_sheet.fname << ['Мортынюк', 'Назаров']
                # )

    
            elif self.ui.comboBox_8.currentText() != "<--Не выбрана-->":
                # spec = Session_sheet.select().join(Spec).where(
                #     Spec.name == self.ui.comboBox_8.currentText()
                # )
                return None
            
            elif self.ui.comboBox_8.currentText() == "<--Не выбрана-->":
                return None
            
            column_list = ["id", "diplom", "fname", "lname",
                           "iddisc", "idspec", "start", "end",
                           "sem1_o", "sem1_e", "sem2_o", "sem2_e",
                           "sem3_o", "sem3_e", "sem4_o", "sem4_e",
                           "sem5_o", "sem5_e", "sem6_o", "sem6_e",
                           "sem7_o", "sem7_e", "sem8_o", "sem8_e"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(spec.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            data_for_combobox = ["<--Не выбрана-->", "5", "4", "3", "2"]
            
            count = 0
            for i in spec:
                
                
                disc = Discipline.select().where(Discipline.id == i.iddisc).get().name
                spec = Spec.select().where(Spec.id == i.idspec).get().name
                
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.fname)))
                self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(disc)))
                self.ui.tableWidget_3.setItem(count, 5, QtWidgets.QTableWidgetItem(str(spec)))
                self.ui.tableWidget_3.setItem(count, 6, QtWidgets.QTableWidgetItem(str(i.start)))
                self.ui.tableWidget_3.setItem(count, 7, QtWidgets.QTableWidgetItem(str(i.end)))
                
                disc = Study_schedule.get(Study_schedule.iddisc == i.iddisc)
                disc_list = [disc.sem1_o, disc.sem1_e, disc.sem2_o, disc.sem2_e,
                         disc.sem3_o, disc.sem3_e, disc.sem4_o, disc.sem4_e,
                         disc.sem5_o, disc.sem5_e, disc.sem6_o, disc.sem6_e,
                         disc.sem7_o, disc.sem7_e, disc.sem8_o, disc.sem8_e]
                
                
                test_list = [i.sem1_o, i.sem1_e, i.sem2_o, i.sem2_e,
                         i.sem3_o, i.sem3_e, i.sem4_o, i.sem4_e,
                         i.sem5_o, i.sem5_e, i.sem6_o, i.sem6_e,
                         i.sem7_o, i.sem7_e, i.sem8_o, i.sem8_e]    
                count_exm = 0
                count_exm2 = 1
                for k in range(8, 24):
                    
                    if disc_list[k - 8] == "-":
                        self.ui.tableWidget_3.setItem(count, k, QtWidgets.QTableWidgetItem("-"))
                        # continue
                    
                    elif disc_list[k - 8] == "Да":
                        if count_exm2 >= i.start and count_exm2 <= i.end + 0.5:
                            if test_list[k - 8] == "5":
                                combobox = self.create_combobox(data_for_combobox, data_for_combobox[1])
                        
                            elif test_list[k - 8] == "4":
                                combobox = self.create_combobox(data_for_combobox, data_for_combobox[2])
                                
                            elif test_list[k - 8] == "3":
                                combobox = self.create_combobox(data_for_combobox, data_for_combobox[3])
                                
                            elif test_list[k - 8] == "2":
                                combobox = self.create_combobox(data_for_combobox, data_for_combobox[4])
                            
                            else:
                                combobox = self.create_combobox(data_for_combobox, data_for_combobox[0])
                                
                            self.ui.tableWidget_3.setCellWidget(count, k, combobox)
                        
                        # else:
                        #     self.ui.tableWidget_3.setItem(count, k, QtWidgets.QTableWidgetItem("да"))
                            
                    count_exm += 1
                    count_exm2 += 0.5
                count += 1
                    
            
        
        elif self.ui.comboBox_7.currentText() == "Группы":
            
            self.ui.comboBox_10.clear()
            if not [self.ui.comboBox_10.itemText(i) for i in range(self.ui.comboBox_10.count())]: 
                self.ui.comboBox_10.addItems(["<--Не выбран-->", "Задолжность по группе", "Наполнение группы"])
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Специальность")
            self.ui.comboBox_8.setVisible(True)
            
            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]: 
                data = ["<--Не выбран-->"]
                with db:
                    temp = Spec.select()
                    
                for i in temp:
                    data.append(i.name)    
                self.ui.comboBox_8.addItems(data)
            
            self.ui.lineEdit_9.setVisible(True)
            self.ui.lineEdit_9.setText("Курс")
            self.ui.comboBox_9.setVisible(True) 

            if not [self.ui.comboBox_9.itemText(i) for i in range(self.ui.comboBox_9.count())]: 
                self.ui.comboBox_9.addItems(["<--Не выбран-->", "1", "2", "3", "4"])
            
            with db:
                if self.ui.comboBox_8.currentText() != "<--Не выбран-->" and \
                    self.ui.comboBox_9.currentText() != "<--Не выбран-->":
                    groups = Group.select().join(Spec).where(
                        Spec.name == self.ui.comboBox_8.currentText(),
                        Group.course == int(self.ui.comboBox_9.currentText())
                    )
                
                elif self.ui.comboBox_8.currentText() != "<--Не выбран-->":
                    groups = Group.select().join(Spec).where(Spec.name == self.ui.comboBox_8.currentText())
                
                elif self.ui.comboBox_9.currentText() != "<--Не выбран-->":
                    groups = Group.select().where(Group.course == int(self.ui.comboBox_9.currentText()))
                 
                else:
                    groups = Group.select()
                
            column_list = ["id", "name", "course", "curator", "specid"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(groups.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in groups:
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.curator)))
                self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.specid)))
                count += 1
                
        elif self.ui.comboBox_7.currentText() == "Студенты":
            
            self.ui.comboBox_10.clear()
            if not [self.ui.comboBox_10.itemText(i) for i in range(self.ui.comboBox_10.count())]: 
                self.ui.comboBox_10.addItems(["<--Не выбран-->", "Карточка студента", "Справка об обучении"])
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Группа")
            self.ui.comboBox_8.setVisible(True)
            
            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]: 
                data = ["<--Не выбран-->"]
                with db:
                    temp = Group.select()
                    
                for i in temp:
                    data.append(i.name)    
                self.ui.comboBox_8.addItems(data)
            
            self.ui.lineEdit_9.setVisible(True)
            self.ui.lineEdit_9.setText("Тип обучения")
            self.ui.comboBox_9.setVisible(True) 
            if not [self.ui.comboBox_9.itemText(i) for i in range(self.ui.comboBox_9.count())]: 
                self.ui.comboBox_9.addItems(["<--Не выбран-->", "Очно", "Заочно"])
            
            with db:
                if self.ui.comboBox_8.currentText() != "<--Не выбран-->" and \
                    self.ui.comboBox_9.currentText() != "<--Не выбран-->":
                    students = Student.select().join(Group).where(
                        Group.name == str(self.ui.comboBox_8.currentText()),
                        Student.status == str(self.ui.comboBox_9.currentText())
                    )
                
                elif self.ui.comboBox_8.currentText() != "<--Не выбран-->":
                    students = Student.select().join(Group).where(Group.name == str(self.ui.comboBox_8.currentText()))
                
                elif self.ui.comboBox_9.currentText() != "<--Не выбран-->":
                    students = Student.select().where(Student.status == self.ui.comboBox_9.currentText())
                 
                else:
                    students = Student.select()
                
            column_list = ["id", "diplom", "fname", "lname", "enrollment",
                           "status", "paid", "groupid"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(students.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in students:
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.fname)))
                self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui.tableWidget_3.setItem(count, 5, QtWidgets.QTableWidgetItem(str(i.status)))
                self.ui.tableWidget_3.setItem(count, 6, QtWidgets.QTableWidgetItem(str(i.paid)))
                self.ui.tableWidget_3.setItem(count, 7, QtWidgets.QTableWidgetItem(str(i.groupid)))
                count += 1
                
        elif self.ui.comboBox_7.currentText() == "Приказы":
            self.ui.comboBox_10.clear()
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Причина")
            self.ui.comboBox_8.setVisible(True)
            
            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]: 
                data = ["<--Не выбран-->", "Зачисление", "Перевод", "Отчисление"]
                self.ui.comboBox_8.addItems(data)
            
            self.ui.lineEdit_9.setVisible(False)
            self.ui.comboBox_9.setVisible(False) 
            
            with db:
                if self.ui.comboBox_8.currentText() != "<--Не выбран-->":
                    reports = Report.select().where(Report.reason == str(self.ui.comboBox_8.currentText()))
                
                else:
                    reports = Report.select()
                
            column_list = ["id", "lname", "diplom", "rep_date", "reason"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(reports.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in reports:
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.rep_date)))
                self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.reason)))
                count += 1
                
        elif self.ui.comboBox_7.currentText() == "Архив":
            self.ui.comboBox_10.clear()
            
            self.ui.lineEdit_8.setVisible(True)
            self.ui.lineEdit_8.setText("Специальность")
            self.ui.comboBox_8.setVisible(True)
            
            if not [self.ui.comboBox_8.itemText(i) for i in range(self.ui.comboBox_8.count())]: 
                data = ["<--Не выбран-->"]
                with db:
                    temp = Spec.select()
                    
                for i in temp:
                    data.append(i.name)    
                self.ui.comboBox_8.addItems(data)
            
            self.ui.lineEdit_9.setVisible(True)
            self.ui.lineEdit_9.setText("Причина")
            self.ui.comboBox_9.setVisible(True) 
            if not [self.ui.comboBox_9.itemText(i) for i in range(self.ui.comboBox_9.count())]: 
                self.ui.comboBox_9.addItems(["<--Не выбран-->", "Отчисление", "Академ. отпуск", "Перевод"])
            
            with db:
                if self.ui.comboBox_8.currentText() != "<--Не выбран-->" and \
                    self.ui.comboBox_9.currentText() != "<--Не выбран-->":
                    archives = Archive.select().where(
                        Archive.specName == str(self.ui.comboBox_8.currentText()),
                        Archive.reason == self.ui.comboBox_9.currentText()
                    )
                
                elif self.ui.comboBox_8.currentText() != "<--Не выбран-->":
                    archives = Archive.select().where(Archive.specName == str(self.ui.comboBox_8.currentText()))
                
                elif self.ui.comboBox_9.currentText() != "<--Не выбран-->":
                    archives = Archive.select().where(Archive.reason == self.ui.comboBox_9.currentText())
                 
                else:
                    archives = Archive.select()
                
            column_list = ["id", "diplom", "name", "enrollment", "expulsion",
                           "course", "specName", "reason"]
            
            self.ui.tableWidget_3.setColumnCount(len(column_list))
            self.ui.tableWidget_3.setRowCount(archives.count())
            self.ui.tableWidget_3.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in archives:
                self.ui.tableWidget_3.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget_3.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui.tableWidget_3.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget_3.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui.tableWidget_3.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.expulsion)))
                self.ui.tableWidget_3.setItem(count, 5, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui.tableWidget_3.setItem(count, 6, QtWidgets.QTableWidgetItem(str(i.specName)))
                self.ui.tableWidget_3.setItem(count, 7, QtWidgets.QTableWidgetItem(str(i.reason)))
                count += 1