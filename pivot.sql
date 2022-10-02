drop table geeksforgeeks;
Create Table geeksforgeeks
(
CourseName nvarchar(50),
CourseCategory nvarchar(50)
) ;

Insert into geeksforgeeks  values('C', 'PROGRAMMING')
Insert into geeksforgeeks  values('JAVA', 'PROGRAMMING')
Insert into geeksforgeeks  values('PYTHON', 'PROGRAMMING')
Insert into geeksforgeeks  values('PLACEMENT 100', 'INTERVIEWPREPARATION')

SELECT * FROM (
    select CourseName, CourseCategory from geeksforgeeks
    ) t pivot (

    )

