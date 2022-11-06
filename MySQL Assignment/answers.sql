# 1. Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT 
    COUNT(*)
FROM
    SalesPeople
WHERE
    Sname LIKE 'a%';

# 2. Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT 
    SalesPeople.Snum,
    SalesPeople.Sname,
    SalesPeople.City,
    SUM(Orders.Amt) AS all_order_worth
FROM
    SalesPeople JOIN Orders ON SalesPeople.Snum = Orders.Snum
GROUP BY SalesPeople.Snum
HAVING all_order_worth > 2000;

# 3. Count the number of Salesperson belonging to Newyork.
SELECT 
    COUNT(*)
FROM
    SalesPeople
WHERE
    City = 'Newyork';

# 4. Display the number of Salespeople belonging to London and belonging to Paris.
SELECT 
    city, COUNT(Sname)
FROM
    Salespeople
GROUP BY City
HAVING city IN ('London' , 'Paris');

# 5. Display the number of orders taken by each Salesperson and their date of orders.
SELECT 
	SalesPeople.Snum, 
	SalesPeople.Sname, 
	Orders.Odate, 
	count(*) OVER(PARTITION BY SalesPeople.Snum) AS number_of_orders
FROM 
	SalesPeople JOIN Orders ON SalesPeople.Snum = Orders.Snum;
