
create table triangles(a integer, b integer, c integer);

insert into triangles(a, b, c)
values
(20, 20, 20),
(20, 20, 23),
(20, 21, 22),
(13, 14, 30),
(20, 20, 20),
(13, 14, 30)
;



select a, b, c,
case
when a + b < c or a + c < b or b + c < a then 'Not A Triangle'
when a = b and b = c and a = c then 'Equilateral'
when a = b or a = c or b = c then 'Isosceles'
else 'Scalene'
end
from triangles