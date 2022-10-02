drop table submission_stats;
create table submission_stats(challenge_id integer, total_submissions integer, total_accepted_submission integer);

insert into submission_stats(challenge_id, total_submissions, total_accepted_submission)
values
(1, 10, 5),
(1, 15, 5),
(2, 11, 2),
(2, 11, 2),
(3, 12, 35),
(3, 12, 35)
;