-- SQL script to create table public.food with menu information

CREATE TABLE public.food (
    food_id BIGINT PRIMARY KEY,
    food_name TEXT NOT NULL,
    price_dollars DECIMAL(5,2) NOT NULL,
    kcal INT NOT NULL,
    nutrition_fat_g BIGINT NOT NULL,
    nutrition_cholesterol_mg BIGINT NOT NULL,
    nutrition_sodium_mg BIGINT NOT NULL,
    nutrition_carbohydrates_g BIGINT NOT NULL,
    nutrition_fiber_g BIGINT NOT NULL,
    nutrition_sugar_g BIGINT NOT NULL,
    nutrition_protein_g BIGINT NOT NULL,
    food_category TEXT NOT NULL,
    locationid BIGINT NOT NULL,
    location_name TEXT NOT NULL
);