USE 11am_pro;

SELECT * FROM students01;
SELECT * FROM subjects;


-- ALTER TABLE marks ADD COLUMN exam_date DATE;
-- ALTER TABLE marks ADD COLUMN exam_time TIME;
-- ALTER TABLE marks ADD COLUMN created_at DATETIME;

-- UPDATE marks SET exam_date = "2026-11-26" WHERE stu_id = 1;
-- UPDATE marks SET exam_time = NOW() WHERE stu_id = 1;
-- UPDATE marks SET created_at = NOW() WHERE stu_id = 1;
-- UPDATE marks SET exam_date = "2025-10-25" WHERE stu_id = 2;
-- UPDATE marks SET exam_date = "2024-10-25" WHERE stu_id = 3;
-- UPDATE marks SET exam_date = "2023-10-25" WHERE stu_id = 7;
-- UPDATE marks SET created_at = NOW() WHERE stu_id = 2;

-- SELECT * FROM marks WHERE YEAR(exam_date) = 2025;
-- SELECT * FROM marks WHERE MONTH(exam_date) = 11;
-- SELECT * FROM marks WHERE exam_date > DATE_SUB(CURDATE(), INTERVAL 2 YEAR) AND exam_date <= CURDATE();

-- SELECT * FROM marks;

-- SELECT UPPER(student_name) FROM students01;
-- SELECT LOWER(student_name) FROM students01;
-- SELECT LENGTH(student_name) FROM students01;
-- SELECT CONCAT(stu_id, " - ", student_name) AS concat_name FROM students01;
-- SELECT SUBSTRING(student_name, 1,3) FROM students01;
-- SELECT student_name, REPLACE(student_name, "a", "*") FROM students01;

SELECT UPPER(st.student_name) as student_name, m.marks,
	date_format(m.exam_date, "%d-%m-%Y") AS exam_date
    FROM students01 st
    INNER JOIN marks m ON m.stu_id = st.stu_id;