-- create a trigger that decreases the quantity of an item after adding a new order

CREATE TRIGGER decrease_quantity_of_item_after_new_order_add
AFTER INSERT on orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
