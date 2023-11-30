
--Query to Join Projects and Assignments for the starting page for a employee
SELECT 
project.id,project.p_id,project.name,project.company,project.start_date,project.end_date,project.fk_creator,project.creation_date, 
assignment.id,assignment.fk_project,assignment.fk_employee,assignment.role
FROM project
JOIN assignment ON project.id = assignment.fk_project
WHERE assignment.fk_employee = 2