import substitute


def can_make_recipe(recipe, inventory):
	excact_missing = [thread for thread in recipe if thread not in inventory]
	subs = substitute.find_substitutes(excact_missing, recipe, inventory)	# I can image an implementation where this is not a function of recipe
	return excact_missing, subs


def all_makeable_recipes(recipe_book, inventory, num_willing_to_buy=3):
	for recipe in recipe_book:
		exact_missing, subs = can_make_recipe(recipe, inventory)
		num_missing = len(exact_missing)
		can_make = (num_missing == 0)
		can_make_with_subs = (len(subs) <= len(recipe) // 2)
		if can_make:
			print(f"{recipe} can be made")		# str(recipe) : f"{recipe.name} on page {recipe.page} of {recipe_book}" (str(recipe_book) : title)
		elif can_make_with_subs:				# len(recipe) : number of colors in recipe
			print(f"{recipe} can be made, if the following substitutions are made: ")
			for act, sub in subs:
				print(f"\t{act} -> {sub}")
		if num_missing <= num_willing_to_buy:
			start_of_message = "alternatively, " if can_make_with_subs else f"{recipe} can almost be made"
			print(f"{start_of_message}, the only missing colors are: {exact_missing}")
