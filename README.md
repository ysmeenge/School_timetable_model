# School_timestable_model
A model that makes the optimal school timetable based on available classrooms and teachers.


## Goal

This model makes a timetable for a high school. Each high school has many teachers, students, courses and classrooms. The model makes a timetable such
all students know when to go to which class with which teacher assigned.

## Variables

* Teachers
* Students or classes (group of 30 children)
* Courses
* class rooms
* Hour of week / schooldays

## Constraints

* Each student has a list of courses to attend
* Each teacher can give a specific set of courses
* Each student can only follow one course at the same time
* One classroom can be assigned to one course at the same time
* One teacher can be assigned to one classroom at the same time
* There is a max amount of students that can be assigned to each classroom at the same time
* One classroom can be used for one course at the same time
* One course for one student should always be given by the same teacher

## Objective
* Points for each correctly assigned course
* Add later: Penalty for free period of student (tussenuur in Dutch) (minimize the amount of hours the student needs to be at school)
* Add later: Penalty for free period of teacher (mininmize the amount of hours the teacher needs to be at school)
* Add later: Penalty for double period (blokuur in Dutch)

## Modelling

1. Start with: courses + one day
2. Add teachers
3. Add classrooms
4. Add students with different courses instead of full classes of students
5. Add multiple days such that we make a full week schedule
6. Add not every classroom is suitable for every course (fixed rooms: music in music room, PE should be given in gym, maybe also add preferred rooms: english is usually given in the same room). Required classroom, preferred class room.
7. Add same course needs to be given to a students multiple times per week (e.g. 3 hours of Dutch, 2 hours of English etc)



