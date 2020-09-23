'''
Question 3

Complete the body of the format_name function. 
This function receives the first_name and last_name parameters and then returns a properly formatted string.
'''




def format_name(first_name, last_name):
	# code goes here
	if first_name != "" and last_name != "":  # اذا كان الاسم الاول و الاسم الاخير موجودين اذا اطبع الاسم + الاسم الثاني 
        #string = first_name + ' , ' + last_name
        string = "Name: {} , {}".format(first_name,last_name)
    elif first_name != "" and last_name == "":
        string = "Name: " + first_name
    elif first_name == "" and last_name != "":
        string = string = "Name: " + last_name
    elif first_name == "" and last_name == "":
        string = ""
    
    # codes here 
    
	return string 

print(format_name("Ernest", "Hemingway"))  # --->  print(string) --- > print("Name: Hemingway, Ernest")


# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string