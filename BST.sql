drop table if exists bst;

create table bst(N integer, P integer);

insert into bst(N, P)
values
       (1,2),
       (3,2),
       (6,8),
       (9,8),
       (2,5),
       (8,5),
       (5,null)
;

select
    case
        when p_id is null then 'Root'
        when id in (select p_id from tree) then 'Inner'
        else 'Leaf'
    end as type
from tree
order by id asc

