<?php

namespace Database\Seeders;

use App\Models\Product;
use Illuminate\Database\Seeder;

class ProductSeeder extends Seeder
{
    public function run()
    {
        $products = [
            [
                'name' => 'Sofa',
                'price' => 1500,
                'style' => 'Modern',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Refrigerator',
                'price' => 800,
                'style' => 'Modern',
                'material' => 'Metal',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Washing Machine',
                'price' => 600,
                'style' => 'Modern',
                'material' => 'Metal',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Microwave Oven',
                'price' => 300,
                'style' => 'Modern',
                'material' => 'Metal',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Television',
                'price' => 1200,
                'style' => 'Modern',
                'material' => 'Metal',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Queen Bed Frame',
                'price' => 700,
                'style' => 'Modern',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Office Desk',
                'price' => 400,
                'style' => 'Modern',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Dining Table',
                'price' => 900,
                'style' => 'Traditional',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Coffee Table',
                'price' => 250,
                'style' => 'Modern',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Bookshelf',
                'price' => 350,
                'style' => 'Modern',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Armchair',
                'price' => 600,
                'style' => 'Traditional',
                'material' => 'Fabric',
                'color_palette' => 'Dark',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Nightstand',
                'price' => 150,
                'style' => 'Modern',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Dresser',
                'price' => 700,
                'style' => 'Modern',
                'material' => 'Wood',
                'color_palette' => 'Neutral',
                'quality' => 'Standard'
            ],
            [
                'name' => 'Bed Mattress',
                'price' => 800,
                'style' => 'Modern',
                'material' => 'Foam',
                'color_palette' => 'Neutral',
                'quality' => 'Premium'
            ],
            // ... continuing with all other products
            [
                'name' => 'Storage Shed',
                'price' => 700,
                'style' => 'Traditional',
                'material' => 'Metal',
                'color_palette' => 'Dark',
                'quality' => 'Standard'
            ],
        ];

        foreach ($products as $product) {
            Product::create($product);
        }
    }
} 