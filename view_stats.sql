drop table view_stats;

create table view_stats(challenge_id integer, total_views integer, total_unique_views integer);

insert into view_stats(challenge_id, total_views, total_unique_views)
values
(33090,76,6),
(25505,68,15),
(7583,29,21)