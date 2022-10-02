drop table station;
create table station (id integer, city string, state string, lat_n number, long_w number);

insert into station(id, city, state, lat_n, long_w)
values
       (1, 'Dubai', 'UAE', 10.3544654, 20.879865),
       (2, 'Manhattan', 'USA', 5.654654, 30.5468465),
       (2, 'Paris', 'France', 19.651231658, 5.65432184)


-- abs(min(lat) - max(lat)) + abs(min(lon) - max(lon))

select sqrt((min(lat_n) + max(lat_n))*(min(lat_n) + max(lat_n))) + ((min(long_w) + max(long_w)))*((min(long_w) + max(long_w))) as sum from station;


select abs(trunc((min(lat_n)-min(long_w))+(max(lat_n)-max(long_w)),4)) from station;