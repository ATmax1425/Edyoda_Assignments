CREATE DATABASE assignment_1;
USE assignment_1;

CREATE TABLE SalesPeople (
    Snum INT,
    Sname VARCHAR(20) UNIQUE,
    City VARCHAR(20),
    Comm FLOAT,
    PRIMARY KEY (Snum)
);

CREATE TABLE Customers (
    Cnum INT,
    Cname VARCHAR(20),
    City VARCHAR(20) NOT NULL,
    Snum INT,
    PRIMARY KEY (Cnum),
    FOREIGN KEY (Snum)
        REFERENCES SalesPeople (Snum)
);

CREATE TABLE Orders (
    Onum INT,
    Amt FLOAT,
    Odate DATE,
    Cnum INT,
    Snum INT,
    PRIMARY KEY (Onum),
    FOREIGN KEY (Cnum)
        REFERENCES Customers (Cnum),
    FOREIGN KEY (Snum)
        REFERENCES SalesPeople (Snum)
);

INSERT INTO SalesPeople (Snum, Sname, City, Comm)
VALUES (1001, 'Peel', 'London', 0.12),
		(1002, 'Serres', 'Sanjose', 0.13),
		(1004, 'Motika', 'London', 0.11),
		(1007, 'Rifkin', 'Barcelona', 0.15),
		(1003, 'Axelrod', 'Newyork', 0.10);

INSERT INTO Customers (Cnum, Cname, City, Snum)
VALUES (2001, 'Hoffman', 'London', 1001),
		(2002, 'Giovanni', 'Rome', 1003),
		(2003, 'Liu', 'Sanjose', 1002),
		(2004, 'Grass', 'Berlin', 1002),
		(2006, 'Clemens', 'London', 1001),
		(2008, 'Cisneros', 'Sanjose', 1007),
		(2007, 'Pereira', 'Rome', 1004);

INSERT INTO Orders (Onum, Amt, Odate, Cnum, Snum)
VALUES	(3001, 18.69, STR_TO_DATE('3-10-1990', '%d-%m-%Y'), 2008, 1007),
		(3003, 767.19, STR_TO_DATE('3-10-1990', '%d-%m-%Y'), 2001, 1001),
		(3002, 1900.10, STR_TO_DATE('3-10-1990', '%d-%m-%Y'), 2007, 1004),
		(3005,  5160.45, STR_TO_DATE('3-10-1990', '%d-%m-%Y'), 2003, 1002),
		(3006,  1098.16, STR_TO_DATE('3-10-1990', '%d-%m-%Y'), 2008, 1007),
		(3009, 1713.23, STR_TO_DATE('4-10-1990', '%d-%m-%Y'), 2002, 1003),
		(3007, 75.75, STR_TO_DATE('4-10-1990', '%d-%m-%Y'), 2004, 1002),
		(3008, 4273.00, STR_TO_DATE('5-10-1990', '%d-%m-%Y'), 2006, 1001),
		(3010, 1309.95, STR_TO_DATE('6-10-1990', '%d-%m-%Y'), 2004, 1002),
		(3011, 9891.88, STR_TO_DATE('6-10-1990', '%d-%m-%Y'), 2006, 1001);
