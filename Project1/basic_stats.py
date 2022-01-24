# Author: Frank Shang
# Date: 06/24/2021
# Description: This program uses the import statistics to find the mean, median, and mode of a list of student objects.

import statistics

class Student:
  '''student class'''

  def __init__(self, name, grade):
    '''initializes all data members'''
    self._name = name
    self._grade = grade

  def get_grade(self):
    '''method that returns the grade of the student'''
    return self._grade

def basic_stats(students):
    '''function that uses the statistics module to find the mean, median, and mode of the incoming parameter list'''
    list_grades = []
    for student in students:
    #print(student.get_grade())
        list_grades.append(student.get_grade())
    print(list_grades)
    mean = statistics.mean(list_grades)
    median = statistics.median(list_grades)
    mode = statistics.mode(list_grades)
    tuple_stats = (mean, median, mode)
    return tuple_stats

#s1 = Student("Kyoungmin", 73)
#s2 = Student("Mercedes", 74)
#s3 = Student("Avanika", 78)
#s4 = Student("Marta", 74)

#student_list = [s1, s2, s3, s4]
#print(basic_stats(student_list))
