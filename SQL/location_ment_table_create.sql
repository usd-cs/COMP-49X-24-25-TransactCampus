-- Create location menu table

CREATE TABLE location_menu (
    locationid INT,
    itemid INT,
    foodid INT,
    food_name VARCHAR(255),
    food_category VARCHAR(100),
    kcal DECIMAL(10,2),
    nutrition_fat_g DECIMAL(10,2),
    nutrition_cholesterol_mg DECIMAL(10,2),
    nutrition_sodium_mg DECIMAL(10,2),
    nutrition_carbohydrates_g DECIMAL(10,2),
    nutrition_fiber_g DECIMAL(10,2),
    nutrition_sugar_g DECIMAL(10,2),
    nutrition_protein_g DECIMAL(10,2),
    nutrition_score DECIMAL(10,2),
    PRIMARY KEY (locationid, itemid, foodid)
);