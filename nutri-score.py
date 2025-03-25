import pandas as pd


def calculate_nutri_score(nutrients, is_beverage=False):
    """Calculates the Nutri-Score based on provided nutrients (Updated 2024 formula).

    Args:
        nutrients (dict): Dictionary of nutrient values per 100g/100ml.
            Required keys: energy, sugars, saturated_fat, sodium, fiber, protein
            Optional key for beverages: fruit_juice_percent
            Optional key for general food: fruit_veg_nuts_percent
        is_beverage (bool): True if the product is a beverage, False otherwise.

    Returns:
        str: The Nutri-Score letter (A-E) or None if input is invalid.
    """

    required_keys = ["energy", "sugars", "saturated_fat", "sodium", "fiber", "protein"]
    if not all(key in nutrients for key in required_keys):
        print("Error: Missing required nutrients in input.")
        return None

    negative_points = 0
    positive_points = 0

    # Negative points
    negative_points += nutrients["energy"] / 335  # Energy (kJ)
    negative_points += nutrients["sugars"] / 4.5
    negative_points += nutrients["saturated_fat"] / 1
    negative_points += nutrients["sodium"] / 90

    # Positive points
    fruit_veg_nuts = nutrients.get("fruit_veg_nuts_percent", 0)
    # Real Nutri-Score gives:
    # 0 points <40%, 1 point if ≥40%, 2 if ≥60%, 5 if ≥80%
    if fruit_veg_nuts >= 80:
        positive_points += 5
    elif fruit_veg_nuts >= 60:
        positive_points += 2
    elif fruit_veg_nuts >= 40:
        positive_points += 1

    positive_points += nutrients["fiber"] / 0.9
    positive_points += nutrients["protein"] / 3.5

    score = negative_points - positive_points

    if is_beverage:
        if score < 1:
            return "A"
        elif score < 5:
            return "B"
        elif score < 9:
            return "C"
        elif score < 13:
            return "D"
        else:
            return "E"
    else:
        if score <= -1:
            return "A"
        elif score <= 2:
            return "B"
        elif score <= 10:
            return "C"
        elif score <= 18:
            return "D"
        else:
            return "E"


def estimate_fruit_veg_nut_percent(row):
    name = row["food_name"].lower()
    category = row["food_category"].lower()

    if (
        "salad" in name
        or "vegetable" in name
        or category in ["salads", "vegan", "fruit"]
    ):
        return 80
    elif "wrap" in name or "bowl" in name or "tofu" in name:
        return 60
    elif "sandwich" in name or "chicken" in name:
        return 40
    else:
        return 0  # assume processed or mixed food


# Apply scoring
def get_nutri_score(row):
    try:
        nutrients = {
            "energy": row["kcal"] * 4.184,  # kcal to kJ
            "sugars": row["nutrition_sugar_g"],
            "saturated_fat": row[
                "nutrition_fat_g"
            ],  # assuming total fat = saturated fat
            "sodium": row["nutrition_sodium_mg"],
            "fiber": row["nutrition_fiber_g"],
            "protein": row["nutrition_protein_g"],
            "fruit_veg_nuts_percent": estimate_fruit_veg_nut_percent(row),
        }
        is_beverage = row["food_category"].lower() in [
            "beverage",
            "drink",
            "juice",
            "blended",
            "smoothies",
        ]
        return calculate_nutri_score(nutrients, is_beverage)
    except Exception as e:
        return None


# Load our data
df = pd.read_csv("food.csv")

# Add the new column
df["food_score"] = df.apply(get_nutri_score, axis=1)

# Save to a new CSV
df.to_csv("scored_food.csv", index=False)
