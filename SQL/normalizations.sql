-- USE 11am_pro;

-- CREATE TABLE students01(
-- 	stu_id INT AUTO_INCREMENT PRIMARY KEY,
-- 	student_name VARCHAR(30) NOT NULL
-- );

-- CREATE TABLE subjects(
-- 	sub_id INT AUTO_INCREMENT PRIMARY KEY,
--     subject_name VARCHAR(30) NOT NULL
-- );

-- CREATE TABLE marks(
-- 	stu_id INT,
--     sub_id INT,
--     marks INT,
--     
--     PRIMARY KEY(stu_id, sub_id),
--     
-- 	FOREIGN KEY(stu_id) REFERENCES students01(stu_id),
--     FOREIGN KEY(sub_id) REFERENCES subjects(sub_id)
-- );


-- INSERT INTO students01(student_name)
-- VALUES
-- ("Ram"),("Sita"),("Ravan"),("Kansh"),("Shyam"),("Hanuman"),("Balveer");

-- INSERT INTO subjects(subject_name)
-- VALUES
-- ("Python"),("Node"),("React");

-- INSERT INTO marks(stu_id, sub_id, marks)
-- VALUES
-- (1, 3, 60), (2,2,85), (3,1,78),(1,2,63), (7, 3,58); 

-- SELECT * FROM students01;
-- SELECT * FROM subjects;
-- SELECT * FROM marks;

-- ALTER TABLE marks ADD CONSTRAINT FOREIGN KEY(stu_id) REFERENCES students01(stu_id) ON DELETE CASCADE;
-- ALTER TABLE marks ADD CONSTRAINT FOREIGN KEY(sub_id) REFERENCES subjects(sub_id) ON DELETE CASCADE;