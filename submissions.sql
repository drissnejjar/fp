drop table if exists submissions;

create table submissions(submission_date date, submission_id integer, hacker_id integer, score integer);

insert into submissions(submission_date, submission_id, hacker_id, score)
VALUES
        ('2016-03-01', 100, 10, 0),
       ('2016-03-01', 200, 12, 60),
        ('2016-03-02', 1, 10, 0),
        ('2016-03-02', 2, 11, 60),
        ('2016-03-02', 3, 12, 25),
        ('2016-03-02', 4, 12, 60);