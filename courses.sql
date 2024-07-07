create database courses;
use courses;

create table subjects(
    course_id int primary key,
    course_name varchar (255),
    category varchar (255),
    instructor_id int
);

create table instructors(
    instructor_id int primary key,
    instructor_name varchar(255)
);

create table students(
    student_id int primary key,
    student_name varchar(255)
);

create table enrollments(
    enrollment_id int primary key,
    student_id int,
    course_id int,
    enrollment_date date,
    foreign key (student_id) references students(student_id),
    foreign key (course_id) references subjects(course_id)
);

INSERT INTO subjects (course_id, course_name, category, instructor_id) VALUES
(1, 'SQL for beginners', 'Programming', 1),
(2, 'Advanced Excel', 'Data Analysis', 2),
(3, 'Data Analysis with Python', 'Data Analysis', 2),
(4, 'Introduction to Machine Learning', 'Machine Learning', 1);

INSERT INTO instructors(instructor_id, instructor_name) VALUES
(1, 'John Doe'),
(2, 'Jane Smith');

INSERT INTO students (student_id, student_name) VALUES
(1, 'Alice Brown'),
(2, 'Bob Johnson'),
(3, 'Charlie Green'),
(4, 'David Lee'),
(5, 'Eva White');

INSERT INTO enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES
(1, 1, 1, '2024-01-15'),
(2, 2, 2, '2024-02-01'),
(3, 3, 1, '2024-03-10'),
(4, 4, 3, '2024-01-20'),
(5, 5, 2, '2024-02-15');
