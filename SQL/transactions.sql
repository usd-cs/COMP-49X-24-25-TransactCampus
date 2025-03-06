-- SQL script to create table public.transactions with transaction information

CREATE TABLE public.transactions (
    orderid BIGINT NOT NULL,
    food_id BIGINT NOT NULL,
    userid BIGINT NOT NULL,
    locationid BIGINT NOT NULL,
    order_total_dollars DECIMAL(10, 2) NOT NULL,
    number_of_items INT NOT NULL,
    local_creation_datetime TIMESTAMP NOT NULL,
    complete_datetime TIMESTAMP NOT NULL,
    pickup_datetime TIMESTAMP,
    released_datetime TIMESTAMP NOT NULL,
    order_specific_food_id BIGINT NOT NULL,
    item_price_dollars DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (orderid, food_id),  
);