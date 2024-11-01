from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import random
import time
from main import Product, calculate_package_score, generate_package, generate_all_packages

app = FastAPI()

# Define request models using Pydantic
class Preferences(BaseModel):
    style: str
    material: List[str]
    color_palette: List[str]
    quality: str

class PackageRequest(BaseModel):
    budget: float
    essential_items: List[str]
    preferences: Preferences

# Available products
available_products = [
    Product("Sofa", 40000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Refrigerator", 30000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Washing Machine", 44000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Microwave Oven", 3000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Television", 24000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Queen Bed Frame", 17000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Office Desk", 9000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Dining Table", 12000, "Traditional", "Wood", "Neutral", "Standard"),
    Product("Coffee Table", 5500, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bookshelf", 3500, "Modern", "Wood", "Neutral", "Standard"),
    Product("Armchair", 10000, "Traditional", "Fabric", "Dark", "Standard"),
    Product("Nightstand", 4000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Dresser", 15000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bed Mattress", 8000, "Modern", "Foam", "Neutral", "Premium"),
    Product("Desk Lamp", 2000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Entertainment Center", 3000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bar Stool", 1000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Floor Lamp", 1500, "Traditional", "Metal", "Dark", "Standard"),
    Product("Area Rug", 6000, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Wall Art", 2000, "Modern", "Canvas", "Neutral", "Standard"),
    Product("TV Mount", 2500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Console Table", 6000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Throw Blanket", 1500, "Modern", "Fabric", "Neutral", "Premium"),
    Product("Decorative Pillows Set", 2000, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Media Storage Unit", 7000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bed Sheets Set", 3000, "Modern", "Fabric", "Neutral", "Premium"),
    Product("Comforter Set", 5000, "Modern", "Fabric", "Neutral", "Premium"),
    Product("Pillows Set", 2500, "Modern", "Foam", "Neutral", "Premium"),
    Product("Bedroom Bench", 8000, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Under-bed Storage", 3500, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Dining Chairs Set", 15000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Table Runner", 1000, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Placemats Set", 1500, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Serving Cart", 7000, "Modern", "Metal", "Neutral", "Standard"),
    Product("China Cabinet", 25000, "Modern", "Wood", "Neutral", "Premium"),
    Product("Ergonomic Chair", 12000, "Modern", "Fabric", "Neutral", "Premium"),
    Product("Desk Pad", 1000, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Cable Management Set", 1500, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Monitor Stand", 2500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Desk Drawer Unit", 5000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Spice Rack", 1500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Kitchen Storage Set", 3000, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Paper Towel Holder", 500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Dish Drying Rack", 2000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Kitchen Mat Set", 2500, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Laundry Sorter", 3000, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Drying Rack", 2500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Laundry Storage Cabinet", 8000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Laundry Counter Top", 5000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Lint Roller Set", 500, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Floating Shelves Set", 3500, "Modern", "Wood", "Neutral", "Standard"),
    Product("Storage Ottoman", 4500, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Drawer Organizers Set", 2000, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Closet System", 12000, "Modern", "Wood", "Neutral", "Premium"),
    Product("Storage Baskets Set", 2500, "Modern", "Fabric", "Neutral", "Standard"),
    Product("Ceiling Fan with Light", 8000, "Modern", "Metal", "Neutral", "Premium"),
    Product("Wall Sconces Set", 4500, "Modern", "Metal", "Neutral", "Standard"),
    Product("LED Strip Lighting", 2000, "Modern", "Plastic", "Neutral", "Standard"),
    Product("Table Lamp Set", 5000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Reading Light", 1500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Key and Mail Organizer", 1500, "Modern", "Wood", "Neutral", "Standard"),
    Product("Shoe Storage Bench", 7000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Coat Rack", 3000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Magazine Rack", 2000, "Modern", "Metal", "Neutral", "Standard"),
    Product("Umbrella Stand", 1500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Decorative Mirrors Set", 8000, "Modern", "Glass", "Neutral", "Premium"),
    Product("Indoor Plants Set", 5000, "Modern", "Ceramic", "Neutral", "Standard"),
    Product("Wall Shelves Set", 6000, "Modern", "Wood", "Neutral", "Standard"),
    Product("Bookends Set", 1500, "Modern", "Metal", "Neutral", "Standard"),
    Product("Photo Frames Set", 3000, "Modern", "Wood", "Neutral", "Standard")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*']
    )

@app.post("/api/generate-package")
async def generate_packages(request: PackageRequest):
    try:
        # Convert preferences to the format expected by the original code
        user_preferences = {
            "style": request.preferences.style,
            "material": ", ".join(request.preferences.material),
            "color_palette": ", ".join(request.preferences.color_palette),
            "quality": request.preferences.quality
        }

        # Generate packages using the function from main.py
        packages = generate_all_packages(
            request.budget,
            request.essential_items,
            7,  # max_packages
            available_products,
            user_preferences
        )

        # Format the response
        formatted_packages = []
        for package in packages:
            total_price = sum(item.price for item in package)
            score = calculate_package_score(package, user_preferences)
            
            formatted_packages.append({
                "items": [
                    {
                        "name": item.name,
                        "price": item.price,
                        "style": item.style,
                        "material": item.material,
                        "color_palette": item.color_palette,
                        "quality": item.quality
                    } for item in package
                ],
                "total_price": total_price,
                "similarity_score": round(score, 2),
                "remaining_budget": request.budget - total_price
            })

        return {
            "status": "success",
            "packages": formatted_packages,
            "total_packages": len(formatted_packages)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
