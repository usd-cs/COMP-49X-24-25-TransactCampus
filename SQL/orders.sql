-- SQL script to create table public.orders with orders information

CREATE TABLE public.orders (
    orderid BIGINT NOT NULL,
    locationid BIGINT NOT NULL,
    cafeteriaid BIGINT NOT NULL,
    campusid BIGINT NOT NULL,
    released_datetime TIMESTAMP NOT NULL,
    complete_datetime TIMESTAMP NOT NULL,
    local_time TIMESTAMP NOT NULL,
    number_of_items INT NOT NULL,
);