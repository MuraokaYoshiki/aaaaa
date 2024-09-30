-- 例題0601　ex0601.sql
use sampledb;

-- (1)
DROP VIEW if exists emp_dep;
CREATE VIEW emp_dep AS
    SELECT kinmu_employee.s_id as s_id,
        kinmu_employee.l_name as l_name,
        kinmu_employee.f_name as f_name, 
        kinmu_employee.gender as gender,
        kinmu_employee.class as class,
        kinmu_depart.depart_name as depart_name 
    FROM kinmu_employee
    INNER JOIN kinmu_depart
    ON kinmu_employee.depart_id = kinmu_depart.depart_id
;

-- (2)
SELECT *
FROM emp_dep
WHERE gender = 1
AND class = '部長'
;

-- (3)
CREATE VIEW emp_dep_time AS
    SELECT kinmu_employee.s_id as s_id, 
        kinmu_employee.l_name as l_name, 
        kinmu_employee.f_name as f_name, 
        kinmu_depart.depart_name as depart_name,
        kinmu_timecard.r_date as r_date, 
        kinmu_timecard.work_time as work_time
    FROM kinmu_employee
    INNER JOIN kinmu_depart
    ON  kinmu_employee.depart_id = kinmu_depart.depart_id
    INNER JOIN kinmu_timecard
    ON kinmu_employee.s_id = kinmu_timecard.s_id
;

-- (4) 
SELECT *
FROM emp_dep_time
WHERE l_name = '木村'
AND f_name='一郎'
;

-- (5)
SELECT l_name,f_name,sum(work_time) as work200511
FROM emp_dep_time
WHERE l_name = '木村'
AND f_name='一郎'
AND r_date BETWEEN '2005-11-1' AND '2005-11-30'
GROUP BY s_id
;

-- (6)
SELECT s_id,l_name,f_name,sum(work_time) as work200511
FROM emp_dep_time
WHERE r_date BETWEEN '2005-11-1' AND '2005-11-30'
GROUP BY s_id
;



