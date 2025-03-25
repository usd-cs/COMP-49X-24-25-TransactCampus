-- Create the main location orders table

CREATE TABLE location_orders (
    locationid INT,
    orderid INT,
    total_kcal DECIMAL(10,2),
    total_fat_g DECIMAL(10,2),
    total_cholesterol_mg DECIMAL(10,2),
    total_sodium_mg DECIMAL(10,2),
    total_carbohydrates_g DECIMAL(10,2),
    total_fiber_g DECIMAL(10,2),
    total_sugar_g DECIMAL(10,2),
    total_protein_g DECIMAL(10,2),
    location_name VARCHAR(255),
    food_categories TEXT,
    nutrition_score DECIMAL(10,2)
);