def format_name(first_name, last_name):
	# code goes here
	string = ""
	if first_name !="" and last_name!="":
	  string = "Name: {}, {}".format(last_name,first_name)
	elif first_name =="" and last_name=="":
	  string = ""
	elif first_name =="":
	  string = "Name: {}".format(last_name)
	elif last_name =="":
	  string = "Name: {}".format(first_name)
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string