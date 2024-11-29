# Write your MySQL query statement below
select 
    Department.name as Department,
    Employee.name as Employee,
    Employee.salary as Salary
FROM
    Employee
JOIN
    Department ON Employee.departmentId = Department.id
WHERE 
    Employee.salary = (
        SELECT 
            MAX(e.salary) 
        FROM 
            Employee e 
        WHERE 
            e.departmentId = Employee.departmentId
    );

    

