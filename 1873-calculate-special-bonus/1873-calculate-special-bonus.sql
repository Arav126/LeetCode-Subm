# Write your MySQL query statement below

# SELECT employee_id, if(salary%2=1 and name NOT LIKE 'M%', salary, 0) FROM Employees
# SELECT employee_id, if(employee_id%2=1 and name NOT LIKE 'M%', salary, 0) as bonus FROM Employees
SELECT employee_id, if(employee_id%2=1 and name NOT LIKE 'M%', salary, 0) as bonus FROM Employees
ORDER BY employee_id ;
