-- Queries

-- order does not matter after the ON, as long as correct values are referenced
-- when joining, only users tables that do have overlapping information will be transfered, it wont create a bunch of nulls. ie. I never tweeted so the value representing me doesn't get appear
-- in order to print every piece fromhte conjoining tables, juse LEFT JOIN- this will produce null values if necesarry. ie. i never tweeted but you pulled my tweets: 'null' would appear

-- One to One: 
-- SELECT * FROM customers 
-- JOIN addresses ON addresses.id = customers.address_id;
-- the table 'customers' has a foreign key address.id, this combines the two tables, 'addresses' and 'customers', through the foreign key address.id on 'customers'

-- One to Many: 
-- SELECT * FROM orders 
-- JOIN customers ON customers.id = orders.customer_id;
-- the table 'orders' has foreign key customer.id, this combines 'orders' with 'customers' through the foreign key customer_id on 'orders'

-- Many to Many: 
-- SELECT * FROM orders 
-- JOIN items_orders ON orders.id = items_orders.order_id 
-- JOIN items ON items.id = items_orders.item_id;
-- the table 'item_orders' joins the table 'orders' through the foriegn key orders.id on the table 'item_orders'
-- the table 'items' joins the 'item_orders' 

