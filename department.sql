-- +----+-------+--------+--------------+
-- ,id ,name  ,salary ,departmentId ,+----+-------+--------+--------------+
-- | (1,Joe,70000,1),
-- | (2,Jim,90000,1),
-- | (3,Henry,80000,2),
-- | (4,Sam,60000,2),
-- | (5,Max,90000,1),

drop table employee
create table employee (id integer ,name string ,salary integer ,departmentId integer)


insert into employee (id, name, salary, departmentId) VALUES
(1,'Joe',70000,1),
(2,'Jim',90000,1),
(3,'Henry',80000,2),
(4,'Sam',60000,2),
(5,'Max',90000,1)


create table department (id integer, name string)

insert into department (id, name) values
(1, 'IT'),
(2, 'Sales')




select b.name, a.Employee, a.salary as Salary
from
(select name as Employee, DepartmentId, salary, rank() over (partition by DepartmentId order by salary desc) as ord
from employee
) as a
left join department b
on a.departmentId = b.id
where a.ord = 1

select p.salary from (
                       select salary,
                              rank() over (partition by DepartmentId order by salary desc) as ord
                       from employee
                   ) p where ord > 1