# School_timestable_model
A model that makes the optimal school timetable based on available classrooms and teachers.


## Goal

This model makes a timetable for a high school. Each high school has many teachers, students, courses and classrooms. The model makes a timetable such
all students know when to go to which class with which teacher assigned.

## POC situation
We are looking at making a school time table for one day which has 8 periods. We have classes (=groups of 30 students) that need to follow a specific set of courses (e.g. English, Math). The amount of hours per course differs per class (e.g. 2 hours of English, 1 hour of Math). Each course needs to be taught by one teacher in one classroom.

## Variables

* Teachers
* Classes (group of 30 children)
* Courses
* class rooms
* Hour of week / schooldays

## Constraints

* Each class has a list of courses to attend
* Each teacher can give a specific set of courses
* Each class can only follow one course at the same time
* One classroom can be assigned to one course at the same time
* One teacher can be assigned to one course at the same time
* Add later: use individual students instead of classes --> There is a max amount of students that can be assigned to each classroom at the same time
* Add later: One class/student needs multiple hours of the same course + One course for one student/class should always be given by the same teacher
* Add later: instead of one day we look at weekly schedule; ideally max one hour of the same cours each day

## Objective
* Points for each correctly assigned course
* Add later: Penalty for free period of student (tussenuur in Dutch) (minimize the amount of hours the student needs to be at school)
* Add later: Penalty for free period of teacher (mininmize the amount of hours the teacher needs to be at school)
* Add later: Penalty for double period (blokuur in Dutch)

## Modelling

1. POC: one day, set of courses, teachers, classes and classrooms
2. Add multiple days such that we make a full week schedule
3. Add same course needs to be given to some classes multiple times per week (e.g. 3 hours of Dutch, 2 hours of English etc)
4. Add not every classroom is suitable for every course (fixed rooms: music in music room, PE should be given in gym, maybe also add preferred rooms: english is usually given in the same room). Required classroom, preferred class room
5. Instead of clases; add that students with different set of courses instead of full classes of students

## Decision variables
Note that if we know that teacher A cannot give course B then all decision variables with A and B can be set to 0.
Note that if course C cannot be given in classroom D then all decision variables with C and D can be set to 0.





