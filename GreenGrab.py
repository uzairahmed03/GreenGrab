import pytesseract as pytesseract
from PIL import Image



def get_sustainability_rating(food_type):
    sustainability_ratings = {
        "Wheat & Rye (Bread)": 1.4,
        "Maize (Meal)": 1.1,
        "Barley (Beer)": 1.1,
        "Oatmeal": 1.6,
        "Rice": 4,
        "Potatoes": 0.3,
        "Cassava": 0.9,
        "Cane Sugar": 2.6,
        "Beet Sugar": 1.4,
        "Other Pulses": 1.6,
        "Peas": 0.8,
        "Nuts": 0.2,
        "Groundnuts": 2.4,
        "Soymilk": 1,
        "Tofu": 3,
        "Soybean Oil": 6,
        "Sunflower Oil": 7.6,
        "Rapeseed Oil": 3.5,
        "Olive Oil": 3.7,
        "Tomatoes": 6,
        "Onions & Leeks": 1.4,
        "Root Vegetables": 0.3,
        "Brassicas": 0.3,
        "Other Vegetables": 0.4,
        "Citrus Fruit": 0.5,
        "Bananas": 0.3,
        "Apples": 0.8,
        "Berries & Grapes": 0.3,
        "Wine": 1.1,
        "Other Fruit": 1.4,
        "Coffee": 0.7,
        "Dark Chocolate": 16.5,
        "Beef (beef herd)": 18.7,
        "Beef (dairy herd)": 59.6,
        "Lamb & Mutton": 21.1,
        "Pig Meat": 24.5,
        "Poultry Meat": 7.2,
        "Milk": 6.1,
        "Cheese": 2.8,
        "Eggs": 21.2,
        "Fish (farmed)": 4.5,
        "Shrimps (farmed)": 5.1
    }

    rating = sustainability_ratings.get(food_type)
    return rating


def image_to_text(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(img)
        return text


food_type = image_to_text(input("Enter the food type: "))
rating = get_sustainability_rating(image_to_text(food_type))
if rating is not None:
    print(f"{food_type} is rated {rating} on the sustainability scale.")
else:
    print(f"Sustainability rating not found for {food_type}.")

