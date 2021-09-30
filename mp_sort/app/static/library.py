from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	result = list(range(0,number))
	random.seed(seed)
	random.shuffle(result)
	return result
	pass

def generate():
	global array
	number = 10
	seed = 200
	array = gen_random_int(number,seed)

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	pass

	string = ",".join(map(str,array))
	array_str = string + "."
		
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	pass

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	array_str = document.getElementById("generate").innerHTML
	array = array_str.split(",")
	array[len(array)-1] = array[len(array)-1].replace(".","")
	sortedarray = list(map(int,array))
	n = len(sortedarray)
	for i in range(1, n):
		j = i
		while (sortedarray[j] < sortedarray[j-1]):
			sortedarray[j], sortedarray[j-1] = sortedarray[j-1], sortedarray[j]
			j -= 1
			if j==0:
				break
	new_string = ",".join(map(str, sortedarray))
	array_str = new_string + "."
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	pass
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	list = value.split(",")
	new_array = []
	for i in list:
		new_array.append(int(i))
	n = len(new_array)
	for i in range(1, n):
		j = i
		while (new_array[j] < new_array[j-1]):
			new_array[j], new_array[j-1] = new_array[j-1], new_array[j]
			j -= 1
			if j==0:
				break
	new_string = ",".join(map(str, new_array))
	array_str = new_string + "."
	pass

	document.getElementById("sorted").innerHTML = array_str