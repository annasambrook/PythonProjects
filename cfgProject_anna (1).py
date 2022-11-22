# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:29:48 2022

@author: Anna
"""
import requests
import csv


def display_options():
    print("""
===== Additional Search Options =====
1. Dietary Requirement
2. Cook Time
3. Calories
4. None
          """)


# define recipe ingredient search
def recipe_search_ingredient(ingredient):
    url_ingredient = "&q=" + ingredient
    return url_ingredient


# define dietary restriction search
def dietary_restriction_search(dietary_requirement):
    url_dietary = "&health=" + dietary_requirement
    return url_dietary


def cook_time_search(cook_time):
    url_cook_time = "&time=" + cook_time
    return url_cook_time


def calories_search(calories):
    url_calories = "&calories=" + calories
    return url_calories


# define dietary requirements menu
# small demo list of dietary requirements
def display_dietary_requirements_menu():
    print("""
=== Dietary Requirements ===
1. Vegetarian
2. Vegan
3. Gluten Free
4. Lactose Free
    """)


def recipe_search(url_addition):
    app_id = "ce13ca6c"
    app_key = "8726ace363c7bec7e1f8f534de301da5"
    url_base = "https://api.edamam.com/search?app_id={}&app_key={}".format(app_id, app_key)
    full_url = url_base + url_addition
    response = requests.get(full_url)
    recipes = response.json()
    return recipes["hits"]


def print_results(results):
    for result in results:
        recipe = result["recipe"]
        print(recipe["label"])
        print("URL: " + recipe["url"])
        print("Total recipe calories: " + str(int(recipe["calories"])))
        print("Servings: " + str(recipe["yield"]))
        #        print("Dietary label: " + str(recipe["healthLabels"]))
        print()


# define main method
def run():
    choose_another_option = "y"
    dietary_requirement_choice = ""
    cook_time_choice = ""
    calories_choice = ""

    print("Welcome to the recipe search app!")

    ingredient = input("Enter an ingredient to use in your recipe: \n")
    ingredient_choice = recipe_search_ingredient(ingredient)

    while choose_another_option == "y":

        display_options()
        option_choice = input("Choose a search option (1-4) \n")

        if option_choice == "1":

            while option_choice == "1":
                display_dietary_requirements_menu()
                dietary_requirement_num = input("Enter dietary requirement (1-4): \n")

                if dietary_requirement_num == "1":
                    dietary_requirement = "vegetarian"
                    break

                elif dietary_requirement_num == "2":
                    dietary_requirement = "vegan"
                    break

                elif dietary_requirement_num == "3":
                    dietary_requirement = "gluten-free"
                    break

                elif dietary_requirement_num == "4":
                    dietary_requirement = "dairy-free"
                    break

                else:
                    print("Please choose a valid option choice (1-4)")
                    continue

            dietary_requirement_choice = dietary_restriction_search(dietary_requirement)

        elif option_choice == "2":
            cook_time = input("Enter maximum time for recipe completion (minutes): \n")
            cook_time_choice = cook_time_search(cook_time)

        elif option_choice == "3":
            calories = input("Enter calorie range per serving (e.g. 300-600): \n")
            calories_choice = calories_search(calories)

        elif option_choice == "4":
            break

        else:
            print("Please choose a valid option choice (1-4)")
            continue

        choose_another_option = input("Would you like to add another search field? (y/n) \n")

    url_addition = ingredient_choice + dietary_requirement_choice + cook_time_choice + calories_choice

    results = recipe_search(url_addition)

    print_results(results)

    # save results into csv file with ingredient as file name

    # with open(("recipe_search" + ingredient + ".csv"), "w", newline="\n") as file:
    #     writer = csv.writer(file, delimiter="|")
    #     writer.writerow(["Recipe", "URL", "Total recipe calories", "Servings"])
    #     for result in results:
    #         recipe = result["recipe"]
    #         writer.writerow([recipe["label"], recipe["url"], recipe["calories"], recipe["yield"]])
    # file.close()
    #
    for result in results:
        recipe = result["recipe"]
        f = open("recipe_search_" + ingredient + '.csv', "a")  # save results to csv file; a/append results as they are printed
        print(recipe["label"], file=f)
        print("URL: " + recipe["url"], file=f)
        print("Total recipe calories: " + str(int(recipe["calories"])), file=f)
        #        print("Dietary label: " + str(recipe["healthLabels"]), file=f)
        print(file=f)
        f.close()


run()
