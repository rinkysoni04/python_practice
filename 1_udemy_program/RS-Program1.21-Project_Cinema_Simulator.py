# Create dictionary of films

films={"AVATAR": [3, 5],
       "RRR": [15, 5],
       "KANTARA": [18, 5],
       "KGF": [18, 5],
       "PUSHPA": [18, 5]
       }



while True:

    # Ask user to enter their choice of movie

    choice = input("Which movie would you like to watch?").strip().upper()

    #print("i am here {}".format(choice))


    if choice in films:

        #check age of the user



        age = int(input ("How old are you?").strip())

        if films[choice][0]<=age:

            #check no. of available seats

            if films[choice][1]>0:

             #deduct 1 from available seats

               films[choice][1]=films[choice][1] - 1

               print("Enjoy the movie!")

            else:
               print("Sorry! We are sold out..")
        else:
            print("Sorry! You are too young to watch this movie...")


    else:
        print("Sorry! We dont have that movie.")




