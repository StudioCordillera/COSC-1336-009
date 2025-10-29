## Project 1: Recipe Scaler

### Overview
Build a Python program that helps a user scale one of three predefined recipes (Cake, Cookies, Brownies) to a desired number of servings.

### User Interaction Flow
1. Display a header.
2. Wait for user to press Enter to begin.
3. Show numbered menu:
   1. Cake
   2. Cookies
   3. Brownies
4. User selects a recipe (1, 2, or 3). Re-prompt until valid.
5. Ask for desired servings (positive whole number). Re-prompt until valid.
6. Calculate scaled ingredient amounts.
7. Print formatted scaled recipe report.
8. Show closing message and exit.

### Data Requirements
Define the recipes directly in the code (no external files). Each recipe includes:
- Base servings (e.g., Cake = 8 slices, Cookies = 24 cookies, Brownies = 16 squares)
- Ingredients list: each ingredient has name, quantity (float for base recipe), and unit (e.g., cups, tsp, units)
Keep ingredient lists reasonable (5–8 items per recipe).

### Scaling Rules
- Scaling factor = desired_servings / base_servings
- Scaled quantity = original_qty * scaling_factor
- For countable items like eggs (unit "units"), round to nearest 0.5
- For other ingredients, round to two decimal places

### Output Formatting
Report must include:
- Recipe name
- Target servings
- Table header: Ingredient | Qty | Unit
- Aligned columns for readability
- Divider lines above and below the table

Example layout (values illustrative only):
```
----------------------------------------------
Recipe: Cake
Target Servings: 10
----------------------------------------------
Ingredient             Qty  Unit
------------------ -------  ------
Flour                  2.5  cups
Sugar                 1.88  cups
Eggs                   4.0  units
... etc ...
----------------------------------------------
```

### Input Validation
- Menu choice: must be 1, 2, or 3
- Servings: must be a positive integer (> 0)
- Invalid input triggers a clear retry message

### Suggested Functions
Implement (or adapt) these for organization:
- `header()`
- `get_recipe_choice()`
- `get_servings()`
- `scale_recipe(recipe_name, target_servings)`
- `print_scaled(recipe_name, target_servings, scaled_ingredients)`
- `footer()`
- `main()`

### Constraints
- Single Python file (e.g., `recipe_scaler.py`)
- No external packages
- Clear variable names
- Comment block at top with: Name, Date, Project Title, Brief Description

### Grading Criteria
1. Correct interaction flow
2. Accurate scaling math
3. Proper rounding rules
4. Robust input validation loops
5. Clean, aligned formatting
6. Functional decomposition (use of functions)
7. Descriptive header comment

### Optional Enhancements (Extra Credit if clearly marked)
- Loop to scale another recipe without restarting
- Warning if servings > 10 × base (e.g., "Large batch – check oven capacity")
- Convert large cup totals to quarts (4 cups = 1 quart)
- Support fractional servings (e.g., 6.5) with adjusted rounding
- Display original vs scaled quantities side-by-side

### What to Avoid
- Hardcoding scaled values
- Printing raw scaling factor without context
- Crashing on invalid input
- Using external files or libraries

### Deliverable
Submit: `recipe_scaler.py`

### Starter Pseudocode (Optional Guide)
```
def main():
	header()
	wait_for_enter()
	name = get_recipe_choice()
	servings = get_servings()
	ingredients = scale_recipe(name, servings)
	print_scaled(name, servings, ingredients)
	footer()
```

### Reflection (Optional for Students)
Add a brief comment at end: What was the trickiest part? How did you test correctness?

---
End of Project 1 Prompt

