import os
import multiprocessing
import time
import shutil

from PySide6 import QtCore, QtGui, QtWidgets

from datetime import date
from docxtpl import DocxTemplate
from docx2pdf import convert

from Moduls.send_email import *
import Moduls.load_yadisk

def more_func(link, print_status, open_status,  pdf_status, email_status, title,
              send_status=None):
    
    
    if email_status or pdf_status:
        pdf_link = link.split('.')[0] + ".pdf"
        pdf_link = pdf_link.replace("Word", "Pdf")
        
        arch_link = pdf_link.split("\\")
        
        convert(link, pdf_link)
        
        if email_status:
            flink = f"{arch_link[0]}/{arch_link[1]}.zip"
            
            if send_status:
                shutil.make_archive(f"{arch_link[0]}/{arch_link[1]}", "zip", arch_link[0] + f"\{arch_link[1]}")
                                            
                if os.stat(flink).st_size >= 30000000:
                    link_disk = Moduls.load_yadisk.start_load(
                        flink,
                        arch_link[1],
                        f"{arch_link[1]}.zip"
                    )
                    start(rep_title=title, link_disk=link_disk)
                
                else:
                    start(rep_title=title, link_arch=flink)
        
    if print_status:
        os.startfile(link, "print")
    
    time.sleep(1)
    if open_status:
        os.startfile(link, "open")


def create_link(name_folder, pdf_status,
                email_status, more_stud_status,
                doc, file_name, link=None):
    
    def create_dir(link):
        try:
            os.mkdir(f"{link}\{name_folder}")
            os.mkdir(f"{link}\{name_folder}\Word")
            
            if pdf_status == True or email_status == True:
                os.mkdir(f"{link}\{name_folder}\Pdf")    
            
        except:
            pass
    
    if more_stud_status:
        create_dir(link=link)
        end_link = f"{link}\{name_folder}\Word\{file_name}.docx"
        doc.save(end_link)
    
    else:
        flink = QtWidgets.QFileDialog.getExistingDirectory()
        create_dir(link=flink)
        end_link = f"{flink}\{name_folder}\Word\{file_name}.docx"
        doc.save(end_link)

        
    return end_link


def debt_group(group, data, print_status, open_status, pdf_status, email_status,
               more_stud_status, link=None):
    
    today_date = date.today().strftime("%d.%m.%Y")

    doc = DocxTemplate(r"\LR BD new\Reports\Debt group.docx")
    context = {'group': group, 'date': today_date, 'data': data}
    doc.render(context)
    
    end_link = create_link(name_folder=f"Задолжности по группе {group}", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Задолжности по группе {group}")

    title = end_link.split('\\')[-1]
    multiprocessing.Process(target=more_func,
                            args=(end_link, print_status, open_status,
                                pdf_status, email_status, title, True
                            )).start()


def student_list_of_group(group, data, count, print_status, open_status, pdf_status, email_status,
                          more_stud_status, link=None):
    
    today_date = date.today().strftime("%d.%m.%Y")

    doc = DocxTemplate(r"\LR BD new\Reports\List of group.docx")
    context = {'group': group, 'date': today_date, 'data': data, 'count': count}
    doc.render(context)
    
    end_link = create_link(name_folder=f"Наполнение группы {group}", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Наполнение группы {group}")

    title = end_link.split('\\')[-1]
    multiprocessing.Process(target=more_func,
                            args=(end_link, print_status, open_status,
                                pdf_status, email_status, title, True
                            )).start()


def student_card(lname, fname, enroll, group, spec, id_rep, diplom, status, course,
                 print_status, open_status, pdf_status, email_status,
                 more_stud_status, link=None):
    
    today_date = date.today().strftime("%d.%m.%Y")

    doc = DocxTemplate(r"\LR BD new\Reports\Student card.docx")
    context = {'lname': lname, 'fname': fname,
               'diplom':diplom, 'status':status, 'enroll': enroll,
                'course':course, 'group': group, 'spec': spec, 'date': today_date}
    doc.render(context)
    
    end_link = create_link(name_folder=f"Карточка студента №{id_rep}", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Карточка студента №{id_rep}")

    title = end_link.split('\\')[-1]
    multiprocessing.Process(target=more_func,
                            args=(end_link, print_status, open_status,
                                pdf_status, email_status, title, True
                            )).start()


def about_student(student, date, spec, id_rep,
                  print_status, open_status, pdf_status, email_status,
                  more_stud_status, link=None):
    
    doc = DocxTemplate(r"\LR BD new\Reports\About studying.docx")
    context = { 'date' : date, 'student' : student, 'spec' : spec}
    doc.render(context)
    
    end_link = create_link(name_folder=f"Справка об обучении студента №{id_rep}", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Справка об обучении студента №{id_rep}")

    title = end_link.split('\\')[-1]
    multiprocessing.Process(target=more_func,
                            args=(end_link, print_status, open_status,
                                pdf_status, email_status, title, True
                            )).start()


def change_group(old_group, new_group, student, id_rep, diplom, rep_date,
                 print_status, open_status, pdf_status, email_status,
                 more_stud_status, link=None, send_status=None):
    
    today_date = date.today().strftime("%d.%m.%Y")

    doc = DocxTemplate(r"\LR BD new\Reports\Change report.docx")
    context = { 'date' : rep_date, 'student' : student,
               'old_group' : old_group, 'new_group': new_group,
               'diplom': diplom}
    doc.render(context)
    
    if more_stud_status:
        end_link = create_link(name_folder=f"Удаление группы {old_group}", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Приказ №{id_rep}", link=link)
        
        title = end_link.split('\\')[-3]
        multiprocessing.Process(target=more_func,
                                args=(end_link, print_status, open_status,
                                    pdf_status, email_status, title, send_status
                                )).start()
    
    else:
        end_link = create_link(name_folder=f"Перевод студента 'Приказ №{id_rep}'", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Приказ №{id_rep}", link=link)

        title = end_link.split('\\')[-3]
        multiprocessing.Process(target=more_func,
                                args=(end_link, print_status, open_status,
                                    pdf_status, email_status, title, True
                                )).start()
        

def append_rep(student, spec, group, enrollment, id_rep, open_status,
               print_status, pdf_status, email_status,
               more_stud_status, link=None):
    
    # today_date = date.today()
    
    doc = DocxTemplate(r"\LR BD new\Reports\Append report.docx")
    context = { 'date' : enrollment, 'student' : student, 'group' : group, 'spec': spec}
    doc.render(context)
    
    end_link = create_link(name_folder=f"Зачисление 'Приказ №{id_rep}'", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Приказ №{id_rep}")

    title = end_link.split('\\')[-1]
    multiprocessing.Process(target=more_func,
                            args=(end_link, print_status, open_status,
                                pdf_status, email_status, title, True
                            )).start()
        
    
    
def delete_rep(student, group, id_rep, open_status,
               print_status, pdf_status, email_status,
               more_stud_status, link=None):
    
    today_date = date.today().strftime("%d.%m.%Y")
    
    doc = DocxTemplate(r"\LR BD new\Reports\Delete report.docx")
    context = { 'date' : today_date, 'student' : student, 'group' : group}
    doc.render(context)
    
    end_link = create_link(name_folder=f"Отчисление 'Приказ №{id_rep}'", pdf_status=pdf_status,
                            email_status=email_status, more_stud_status=more_stud_status,
                            doc=doc, file_name=f"Приказ №{id_rep}")

    title = end_link.split('\\')[-1]
    multiprocessing.Process(target=more_func,
                            args=(end_link, print_status, open_status,
                                pdf_status, email_status, title, True
                            )).start()