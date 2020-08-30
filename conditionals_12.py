#Nested loop : Each student name and the number of subjects they are enrolled for
students = [
("John", ["CompSci", "Physics"]),
("Vusi", ["Maths", "CompSci", "Stats"]),
("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

for names,subjects in students :
    print(names, "takes", len(subjects), "courses")

# Count how many students are taking computer science
counter = 0
for names,subjects in students :
    for x in subjects :
        if x == "CompSci" :
            counter +=1

print("The number of students taking computer science is : ", counter)

times = 0
for names,subjects in students :
    if "CompSci" in subjects :
        times += 1

print("The number of students  taking Computer Science is :", times)

