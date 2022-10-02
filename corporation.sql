-- company_code
-- founder
-- total_lead
-- total_senior
-- total_managers
-- total_employees
--
-- company_code asc
--

create table company (company_code string, founder string);

create table lead_manager(lead_manager_code string, company_code string);

create table senior_manager(senior_manager_code string, lead_manager_code string, company_code string);

create table manager(manager_code string, senior_manager_code string, lead_manager_code string, company_code string);

create table employee(employee_code string, manager_code string, senior_manager_code string, lead_manager_code string, company_code string);


insert into company (company_code, founder) values ('C1', 'Monika'), ('C2', 'Samantha'), ('C10', 'Samantha');
insert into lead_manager(lead_manager_code, company_code) values ('LM1', 'C1'), ('LM2', 'C2');
insert into senior_manager(senior_manager_code, lead_manager_code, company_code) values ('SM1', 'LM1', 'C1'), ('SM2', 'LM1', 'C1'), ('SM3', 'LM2', 'C2');
insert into manager(manager_code, senior_manager_code, lead_manager_code, company_code) values ('M1', 'SM1', 'LM1', 'C1'), ('M2', 'SM3', 'LM2', 'C2'), ('M3', 'SM3', 'LM2', 'C2');
insert into employee(employee_code, manager_code, senior_manager_code, lead_manager_code, company_code)
values ('E1', 'M1', 'SM1', 'LM1', 'C1'), ('E2', 'M1', 'SM1', 'LM1', 'C1'), ('E3', 'M2', 'SM3', 'LM2', 'C2'), ('E4', 'M3', 'SM3', 'LM2', 'C2'), ('E4', 'M3', 'SM3', 'LM2', 'C10');

select c.company_code, lm.lead_manager_code, count(lead_manager_code) from company c
left join lead_manager lm on c.company_code = lm.company_code
group by 1,2;




select c.company_code, c.founder, count(distinct lm.lead_manager_code) as total_lead
     , count(distinct sm.senior_manager_code) as total_senior
     , count(distinct m.manager_code) as total_manager, count(distinct e.employee_code) as total_employee
from company c, lead_manager lm, senior_manager sm, manager m, employee e
where c.company_code = lm.company_code
and c.company_code = sm.company_code
and c.company_code = m.company_code
and c.company_code = e.company_code
group by 1,2
order by substr(c.company_code, 1) asc;

