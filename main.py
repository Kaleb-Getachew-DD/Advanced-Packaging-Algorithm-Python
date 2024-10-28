class Product:
    def __init__(self, name, price, style, material, color_palette, quality):
        self.name = name
        self.price = price
        self.style = style
        self.material = material
        self.color_palette = color_palette
        self.quality = quality

# Example available products
available_products = [
    Product("Sofa", 1500, "Modern", "Wood", "Neutral", "Standard"),
    Product("Refrigerator", 800, "Modern", "Metal", "Neutral", "Standard"),
    Product("Washing Machine", 600, "Modern", "Metal", "Neutral", "Standard"),
    Product("Microwave Oven", 300, "Modern", "Metal", "Neutral", "Standard"),
    Product("Television", 1200, "Modern", "Metal", "Neutral", "Standard"),
    Product("Queen Bed Frame", 700, "Modern", "Wood", "Neutral", "Standard"),
    Product("Office Desk", 400, "Modern", "Wood", "Neutral", "Standard"),
    Product("Dining Table", 900, "Traditional", "Wood", "Neutral", "Standard"),
    Product("Coffee Table", 250, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bookshelf", 350, "Modern", "Wood", "Neutral", "Standard"),
    Product("Armchair", 600, "Traditional", "Fabric", "Dark", "Standard"),
    Product("Nightstand", 150, "Modern", "Wood", "Neutral", "Standard"),
    Product("Dresser", 700, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bed Mattress", 800, "Modern", "Foam", "Neutral", "Premium"),
    Product("Desk Lamp", 100, "Modern", "Metal", "Neutral", "Standard"),
    Product("Entertainment Center", 1000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bar Stool", 200, "Modern", "Metal", "Neutral", "Standard"),
    Product("Floor Lamp", 150, "Traditional", "Metal", "Dark", "Standard"),
    Product("Area Rug", 300, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Wall Art", 200, "Modern", "Canvas", "Neutral", "Standard"),
    Product("Shower Curtain", 30, "Modern", "Fabric", "Dark", "Standard"),
    Product("Coffee Maker", 150, "Modern", "Metal", "Neutral", "Standard"),
    Product("Toaster", 80, "Modern", "Metal", "Neutral", "Standard"),
    Product("Blender", 120, "Modern", "Metal", "Neutral", "Standard"),
    Product("Cookware Set", 200, "Modern", "Metal", "Neutral", "Standard"),
    Product("Cutlery Set", 50, "Modern", "Metal", "Neutral", "Standard"),
    Product("Pots and Pans Set", 250, "Modern", "Metal", "Neutral", "Standard"),
    Product("Dishwasher", 1200, "Modern", "Metal", "Neutral", "Premium"),
    Product("Vacuum Cleaner", 300, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Iron", 80, "Modern", "Metal", "Neutral", "Standard"),
    Product("Curtains", 100, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Bedside Lamp", 75, "Modern", "Metal", "Neutral", "Standard"),
    Product("Pet Bed", 100, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Wall Clock", 50, "Modern", "Wood", "Neutral", "Standard"),
    Product("Fan", 150, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Air Purifier", 200, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Plant Pot", 25, "Modern", "Ceramic", "Neutral", "Standard"),
    Product("Outdoor Patio Set", 1500, "Modern", "Wood", "Neutral", "Standard"),
    Product("Fire Pit", 400, "Modern", "Metal", "Dark", "Standard"),
    Product("Grill", 300, "Modern", "Metal", "Dark", "Standard"),
    Product("Garden Tools Set", 100, "Modern", "Metal", "Dark", "Standard"),
    Product("Storage Shed", 700, "Traditional", "Metal", "Dark", "Standard"),
]

# User input data
budget = 3000
essential_items = [
    "Sofa",
    "Queen Bed Frame",
    "Office Desk",
    "Dining Table",
    "Washing Machine",
    "Microwave Oven",
    "Television",
    "Armchair",
    "Nightstand",
    "Refrigerator"
]

# User preferences
user_preferences = {
    "style": "Modern",
    "material": "Wood, Metal, Fabric",
    "color_palette": "Neutral, Dark",
    "quality": "Premium"
}

# Prepare to store selected packages
packages = []
max_packages = 7
all_used_products = set()

# Function to calculate the score for a package
def calculate_package_score(package, user_preferences):
    total_matches = 0
    total_products = len(package)

    for product in package:
        matches = 0
        if product.style == user_preferences["style"]:
            matches += 1
        if product.material in user_preferences["material"].split(", "):
            matches += 1
        if product.color_palette in user_preferences["color_palette"].split(", "):
            matches += 1
        if product.quality == user_preferences["quality"]:
            matches += 1
        
        total_matches += matches

    if total_products > 0:
        average_score = (total_matches / (total_products * 4)) * 100
    else:
        average_score = 0  # No products means no score

    return average_score

def generate_package(available_products, essential_items, remaining_budget):
    selected_package = []
    used_products = set()  # Keep track of used products in this package

    for essential in essential_items:
        best_product = None
        max_matches = 0

        for product in available_products:
            # Check if product matches the essential item
            if product.name == essential and product.name not in all_used_products:
                matches = 0

                # Increment match count for each criteria
                if product.style == user_preferences["style"]:
                    matches += 1
                if product.material in user_preferences["material"].split(", "):
                    matches += 1
                if product.color_palette in user_preferences["color_palette"].split(", "):
                    matches += 1
                if product.quality == user_preferences["quality"]:
                    matches += 1

                # Check if this product has more matches
                if matches > max_matches:
                    max_matches = matches
                    best_product = product

        # If a best product was found and it fits in the budget
        if best_product and best_product.price <= remaining_budget:
            selected_package.append(best_product)
            remaining_budget -= best_product.price
            used_products.add(best_product.name)
            all_used_products.add(best_product.name)  # Add to global used products
            # Remove the product from available products to avoid re-selection
            available_products.remove(best_product)

    # Add additional products if there's remaining budget
    for product in available_products:
        if remaining_budget >= product.price and product.name not in used_products and product.name not in all_used_products:
            selected_package.append(product)
            remaining_budget -= product.price
            used_products.add(product.name)
            all_used_products.add(product.name)  # Add to global used products

    return selected_package, remaining_budget

# Generate up to max_packages
while len(packages) < max_packages:
    remaining_budget = budget
    new_package, remaining_budget = generate_package(available_products.copy(), essential_items, remaining_budget)
    
    if not new_package:
        break  # Stop if no new package can be generated

    packages.append(new_package)

# Modify the final output section to help debug
for idx, package in enumerate(packages):
    print(f"=== Package {idx + 1} ===")
    total_price = 0
    for item in package:
        print(f"Item: {item.name}, Price: ${item.price}")
        total_price += item.price
    score = calculate_package_score(package, user_preferences)
    print(f"Total Price: ${total_price}")
    print(f"Package similarity Score: {score:.2f}%") 
    print(f"Remaining Budget: ${budget - total_price}\n")

# Print a summary of packages generated
print(f"Total Packages Generated: {len(packages)}")
