USE 11am_pro;

SELECT * FROM students01;
SELECT * FROM subjects;
SELECT * FROM marks;
SELECT * FROM view;

-- SELECT st.stu_id AS student_id, st.student_name AS student_name, sb.subject_name AS subject_name, m.marks
-- 	FROM students01 st
--     INNER JOIN marks m ON m.stu_id = st.stu_id
--     INNER JOIN subjects sb ON sb.sub_id = m.sub_id;

-- SELECT st.stu_id AS student_id, st.student_name AS student_name, sb.subject_name AS subject_name, m.marks
-- 	FROM students01 st
--     RIGHT JOIN marks m ON m.stu_id = st.stu_id
--     LEFT JOIN subjects sb ON sb.sub_id  = m.sub_id;
    
-- SELECT st.stu_id AS student_id, st.student_name AS student_name, sb.subject_name AS subject_name, m.marks
-- 	FROM students01 st
-- 	LEFT OUTER JOIN marks m ON m.stu_id = st.stu_id
-- 	LEFT OUTER JOIN subjects sb ON sb.sub_id  = m.sub_id;
    
-- CREATE TABLE VIEW AS
-- SELECT st.stu_id AS student_id, st.student_name AS student_name, sb.subject_name AS subject_name, m.marks
-- 	FROM students01 st
--     INNER JOIN marks m ON m.stu_id = st.stu_id
-- 	INNER JOIN subjects sb ON sb.sub_id = m.sub_id
-- UNION 
-- SELECT st.stu_id AS student_id, st.student_name AS student_name, sb.subject_name AS subject_name, m.marks
-- 	FROM students01 st
--     LEFT JOIN marks m ON m.stu_id = st.stu_id
-- 	LEFT JOIN subjects sb ON sb.sub_id = m.sub_id;