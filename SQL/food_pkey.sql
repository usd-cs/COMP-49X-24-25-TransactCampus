-- SQL script to go through food table, delete duplicate food_ids, and then make food_ids primary keys

-- Find duplicate food_ids
WITH duplicate_food AS (
    SELECT food_id
    FROM public.food
    GROUP BY food_id
    HAVING COUNT(*) > 1
)

-- Delete duplicate food_ids
DELETE FROM public.food
WHERE food_id IN (SELECT food_id FROM duplicate_food)
AND ctid NOT IN (
    SELECT MIN(ctid)
    FROM public.food
    WHERE food_id IN (SELECT food_id FROM duplicate_food)
    GROUP BY food_id
);

-- Make food_id primary key
ALTER TABLE public.food
    ADD CONSTRAINT food_pk PRIMARY KEY (food_id);