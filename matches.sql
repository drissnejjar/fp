create table teams (team_id integer, team_name string)

create table matches ( match_id integer, host_team integer, guest_team integer, host_goals integer, guest_goals integer)

insert into teams values (10, 'Give');
insert into teams values (20, 'Never');
insert into teams values (30, 'You');
insert into teams values (40, 'Up');
insert into teams values (50, 'Gonna');
insert into matches values (1, 30, 20, 1, 0);
insert into matches values (2, 10, 20, 1, 2);
insert into matches values (3, 20, 50, 2, 2);
insert into matches values (4, 10, 30, 1, 0);
insert into matches values (5, 30, 50, 0, 1);


with host_points as (
    select
            case
            when m.host_goals > m.guest_goals then 3
            when m.host_goals = m.guest_goals then 1
            when m.host_goals < m.guest_goals then 0
                else 0
        end as host_num_points,
           t.team_id,
           t.team_name
    from matches m
    full join teams t
        on m.host_team = t.team_id
),
 guest_points as (
     select
        case
            when m.host_goals < m.guest_goals then 3
            when m.host_goals = m.guest_goals then 1
            when m.host_goals > m.guest_goals then 0
            else 0
        end as guest_num_points,
            t.team_id,
            t.team_name
     from matches m
    full join teams t
        on m.guest_team = t.team_id
 )
   select team_id, team_name, sum(num_points) as num_points  from (
select team_id, team_name, sum(host_num_points) as num_points from host_points group by team_id
union all
select team_id, team_name, sum(guest_num_points) as num_points from guest_points
group by team_id) result
group by 1,2
order by num_points desc, team_id asc


