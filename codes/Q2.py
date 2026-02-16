2.Write a Python script that analyzes a text file containing student grades and generates a comprehensive report. (7 marks)
Input CSV Format:
csv
StudentID,Name,Math,Physics,Chemistry,Biology
S001,Alice Johnson,85,90,88,92
S002,Bob Smith,78,82,75,80
S003,Carol White,92,88,95,90
S004,David Brown,70,68,72,75

Requirements:
Read the CSV file
Create a class Student to store each student's information
Calculate individual student averages
Generate a report showing: 
 Total number of students
 Class average for each subject
 Overall class average
 Top 3 students by overall average
 Students who scored above 90 in any subject
 Subject-wise highest and lowest scores
 Handle file not found exceptions
Write formatted output to a text file

import csv

class Student:
 def __init__(self,student_id,name,math,physics,chemistry,biology):
   self.student_id=student_id
   self.name=name
   self.math=int(math)
   self.physics=int(math)
   self.chemistry=int(chemistry)
   self.biology=int(biology)

 def average(self):
  average=(self.math+self.physics+self.chemistry+self.biology)/4
  return average

students=[]

with open("students.csv","r") as f:
 reader=csv.reader(f)
 next(reader) #to skip first row

 for row in reader:
  student=Student(*row) #create objects and unpack arguments
  students.append(student) #append object to students list

 total_students=len(students)

 math_total=0
 physics_total=0
 chemistry_total=0
 biology_total=0

 for s in students:
  math_total+=s.math
  physics_total+=s.physics
  chemistry_total+=s.chemistry
  biology_total+=s.biology

 math_avg=math_total/total_students
 physics_avg=physics_total/total_students
 chemistry_avg=chemistry_total/total_students
 biology_avg=biology_total/total_students

 overall_class_avg=(math_avg+physics_avg+chemistry_avg+biology_avg)/4

 top_3=sorted(students,key=lambda x: x.average(),reverse=True)[:3]

 above_90=[]
 for s in students:
  if s.math>90 or s.physics>0 or s.chemistry>0 or s.biology>90 :
   above_90.append(s)

 math_scores=[]
 for s in students:
  math_scores.append(s.math)
  physics_scores=[s.physics for s in students]
  chemistry_scores=[s.chemistry for s in students]
  biology_scores=[s.biology for s in students]

with open("report.txt", "w") as rep:
  rep.write("----------- FINAL REPORT -----------\n")

  rep.write(f"Total number of students: {total_students}\n")

  rep.write("Class average per subject:\n")
  rep.write(f"Math average: {math_avg}\n")
  rep.write(f"Physics average: {physics_avg}\n")
  rep.write(f"Chemistry average: {chemistry_avg}\n")
  rep.write(f"Biology average: {biology_avg}\n")

  rep.write(f"Overall class average: {overall_class_avg}\n")

  rep.write("Top 3 students:\n")
  for s in top_3:
   rep.write(f"{s.name} ({s.student_id}) - Average: {s.average()}\n")

  rep.write("\nStudents Scoring Above 90 in Any Subject:\n")
  for s in above_90:
    rep.write(f"{s.name} ({s.student_id})\n")

  rep.write("\nSubject-wise Highest and Lowest Scores:\n")
  rep.write(f"Math: Highest={max(math_scores)}, Lowest={min(math_scores)}\n")
  rep.write(f"Physics: Highest={max(physics_scores)}, Lowest={min(physics_scores)}\n")
  rep.write(f"Chemistry: Highest={max(chemistry_scores)}, Lowest={min(chemistry_scores)}\n")
  rep.write(f"Biology: Highest={max(biology_scores)}, Lowest={min(biology_scores)}\n")
