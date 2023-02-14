#Create list of known users

known_users=["Rajkumar", "Rajkumari", "Rajul", "Rinky", "Sonu", "Sooraj"]

while True:  
#Let Travis introduce itself
   print("Hi! My name is Travis. Welcome to my World :)")

#Take name as input from user & store it in a variable
   name=input("What is your name?: ").strip().capitalize()

#Check if the name is available in the list or not. if available; ask if they want to leave if not then ask if they want to join. Remove or add accordingly & print message.

   if name in known_users:
        print("Hello {}!".format(name))
        remove=input("Would you like to be removed from the system?: ").strip().lower()
        
      if remove=="y":
         print(known_users)
         known_users.remove(name)
         print(known_users)
      elif remove=="n":
           print("No problem! I didnt want you to leave anyway :)")
   else:
        print("Oops! I dont think I have met you yet {}!".format(name))
        add_me=input("Would you like to be added to the system (y/n)?: ").strip().lower()
        
      if add_me=="y":
         Print(known_users)
         known_users.append(name)
         print(known_users)
      elif add_me=="n":
         print("No problem! See you around!")
            






