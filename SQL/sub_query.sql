-- USE 11am_pro;

SELECT * FROM students01;
SELECT * FROM subjects;
SELECT * FROM marks;
-- SELECT * FROM view;

-- SELECT * FROM VIEW WHERE marks > (SELECT AVG(marks) FROM view);

-- SELECT student_name FROM students01 WHERE stu_id IN (SELECT stu_id FROM marks);

-- SELECT * FROM students01 st WHERE EXISTS (SELECT 1 FROM marks m WHERE st.stu_id = m.stu_id);

-- select student_name FROM students01 WHERE stu_id IN (
-- 	SELECT stu_id FROM marks WHERE marks = (
-- 		SELECT MIN(marks) FROM marks
--     )
-- );

SELECT st.stu_id, st.student_name, (
	SELECT SUM(m.marks) FROM marks m
		WHERE m.stu_id = st.stu_id
) AS total_marks from students01 st;