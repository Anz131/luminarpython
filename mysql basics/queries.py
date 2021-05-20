database - collection of tables

banking project
1. create a database
rows, columns
id,name,designation,location,salary
1,ajay
records - each row
1 row = 1 record



create a database

mysql queries

>create database dbname;

>create database mycompany

query for listing all database
>show databases;

query for using a specific database
>use mycompany;

mysql query for creating table
>create table tablename(column name type, column name datatype,,,);

varchar => string array

>create table employee(eid varchar(23),ename varchar(25),desig varchar(25),salary int,exp int,location varchar(25));

>show tables;

display structure of table;

>desc employee;

insert record into tables

>insert into employee(eid,ename,desig,salary,exp,location) values('1000','Anu','Developer',25000,2,'Kannur');

>select * from employee;

fetching employee names

>select ename from employee;

fetch employee details whose salary>23000
>select * from employee where salary>23000;

fetch employee details who are working in kannur
>select * from employee where location='Kannur';

fetch employee details whose salary>23000 and exp>1
>select * from employee where salary>23000 and location='Kannur';


