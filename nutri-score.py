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
    if is_beverage:
        positive_points = nutrients.get("fruit_juice_percent", 0)
    else:
        positive_points = nutrients.get("fruit_veg_nuts_percent", 0)
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


def calculate_nutri_score_2024(nutrients, is_beverage=False):
    """Calculates the Nutri-Score based on provided nutrients (Updated 2024 formula - Conceptual).

    Args:
        nutrients (dict): Dictionary of nutrient values per 100g/100ml.
            Required keys: energy, sugars, saturated_fat, sodium, fiber, protein
            Optional key for beverages: fruit_juice_percent
            Optional key for general food: fruit_veg_nuts_percent
            Optional key: sweeteners (bool)
        is_beverage (bool): True if the product is a beverage, False otherwise.

    Returns:
        str: The Nutri-Score letter (A-E) or None if input is invalid.
    """
    score = calculate_nutri_score(nutrients, is_beverage)

    # 2024 changes (Conceptual implementation):
    if is_beverage and nutrients.get(
        "sweeteners", False
    ):  # Check for sweeteners in beverages
        if score == "B":
            score = "C"
        elif score == "A":
            score = "B"
        elif score == "C":
            score = "D"
        elif score == "D":
            score = "E"

    # More nuanced changes for 2024 would go here (e.g., fiber, protein recalibration)
    # These changes are not yet publicly available in detail.

    return score


# Example Usage

# Example: Soda with sweeteners (Illustrative)
soda_nutrients = {
    "energy": 100,  # kJ
    "sugars": 10,
    "saturated_fat": 0,
    "sodium": 50,
    "fiber": 0,
    "protein": 0,
    "fruit_juice_percent": 0,
    "sweeteners": True,  # added sweeteners for 2024 test
}

soda_score_2023 = calculate_nutri_score(soda_nutrients, is_beverage=True)
soda_score_2024 = calculate_nutri_score_2024(soda_nutrients, is_beverage=True)
print(f"Soda Nutri-Score (2023): {soda_score_2023}")
print(f"Soda Nutri-Score (2024 - with sweeteners): {soda_score_2024}")

soda_nutrients_nosweetener = {
    "energy": 100,  # kJ
    "sugars": 10,
    "saturated_fat": 0,
    "sodium": 50,
    "fiber": 0,
    "protein": 0,
    "fruit_juice_percent": 0,
    "sweeteners": False,  # added sweeteners for 2024 test
}

soda_score_2023_nosweetener = calculate_nutri_score(
    soda_nutrients_nosweetener, is_beverage=True
)
soda_score_2024_nosweetener = calculate_nutri_score_2024(
    soda_nutrients_nosweetener, is_beverage=True
)
print(f"Soda Nutri-Score (2023): {soda_score_2023_nosweetener}")
print(f"Soda Nutri-Score (2024 - without sweeteners): {soda_score_2024_nosweetener}")
