SELECT * FROM Customers;

-- order by ascending
SELECT * FROM Customers ORDER BY companyName ASC;
-- order by descending
SELECT * FROM Customers ORDER BY companyName DESC;

-- Ordering
-- order by price
SELECT * FROM products;
-- select the most expensive product
SELECT MAX(UnitPrice) AS most_expensive_product FROM products;

-- select the least expensive product
SELECT MIN(UnitPrice) AS least_expensive_product FROM products;

-- select the least expensive product
SELECT AVG(UnitPrice) FROM products;

--Give me the total number of products in the table
SELECT COUNT(*) FROM products;

-- ALIAS
SELECT COUNT(*) AS total_products FROM products;

-- Show only the first 5 : LIMIT 5
-- Show the first - første tal fortæller hvorfra i array vi starter - det andet tal, hvor mange vi fetcher
SELECT * FROM products LIMIT 0, 5;
-- GET 5 products, ordereb be cheapest to Highest
SELECT * FROM products ORDER BY UnitPrice ASC LIMIT 0, 5;

-- retrieve all data where contactnames starts with m, followed by anything else
SELECT * FROM customers WHERE ContactName LIKE "%er";
SELECT * FROM customers WHERE ContactName LIKE "%an%";



--JOIN to tabeller - we want to get all the orders and customers 
SELECT * FROM Customers;
SELECT * FROM Orders;
SELECT * FROM Products;
SELECT * FROM "order details";

SELECT * FROM Orders 
JOIN Customers 
ON orders.CustomerID = Customers.CustomerID
WHERE customers.CustomerID = "VINET"
LIMIT 0, 2;



