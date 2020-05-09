create database deviceDashboard;
USE deviceDashboard;

drop table if exists info;
create table info(
	ID int AUTO_INCREMENT primary key,
    grade int,
    class int,
    course int,
    useDate datetime,
    subject varchar(11),
    is_normal bool,
    description TEXT,
    user varchar(15)
) default charset=utf8; 