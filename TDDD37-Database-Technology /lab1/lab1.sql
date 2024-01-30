#Deleting all views and tables
DROP TABLE IF EXISTS jbitemcopy;
DROP VIEW IF EXISTS jbitemcopy_view;
DROP VIEW IF EXISTS jb_debit_view;
DROP VIEW IF EXISTS jb_debit_view_v2;
DROP VIEW IF EXISTS jbsale_supply;

# task 1
SELECT * FROM jbemployee;

#task 2
SELECT NAME FROM jbdept ORDER BY NAME;

#task 3
SELECT NAME FROM jbitem  WHERE QOH = 0;

#task 4
SELECT NAME FROM jbemployee WHERE SALARY BETWEEN 9000 AND 10000;

#task 5
SELECT NAME, (STARTYEAR-BIRTHYEAR) AS AGE_WHEN_STARTED FROM jbemployee;

#task 6
SELECT NAME FROM jbemployee WHERE LOCATE("son,", NAME) != 0;

#task 7
SELECT NAME FROM jbitem WHERE SUPPLIER IN (SELECT ID FROM jbsupplier WHERE NAME = 'Fisher-Price');

#task 8
SELECT NAME FROM jbitem WHERE SUPPLIER = 89;

#task 9
SELECT NAME FROM jbcity WHERE ID IN (SELECT CITY FROM jbsupplier);

#task 10
SELECT NAME, COLOR FROM jbparts WHERE WEIGHT > (SELECT WEIGHT FROM jbparts WHERE NAME = 'card reader');

#task 11
SELECT Find.NAME, Find.COLOR FROM jbparts Find INNER JOIN jbparts Sought ON Find.WEIGHT > Sought.WEIGHT WHERE Sought.NAME = 'card reader';

#task 12
SELECT AVG(WEIGHT) FROM jbparts WHERE COLOR = 'black';

#task 13
SELECT SUPPLIER.name, SUM(DELIVERED.quan*PARTS.weight) as 'Total Weight' FROM jbcity CITY, jbsupplier SUPPLIER, jbsupply DELIVERED, jbparts PARTS WHERE CITY.state = 'Mass' AND CITY.id = SUPPLIER.city
AND PARTS.id = DELIVERED.part AND DELIVERED.supplier = SUPPLIER.id GROUP BY SUPPLIER.name;

#task 14
CREATE TABLE jbitemcopy(
	id INT,
    name VARCHAR(20),
    dept INT NOT NULL,
    price INT,
    qoh INT UNSIGNED,
    supplier INT NOT NULL,
    constraint pk_item PRIMARY KEY(id),
    constraint fk_item_new_dept FOREIGN KEY(dept) REFERENCES jbdept(id),
    constraint fk_item_new_supplier FOREIGN KEY(supplier) REFERENCES jbsupplier(id)
    );
    
    INSERT INTO jbitemcopy(SELECT * FROM jbitem  WHERE PRICE < (SELECT AVG(PRICE) FROM jbitem)
    );

#task 15
CREATE VIEW jbitemcopy_view AS SELECT * FROM jbitem  WHERE PRICE < (SELECT AVG(PRICE) FROM jbitem);
SELECT * FROM jbitemcopy_view;

#task 16
/*
A view is a viritual table that is defined by a query
A table is the place for storage of data and information
A table (static) collects its items directly from the physical storage and the view (dynamic) takes the information from the table and can manipulate its data over time.
Basically a table contains the actual data while a view is just a statement showing data. This means that a View is better when it can be used instead of a complex query to find data, and instead just SELECT items form the view.
*/

#task 17
#DROP VIEW jb_debit_view;
CREATE VIEW jb_debit_view AS SELECT DEBIT.id, SUM(SALE.quantity*ITEM.price) as DEBIT FROM jbdebit DEBIT, jbsale SALE, jbitem ITEM WHERE DEBIT.id = SALE.debit AND ITEM.id = SALE.item GROUP BY DEBIT.id;
select * from jb_debit_view;

#task 18
/*
The join notaton works by joining two tables under a condition. If the INNER JOIN is used, it compares every row from table a with every row from table b and only uses the rows matching the conditoin. 
#The LEFT and RIGHT JOIN work in the same way except that for the LEFT JOIN the left table is always kept, but if there are no mathing results from the right table it's matched with NULL, 
#and vice versa for RIGHT TABLE. Thus we use INNER JOIN so we won't have any NULL's (Although in the case of our code, using INNER, LEFT or RIGHT wouldn't matter in the result.
*/

#DROP VIEW jb_debit_view_v2;
CREATE VIEW jb_debit_view_v2 AS SELECT DEBIT.id, SUM(SALE.quantity*ITEM.price) as DEBIT FROM jbsale SALE 
INNER JOIN jbdebit DEBIT ON DEBIT.id = SALE.debit
INNER JOIN jbitem ITEM ON ITEM.id = SALE.item
GROUP BY DEBIT.id;

select * from jb_debit_view_v2;

#task 19 A AND B
#Had problem with safe updates so we needed to disable it
SET SQL_SAFE_UPDATES = 0;

#DELETE FROM jbsupplier WHERE CITY IN (SELECT ID FROM jbcity WHERE NAME = 'Los Angeles');
/*
Tried to delete supplier we got error message, because we had foreign key constraint in jbitem
Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`simja649`.`jbitem`, CONSTRAINT `fk_item_supplier` FOREIGN KEY (`supplier`) 
REFERENCES `jbsupplier` (`id`))	0.015 sec
We know now that we need to drop jbitem for los angeles to be able to delete jbsupplier
*/
#DELETE FROM jbitem WHERE SUPPLIER IN (SELECT ID FROM jbsupplier WHERE CITY IN (SELECT ID FROM jbcity WHERE NAME = 'Los Angeles'));
/*
Got another error message, we now know we need to delete jbsale constraints for los angeles to be able to recursively work our way back, then it will work to delete
Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails
(`simja649`.`jbsale`, CONSTRAINT `fk_sale_item` FOREIGN KEY (`item`) REFERENCES `jbitem` (`id`))
*/
DELETE FROM jbsale WHERE ITEM IN(SELECT ID from jbitem WHERE SUPPLIER IN(SELECT ID FROM jbsupplier WHERE CITY IN (SELECT ID FROM jbcity WHERE name = 'Los Angeles')));
/*
Now we got a response that the deletion worked, so we recursively delete everything again.
*/
DELETE FROM jbitem WHERE SUPPLIER IN (SELECT ID FROM jbsupplier WHERE CITY IN (SELECT ID FROM jbcity WHERE name = 'Los Angeles'));
DELETE FROM jbsupplier WHERE CITY IN (SELECT ID FROM jbcity WHERE NAME='Los Angeles');

#task 20
#DROP VIEW IF EXISTS jbsale_supply;
CREATE VIEW jbsale_supply(supplier, item, quantity) AS 
SELECT jbsupplier.name, jbitem.name, jbsale.quantity
FROM jbsupplier, jbitem
LEFT JOIN jbsale ON jbsale.item = jbitem.id 
WHERE jbsupplier.id = jbitem.supplier;
SELECT * FROM jbsale_supply;

SELECT supplier, sum(quantity) AS sum FROM jbsale_supply GROUP BY supplier;