import datetime
from user.models import Student, Mentor, Language, Course

language1 = Language.objects.create(name="Python", months_to_learn=6)
language2 = Language.objects.create(name="Java Script", months_to_learn=6)
language3 = Language.objects.create(name="UX-UI", months_to_learn=2)

student1 = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
                                  work_study_place='School №13', has_own_notebook=True, preferred_os='windows')
student2 = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',
                                  work_study_place='TV', has_own_notebook=True, preferred_os='mac')
student3 = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='+0508312312',
                                  work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux')

mentor1 = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',
                                main_work=None, experience=datetime.date(year=2021, month=10, day=23))
mentor2 = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
                                main_work='University of Fort Collins',
                                experience=datetime.date(year=2010, month=9, day=18))


course1 = Course.student.set([student1, student2], through_defaults={'name': 'Python-21', 'language': 'Python',
                                'date_started': 'datetime.date(year=2022, month=8, day=1)','mentor': 'mentor2'})
course2 = Course.student.set([student3], through_defaults={'name': 'UXUI design-43', 'language': 'UX-UI design',
                                'date_started': 'datetime.date(year=2022, month=8, day=22)', 'mentor': 'mentor1'})
