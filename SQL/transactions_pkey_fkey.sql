-- SQL script to go through transactions table, delete missing food_ids from public.food and 
-- orderids from public.orders. and then make food_id and orderid foreign keys

-- Create indexes to speed up deletion
CREATE INDEX IF NOT EXISTS idx_transactions_foodid ON public.transactions(food_id);
CREATE INDEX IF NOT EXISTS idx_transactions_orderid ON public.transactions(orderid);

-- Delete rows where food_id does not exist in food table 
DO $$ 
DECLARE 
    batch_size INT := 100000;
BEGIN
    LOOP
        DELETE FROM public.transactions
        WHERE CTID IN (
            SELECT t.CTID
            FROM public.transactions t
            LEFT JOIN public.food f ON t.food_id = f.food_id
            WHERE f.food_id IS NULL
            LIMIT batch_size
        );

        EXIT WHEN NOT FOUND;  -- Stop when no more rows to delete
    END LOOP;
END $$;

-- Delete rows where orderid does not exist in orders table 
DO $$ 
DECLARE 
    batch_size INT := 100000;
BEGIN
    LOOP
        DELETE FROM public.transactions
        WHERE CTID IN (
            SELECT t.CTID
            FROM public.transactions t
            LEFT JOIN public.orders o ON t.orderid = o.orderid
            WHERE o.orderid IS NULL
            LIMIT batch_size
        );

        EXIT WHEN NOT FOUND;
    END LOOP;
END $$;

-- Create foreign keys
ALTER TABLE public.transactions
ADD CONSTRAINT fk_transactions_orderid
FOREIGN KEY (orderid) REFERENCES public.orders(orderid);

ALTER TABLE public.transactions
ADD CONSTRAINT fk_transactions_foodid
FOREIGN KEY (food_id) REFERENCES public.food(food_id) ON DELETE CASCADE;