# Write your MySQL query statement below

# SELECT id, name, if(sex = 'f', 'm', 'f') as sex, salary FROM Salary;

# here you're updating the root table itself instead of printing values
UPDATE salary 
SET sex = IF(sex LIKE 'f', 'm', 'f');