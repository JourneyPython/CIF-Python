def adventure():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest with two paths ahead.")
    
    choice = input("Do you want to go left or right? (left/right): ").strip().lower()

    if choice == "left":
        print("You walk down the left path and encounter a scary dragon!")
        action = input("Do you want to befriend the dragon or run away? (befriend/run): ").strip().lower()
        
        if action == "befriend":
            print("The dragon becomes your ally!")
            if input("Do you want to go on a treasure hunt with the dragon? (yes/no): ").strip().lower() == "yes":
                print("You and the dragon find a hidden treasure chest filled with gold!")
            else:
                print("You decide to just enjoy the dragon's company and exit the forest safely.")
        else:
            print("You run away, but miss out on a great adventure.")
            reaction = input("You come across an elf who offers you a magical potion. Do you accept it? (yes/no): ").strip().lower()
            
            if reaction == "yes":
                print("The potion grants you invisibility! You safely exit the forest.")
            else:
                print("You decline the potion and continue your journey, but get lost in the forest.")
                response = input("A fairy appears and offers to guide you out. Do you accept? (yes/no): ").strip().lower()
                
                if response == "yes":
                    print("The fairy turns into a goblin and kidnaps you! You are trapped in the forest forever.")
                else:
                    print("You wander aimlessly until you find your way out of the forest.")

    elif choice == "right":
        print("You walk down the right path and fall into a deep pit.")
        action = input("Do you want to try to climb out or call for help? (climb/call): ").strip().lower()
        
        if action == "climb":
            print("You manage to climb out of the pit and continue your journey!")
            act = input("You see something shiny in the distance. Do you want to investigate? (yes/no): ").strip().lower()
            
            if act == "yes":
                print("You accidentally walk into a gryphon nest!")
                next = input("The gryphons are angry. Do you want to apologize or run away? (apologize/run): ").strip().lower()
                
                if next == "apologize":
                    print("The gryphons forgive you and share their treasure with you. You exit the forest rich!")
                else:
                    print("You try to run, but the gryphons catch you. You are trapped in the forest forever.")
            else:
                print("You decide to ignore it and walk away.")
                step = input("You reach a fork in the road. Do you want to go east or west? (east/west): ").strip().lower()
                
                if step == "east":
                    print("You find a unicorn who you befriend. You exit the forest safely with your new friend.")
                else:
                    print("You come across a hydra who chases you away. You are trapped in the forest forever.")
        
        else:
            print("Uh oh! An ogre hears your calls and rescues you, but demands a toll of your gold coins.")
            result = int(input("Will you pay the toll? (1 for yes, 0 for no): "))
            
            if result == 1:
                reaction = int(input("How many gold coins will you give the ogre? "))
                
                if reaction > 10:
                    print("You pay the toll and the ogre lets you go.")
                    move = input("Do you want to head north or south? (north/south): ").strip().lower()
                    
                    if move == "north":
                        print("You find a peaceful village and live happily ever after.")
                    else:
                        print("You wander into a swamp and get stuck forever.")

                else:
                    print("The ogre is angry and forces you to work in the mines to pay him back! You are trapped in the forest for eternity.")
            
            else:
                print("The ogre is angry and takes all your belongings! You are trapped in the forest for eternity.")

    else:
        print("Your indecision leads you to stay in the same spot forever. A witch finds you and turns you into a frog!")
    
adventure()