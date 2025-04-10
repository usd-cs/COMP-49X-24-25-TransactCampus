import pandas as pd


def calculate_nutri_score(nutrients, is_beverage=False):
    """
    Calculates a Nutri-Score-like value on a scale of 1 (least healthy) to 100 (most healthy).

    Args:
        nutrients (dict): Dictionary of nutrient values per 100g/100ml.
        is_beverage (bool): True if the product is a beverage.

    Returns:
        int: Score from 1 (unhealthy) to 100 (healthy).
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
    if fruit_veg_nuts >= 80:
        positive_points += 5
    elif fruit_veg_nuts >= 60:
        positive_points += 2
    elif fruit_veg_nuts >= 40:
        positive_points += 1

    positive_points += min(nutrients["fiber"] / 0.9, 5)
    positive_points += min(nutrients["protein"] / 3.5, 5)

    raw_score = negative_points - positive_points

    # Normalize raw_score to a range from 1 (worst) to 100 (best)
    # Estimated range: worst ~40, best ~-15 → map [40, -15] to [1, 100]
    # Clamp to avoid out-of-bounds values

    min_raw = -15
    max_raw = 40
    raw_score_clamped = max(min(raw_score, max_raw), min_raw)

    normalized_score = 100 - int(
        ((raw_score_clamped - min_raw) / (max_raw - min_raw)) * 99
    )
    return normalized_score


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


def get_letter_grade(score):
    # 0 - 10 F
    # 10 - 20 D
    # 20 - 35 C
    # 36 - 65 B
    # 65 - 100 A
    if score >= 65:
        return "A"
    elif score >= 36:
        return "B"
    elif score >= 20:
        return "C"
    elif score >= 10:
        return "D"
    else:
        return "F"


# Load our data
df = pd.read_csv("food.csv")

# Add the new column
df["food_score"] = df.apply(get_nutri_score, axis=1)
df["letter_grade"] = df["food_score"].apply(get_letter_grade)

# Save to a new CSV
df.to_csv("scored_food.csv", index=False)
