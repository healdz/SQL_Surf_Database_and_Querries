# Create Database
CREATE DATABASE SurfLesson;
USE surflesson;

# Create Tables
CREATE TABLE supplier (SupplierId int primary key,location varchar(50) not null,
NumberOfProductsSold int,EmployeeCount int);

CREATE TABLE SurfShop (BusinessID int primary key,Name varchar(50) not null,Location varchar(50) not null,
Rating int,EmployeeCount int,LessonCapacity int,Rentals varchar(3));

CREATE TABLE Instructors (InstructorID int primary key,Name varchar(50) not null,
Age int,Languages varchar(50) not null,Rating int,Private varchar(3),
YearsTeaching int,Location varchar(50) not null,HireDate int);

CREATE TABLE Clients (ClientID int primary key,Name varchar(50) not null,Age int,Languages varchar(50) not null,
HealthConcerns varchar(3) not null, SkillLevel int, FirstLesson varchar(3) not null ,GroupSize int);

CREATE TABLE Lessons (LessonID int primary key, Capacity int, Difficulty int, Private varchar(3) not null);

CREATE TABLE Schedules (BusinessID int, LessonID int, date int, FOREIGN KEY(BusinessID) REFERENCES SurfShop(BusinessID), 
FOREIGN KEY(LessonID) REFERENCES lessons(lessonID));

CREATE TABLE SurfsWith (InstructorID int, ClientID int, WaveSize varchar(50) not null, injuries varchar(3) not null, 
weather varchar(50) not null, tipAmount int, FOREIGN KEY(ClientID) REFERENCES Clients(ClientID), 
FOREIGN KEY(InstructorID) REFERENCES Instructors(InstructorID));

CREATE TABLE Teaches (InstructorID int, LessonID int, language varchar(50) not null, duration int, size int, 
FOREIGN KEY(InstructorID) REFERENCES instructors(InstructorID), 
FOREIGN KEY(LessonID) REFERENCES lessons(LessonID));

CREATE TABLE Employs (InstructorID int, BusinessID int, Wages int, hours int, contractor varchar(3) not null,
 FOREIGN KEY(BusinessID) REFERENCES SurfShop(BusinessID), 
 FOREIGN KEY(InstructorID) REFERENCES Instructors(InstructorID));
 
CREATE TABLE Reserves (LessonID int, ClientID int, PaymentType varchar(50) not null, price int, 
instructorRequest varchar(50) not null, date int, FOREIGN KEY(ClientID) REFERENCES Clients(ClientID), 
FOREIGN KEY(LessonID) REFERENCES lessons(LessonID));

CREATE TABLE Supplies (SupplierID int, BusinessID int, Cost int, time int, productType varchar(50) not null, 
FOREIGN KEY(BusinessID) REFERENCES SurfShop(BusinessID), 
FOREIGN KEY(SupplierID) REFERENCES supplier(supplierID));

#Load Data into Tables (From python data generator)
load data local infile 'tempSupplier.csv' into table supplier fields terminated by ',' lines terminated by '\n';
load data local infile 'tempClients.csv' into table clients fields terminated by ',' lines terminated by '\n';
load data local infile 'tempLessons.csv' into table lessons fields terminated by ',' lines terminated by '\n';
load data local infile 'tempSurfShop.csv' into table surfshop fields terminated by ',' lines terminated by '\n';
load data local infile 'tempInstructors.csv' into table instructors fields terminated by ',' lines terminated by '\n';
load data local infile 'relationSupplies.csv' into table supplies fields terminated by ',' lines terminated by '\n';
load data local infile 'relationSchedule.csv' into table schedules fields terminated by ',' lines terminated by'\n';
load data local infile 'relationEmploys.csv' into table employs fields terminated by ',' lines terminated by '\n';
load data local infile 'relationTeaches.csv' into table teaches fields terminated by ',' lines terminated by '\n';
load data local infile 'relationSurfsWith.csv' into table surfswith fields terminated by ',' lines terminated by '\n';
load data local infile 'relationReserves.csv' into table reserves fields terminated by ',' lines terminated by '\n';

