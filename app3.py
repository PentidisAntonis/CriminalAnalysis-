#print("Please enter a value- text")
#user_text = input()
#print(user_text)

#text= input('Enter a title:')
#print(len(text))

#password = input('Enter password:')

#while password != "pas123":
   # password = input('Wrong password, enter correct password:')

#print("Correct password")

#name = input('Enter name:')

#while name != "end":
#    print(name.capitalize())
 #   name = input('Enter name:')

while True:
    user_action = input("Type add, edit, show or exit command: ")
    user_action = user_action.strip()

    match user_action:
        case "add":

        case "edit":