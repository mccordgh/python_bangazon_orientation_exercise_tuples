zoo = ("Racoon", "Monkey", "Red Panda", "Zebra")
new_zoo_list = ()

(racoon, monkey, red_panda, zebra) = zoo

zoo_list = [racoon, monkey, red_panda, zebra]

zoo_list.extend(["Llama", "Lizard", "Fox"])

new_zoo_tuple = tuple(zoo_list)


def checkForAnimal(user_animal):
	
	'''
	Checking if the animal entered by the user is in our zoo list of animals
	If it is, return True
	If it is not, return False
	'''
	
	for animal in zoo_list:
		if animal == user_animal:
			return True
	return False

print('Our Zoo Has These Animals:\n  {0}'.format(zoo_list))
user_animal = input("Enter an animal name.\n")
check = checkForAnimal(user_animal)

if check == True:
	print('The {0} is found in our zoo!'.format(user_animal))
else:
	print('The {0} is NOT found in our zoo!'.format(user_animal))