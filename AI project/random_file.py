import random

restaurants = [
    'A2B', 'Anandha Bhavan', 'Saravana Bhavan', 'Dindigul Thalappakatti',
    'The Marina', 'Barbeque Nation', 'Punjab Grill', 'Kumarakom', 'Anjappar',
    'Fried Chicken Hub', 'Hotel Ramya', 'Sangeetha', 'Hotel Saravana',
    'Tandoor', 'Rajdhani', 'Little Italy', 'Pizza Hut', 'Dragon Palace',
    'Great Wall', 'Al Ameer', 'Mezza', 'Sushi Hub', 'Tokyo Diner', 'Kimchi House',
    'Seoul Garden', 'Cafe Coffee Day', 'Taj Mahal', 'Family Feast', 'Cozy Corner',
    'Moonlight Dine', 'Love Birds', 'Skyline Grill', 'Cloud 9', 'Spice Route',
    'Curry Leaf', 'Golden Dragon', 'The Oriental', 'Saffron', 'Eastern Spice',
    'The Green Bowl', 'Tiffin Talk', 'Madras Cafe', 'Herbivore', 'Flavors of India',
    'Taste Junction', 'Urban Tadka', 'Masala Magic', 'Biryani House', 'Namma Veedu',
    'Zaika', 'Mehfil', 'Garam Masala', 'Royal Rasoi', 'Chat Street', 'Swaad',
    'Mirchi', 'Tandoori Nights', 'Dosa Plaza', 'Curry Point', 'Shan-e-Punjab',
    'The Spice House', 'Roti Express', 'Mughlai Darbar', 'Bombay Blues', 'Chili’s',
    'The Yellow Chilli', 'Faji’s', 'Mainland China', 'Barista', 'Cafe Coffee Bean',
    'The Belgian Waffle Co', 'Keventers', 'The Chocolate Room', 'Cafe Mondegar',
    'Le Pain Quotidien', 'Bistro Claytopia', 'The Fatty Bao', 'The Bombay Canteen'
]

cuisines = ['north_indian', 'south_indian', 'chinese', 'italian', 'continental', 'arabic', 'japanese', 'korean', 'sea_food', 'american']

prices = ['low', 'medium', 'high']

cities = ['chennai', 'coimbatore', 'vellore', 'salem', 'tirunelveli', 'trichy', 'hosur', 'madurai']

ambiences = ['casual', 'fine_dining', 'family', 'romantic', 'rooftop']

types = ['veg', 'nonveg', 'veg_nonveg']

ratings = [round(x * 0.1, 1) for x in range(30, 51)]  # 3.0 to 5.0

def generate_unique_name(base_name, idx):
    return f"{base_name}_{idx}"

filename = 'restaurants.pl'

with open(filename, 'w') as f:
    f.write('% Restaurant knowledge base\n\n')
    count = 1

    for i in range(2000):
        base_rest = random.choice(restaurants)
        rest_name = generate_unique_name(base_rest.replace(" ", "_").lower(), i+1)

        cuisine = random.choice(cuisines)
        price = random.choice(prices)
        city = random.choice(cities)
        ambience = random.choice(ambiences)
        food_type = random.choice(types)
        rating = random.choice(ratings)
        image_path = f"images/restaurant_{count}.png"

        fact = f"restaurant('{rest_name}', {cuisine}, {price}, {city}, {ambience}, {food_type}, {rating}, '{image_path}').\n"
        f.write(fact)

        count += 1

print(f"Generated {count-1} restaurant facts in {filename}")
