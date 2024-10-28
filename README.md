# Advanced Packaging Algorithm in Python

## Overview

This project implements a packaging algorithm that selects a set of products based on user-defined preferences and budget constraints. The algorithm evaluates available products, considering factors like style, material, color palette, and quality, to generate optimal product packages for the user.

## Features

- Defines a `Product` class with attributes such as name, price, style, material, color palette, and quality.
- Generates product packages based on a user-defined budget and essential items.
- Evaluates each package based on its similarity to the user's preferences.
- Outputs selected packages, total prices, similarity scores, and remaining budgets.

## Example Products

The algorithm includes a set of example products:

- Sofa: $1500
- Refrigerator: $800
- Washing Machine: $600
- Microwave Oven: $300
- Television: $1200
- Queen Bed Frame: $700
- Office Desk: $400
- Dining Table: $900
- Armchair: $600
- Nightstand: $150
- And many more...

## User Input

- **Budget**: The total amount of money the user is willing to spend (e.g., $3000).
- **Essential Items**: A list of products that the user considers essential (e.g., Sofa, Queen Bed Frame, Office Desk).
- **User Preferences**: A dictionary containing the user's style, material, color palette, and quality preferences.

## Packaging Algorithm

The packaging algorithm follows these steps:

1. Initialize user-defined parameters (budget, essential items, preferences).
2. Iterate through available products to find the best matches for essential items.
3. Calculate similarity scores for each package based on user preferences.
4. Generate multiple packages until the maximum limit is reached or no more products can be selected.

## Code Execution

The final output shows the generated packages along with their details, including total price, similarity score, and remaining budget:

```
=== Package 1 ===
Item: Sofa, Price: $1500
Item: Queen Bed Frame, Price: $700
Item: Office Desk, Price: $400
Item: Microwave Oven, Price: $300
Item: Desk Lamp, Price: $100
Total Price: $3000
Package similarity Score: 75.00%
Remaining Budget: $0

=== Package 2 ===
Item: Dining Table, Price: $900
Item: Washing Machine, Price: $600
Item: Television, Price: $1200
Item: Nightstand, Price: $150
Item: Floor Lamp, Price: $150
Total Price: $3000
Package similarity Score: 65.00%
Remaining Budget: $0

=== Package 3 ===
Item: Armchair, Price: $600
Item: Refrigerator, Price: $800
Item: Coffee Table, Price: $250
Item: Bookshelf, Price: $350
Item: Dresser, Price: $700
Item: Bar Stool, Price: $200
Item: Shower Curtain, Price: $30
Item: Cutlery Set, Price: $50
Total Price: $2980
Package similarity Score: 71.88%
Remaining Budget: $20

=== Total Packages Generated: 6 ===
```

## Installation

To use this project, clone the repository:

```bash
git clone https://github.com/Kaleb-Getachew-DD/Advanced-Packaging-Algorithm-Python.git
cd Advanced-Packaging-Algorithm-Python
```

Make sure you have Python installed. You can run the script using:

```bash
python # Advanced Packaging Algorithm in Python

## Overview

This project implements a packaging algorithm that selects a set of products based on user-defined preferences and budget constraints. The algorithm evaluates available products, considering factors like style, material, color palette, and quality, to generate optimal product packages for the user.

## Features

- Defines a `Product` class with attributes such as name, price, style, material, color palette, and quality.
- Generates product packages based on a user-defined budget and essential items.
- Evaluates each package based on its similarity to the user's preferences.
- Outputs selected packages, total prices, similarity scores, and remaining budgets.

## Example Products

The algorithm includes a set of example products:

- Sofa: $1500
- Refrigerator: $800
- Washing Machine: $600
- Microwave Oven: $300
- Television: $1200
- Queen Bed Frame: $700
- Office Desk: $400
- Dining Table: $900
- Armchair: $600
- Nightstand: $150
- And many more...

## User Input

- **Budget**: The total amount of money the user is willing to spend (e.g., $3000).
- **Essential Items**: A list of products that the user considers essential (e.g., Sofa, Queen Bed Frame, Office Desk).
- **User Preferences**: A dictionary containing the user's style, material, color palette, and quality preferences.

## Packaging Algorithm

The packaging algorithm follows these steps:

1. Initialize user-defined parameters (budget, essential items, preferences).
2. Iterate through available products to find the best matches for essential items.
3. Calculate similarity scores for each package based on user preferences.
4. Generate multiple packages until the maximum limit is reached or no more products can be selected.

## Code Execution

The final output shows the generated packages along with their details, including total price, similarity score, and remaining budget:

```
=== Package 1 ===
Item: Sofa, Price: $1500
Item: Queen Bed Frame, Price: $700
Item: Office Desk, Price: $400
Item: Microwave Oven, Price: $300
Item: Desk Lamp, Price: $100
Total Price: $3000
Package similarity Score: 75.00%
Remaining Budget: $0

=== Package 2 ===
Item: Dining Table, Price: $900
Item: Washing Machine, Price: $600
Item: Television, Price: $1200
Item: Nightstand, Price: $150
Item: Floor Lamp, Price: $150
Total Price: $3000
Package similarity Score: 65.00%
Remaining Budget: $0

=== Package 3 ===
Item: Armchair, Price: $600
Item: Refrigerator, Price: $800
Item: Coffee Table, Price: $250
Item: Bookshelf, Price: $350
Item: Dresser, Price: $700
Item: Bar Stool, Price: $200
Item: Shower Curtain, Price: $30
Item: Cutlery Set, Price: $50
Total Price: $2980
Package similarity Score: 71.88%
Remaining Budget: $20

=== Total Packages Generated: 6 ===
```

## Installation

To use this project, clone the repository:

```bash
git clone https://github.com/Kaleb-Getachew-DD/Advanced-Packaging-Algorithm-Python.git
cd Advanced-Packaging-Algorithm-Python
```

Make sure you have Python installed. You can run the script using:

```bash
python main.py
```

## Contributing

If you would like to contribute to this project, please create a new branch and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
.py
```

## Contributing

If you would like to contribute to this project, please create a new branch and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
