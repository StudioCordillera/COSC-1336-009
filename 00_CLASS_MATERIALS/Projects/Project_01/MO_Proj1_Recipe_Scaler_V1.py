########################################
## Name: Matthew                   #####
## Date: October 22, 2025          #####
## Project Name: Recipe scaler V1  #####
## Status: In-Progress             #####
## --------------------------------#####
## Project Functions               #####
##  - Take 1 inputs to begin       #####
##  - Take 1 input to get servings #####
##  - Calculate modified           #####
##     ingredient values           #####
##  - Print modified recipe        #####
##  - Look stylish with labeler    #####
##    functions                    #####
########################################


############## ASSIGNMENTS #############

## 1 Unit = 4 Teaspoons
## 1 Cup = 48 Teaspoons = 12 Units
## 0.5 Cup = 24 Teaspoons = 6 Units

## BASE INGREDIENT STATIC VARS | FOR RATIO AND SCALING
## SCALE: 1 (unit) = 4 Teaspoons | Pre-Calculated to "Unit" standard

# Unsalted Butter 0.5 cups = 6 (units)
unsalted_butter = 6

# Granulated Sugar 1 cups = 12 (units)
granulated_sugar = 12

# Vanilla Extract 1 teaspoon = 4 (units)
vanilla_extract = 4

# Being arbitrary measurement -> Assigned 1 (unit)/egg | (will handle in-text phrasing)
# Large Eggs 2 eggs = 2 (units)
large_eggs = 2

# Baking Soda 0.25 teaspoon = 1 (unit)
baking_soda = 1

# Salt 0.25 teaspoon = 1 (unit)
salt = 1

# Flour 0.5 cups = 6 (units)
flour = 6

# Cocoa Powder 0.5 cups = 6 (units)
cocoa_powder = 6

# Chocolate Chips 1.5 cups = 18 (units)
chocolate_chips = 18





# unsalted_butter
# granulated_sugar
# vanilla_extract
# large_eggs
# baking_soda
# salt
# flour
# cocoa_powder
# chocolate_chips

########################################
## -------------- Main -------------- ##
########################################

def main():
    # call header > Title Banner
    header()

    # call input func
    get_input()

    # call scaler
    scaler()


    # call footer > End of Program Banner
    footer()

########################################





# This function will display the header of the project
def header():
    print('----------------------------------------------')
    print('          Recipe of Choice Scaler          ')
    print("Select a recipe among 3 options, and scale it to your provided serving size!")
    print('----------------------------------------------')

    
    
# Interaction loop for inputs
def get_input(servings):


    # Prompt user to submit servings Store -> servings as int
    servings = int(input("Please enter your desired servings ..."))

    

    return servings
    # Get desired servings from user

    
# Scale selected recipe
def recipe_scaler():
    # 1 modify recipe variables while 2 handling unit escalation
# unsalted_butter = unsalted_butter
# granulated_sugar = 
# vanilla_extract = 
# large_eggs = 
# baking_soda = 
# salt = 
# flour = 
# cocoa_powder = 
# chocolate_chips = 



# Print scaled recipe
def print_scaled_recipe():
    #







# This function will display the end of the project
def footer():
    print('\n----------------------------------------------')
    print('End of Project')
    print('----------------------------------------------')

main() 












    

### BROWNIES RECIPE ###

"""

** Stored as teaspoons for whole number sake **



0.5 cup unsalted butter, melted and cool
1 cup granulated sugar
1 teaspoon vanilla extract
2 large eggs
0.25 teaspoon baking soda
0.25 teaspoon salt
0.5 cup flour
0.5 cup cocoa powder
1.5 cups of chocolate chips



Brownies Recipe

Source: (https://mytxkitchen.com/easy-homemade-brownies/)
   by: Alaine

0.5 cup unsalted butter, melted and cool
1 cup granulated sugar
1 teaspoon vanilla extract
2 large eggs
0.25 teaspoon baking soda
0.25 teaspoon salt
0.5 cup flour
0.5 cup cocoa powder
1.5 cups of chocolate chips

# unsalted_butter
# granulated_sugar
# vanilla_extract
# large_eggs
# baking_soda
# salt
# flour
# cocoa_powder
# chocolate_chips

Preheat oven to 350F, and line a 9"x 9" metal baking pan with parchment paper or aluminum foil. Melt 0.5 cups of butter on the stove-top or in the microwave in 20s intervals. Let it cool slightly.

TIP: Be sure butter mixture is not too hot before whisking in the eggs, otherwise you will risk cooking the eggs!

Whisk together the melted butter, 1 cup of granulated sugar, and 1 teaspoon of vanilla extract. Then whisk in 2 large eggs, and mix until incorporated fully. 

Add 0.25 teaspoons of baking soda and 0.25 teaspoons of salt, then add 0.5 cups of flour and cocoa powder to the wet ingredients. Stir until incorporated into batter, DON'T OVER STIR! 

Fold in the chocolate chips into the brownie batter.

The batter will be thick. Spread it into the prepared pan and bake @ 350F for 25-30m. 

Let cool for 30m before cutting.


"""