-- SQL script to go through orders table, delete duplicate orderids, and then make orderids primary keys

-- Find duplicate orderids
WITH duplicate_orders AS (
    SELECT orderid
    FROM public.orders
    GROUP BY orderid
    HAVING COUNT(*) > 1
)

-- Delete duplicate orderids
DELETE FROM public.orders
WHERE orderid IN (SELECT orderid FROM duplicate_orders)
AND ctid NOT IN (
    SELECT MIN(ctid)
    FROM public.orders
    WHERE orderid IN (SELECT orderid FROM duplicate_orders)
    GROUP BY orderid
);

-- Make orderid primary key
ALTER TABLE public.orders
    ADD CONSTRAINT orders_pk PRIMARY KEY (orderid);