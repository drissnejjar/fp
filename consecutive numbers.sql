--
-- +----+-----+
-- | id | num |
-- +-(-,----+
--) | (1,1),
-- | (2,1),
-- | (3,1),
-- | (4,2),
-- | (5,1),
-- | (6,2),
-- | (7,2),
-- +----+-----+

drop table logs;

create table logs(id integer, num integer);

insert into logs(id, num)
values(1,10),
(2,10),
(3,10),
(4,20),
(5,10),
(6,20),
(7,20),
(8,56),
(9,56),
(10,56),
       (11,56)


select l1.id, l1.num, l2.id, l2.num from logs l1, logs l2