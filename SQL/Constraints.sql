-- SHOW DATABASES;

-- CREATE DATABASE 11am_pro;
-- USE 11am_pro;

-- CREATE TABLE students(
-- 	stu_id INT AUTO_INCREMENT PRIMARY KEY,
--     stu_name VARCHAR(30) NOT NULL,
--     subjects VARCHAR(30) NOT NULL,
--     marks INT NOT NULL
--     );

-- INSERT INTO students(stu_name, subjects, marks)
-- VALUES
-- ("Ram", "Python", 90),
-- ("Shyam", "Node", 60),
-- ("Ganshyam", "React", 88),
-- ("Sita", "Python", 55),
-- ("Babita", "Node", 45),
-- ("Neeta", "Python", 78),
-- ("Ravan", "React", 69),
-- ("Hanuman", "Node", 58);


-- SELECT * FROM students;

-- SELECT subjects, AVG(marks) AS avg_marks FROM students GROUP BY subjects;
-- SELECT subjects, SUM(marks) AS sum_marks FROM students GROUP BY subjects;
-- SELECT subjects, MAX(marks) AS max_marks FROM students GROUP BY subjects;
-- SELECT subjects, SUM(marks) AS sum_marks_filter FROM students GROUP BY subjects HAVING AVG(marks) >= 70;
-- SELECT * FROM students WHERE marks >= 70;
-- SELECT * FROM students WHERE marks >= 70 AND marks <= 80;
-- SELECT * FROM students WHERE marks >= 70 OR marks <= 80;
-- SELECT * FROM students WHERE NOT marks <= 60;
-- SELECT * FROM students ORDER BY marks ASC;
-- SELECT * FROM students ORDER BY stu_name ASC;
-- SELECT * FROM students ORDER BY stu_name DESC;
-- SELECT * FROM students ORDER BY marks DESC;
SELECT * FROM students WHERE marks >= 60 LIMIT 2;