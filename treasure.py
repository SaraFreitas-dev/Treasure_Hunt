# R is to avoid SyntaxWarning: invalid escape sequence '\`'

def start_game():

    print(r'''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[_______
    *******************************************************************************
    ''')

    print("\nWelcome to Treasure Island! \nYour mission is to find the treasure.")
    input("Click enter to start.")

    print("\n\nYou've obviously found yourself a pirate's treasure map somewhere. But it's not really readable.")
    print("Well, I guess we'll have to wing it...right? Let's go then!")
    print('''
          __________
         |####MAP###|
         |&&& ======|
         |   ')   * |
         | " (      |
         | "º )  '  |
         | ^   ( X  |
         |__________|
          ''')



    ########## LEVELS ########## 
    choice1 = input('\nYou\'re at a cross road. Where do you want to go?\nType "Left" or "Right": ').lower()

    if choice1 == "right":
        print(r'''     
         __/)     (\__
      ,-'~~(   _   )~~`-.
     /      \/'_`\/      \
    |       /_(_)_\       |
    |     _(/(\_/)\)_     |
    |    / // \ / \\ \    |
     \  | ``  / \ ''  |  /
      \  )   /   \   (  /
       )/   /     \   \(
       '    `-`-'-'    `
              ''')
        print("\nYou fell into a hole. Game Over.\n")
        
    elif choice1 == "left":
        print(r'''
              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
              ''')
        choice2 = input('\n\nYou\'ve reached a lake. \nType "Wait" to wait for a boat that\'s seen better days. \nType "Swim" to swim across and hope for the best: ').lower()

        if choice2 == "swim":
            print(r'''
                 |
                 |
                ,|.
               ,\|/.
             ,' .V. `.
            / .     . \
           /_`       '_\
          ,' .:     ;, `.
          |@)|  . .  |(@|
     ,-._ `._';  .  :`_,' _,-.
    '--  `-\ /,-===-.\ /-'  --`
   (----  _|  ||___||  |_  ----)
    `._,-'  \  `-.-'  /  `-._,'
             `-.___,-' 
                  ''')
            print('\nYou swam across the lake and got attacked by a crazy trout ! Game Over.\n')
            
        elif choice2 == "wait":
           print(r'''
                 
     .  o ..                  
     o . o o.o                
          ...oo               
            __[]__            
         __|_o_o_o\__         
         \""""""""""/         
          \. ..  . /          
     ^^^^^^^^^^^^^^^^^^^^  

                 ''')
           print('\nAfter a bumpy ride with a boat that seemed to be held together by duct tape and good intentions, you finally crash-land on the island.')
           input("Click enter to continue the adventure.\n")

           print('\n\nAs you explore the island, you encounter a group of mischievous monkeys who have taken over the place.\nThey’re swinging from trees, playing pranks, and occasionally throwing coconuts at each other.') 
           print(r'''
                                              .___.___.___.___.___.___.___.___..___.___..___.___..___.___..__.
                                            .'                                                                '.
                                           /  "Ah, another treasure hunter! One of the monkeys chimes in.       \
                                          |   We've hidden a few clues around here, but they're all tangled up   |
                                           \    in our monkey business. Good luck finding them!"                /
                                            '-.___.___.___.___.___.___.___.___.___..___.___..___.___..___.___.-'                     
                      __,__                      ______
             .--.  .-"     "-.  .--.           _____
            / .. \/  .-. .-.  \/ .. \       _____    
           | |  '|  /   Y   \  |'  | |    ____   
           | \   \  \ 0 | 0 /  /   / |  ___
            \ '- ,\.-"`` ``"-./, -' /  _ 
             `'-' /_   ^ ^   _\ '-'`       
             .--'|  \._ _ _./  |'--.    
           /`    \   \.-.  /   /    `\
          /       '._/  |-' _.'       \
         /          ;  /--~'   |       \
        /        .'\|.-\--.     \       \
       /   .'-. /.-.;\  |\|'~'-.|\       \
       \       `-./`|_\_/ `     `\'.      \
        '.      ;     ___)        '.`;    /
          '-.,_ ;     ___)          \/   /
           \   ``'------'\       \   `  /
            '.    \       '.      |   ;/_
          ___>     '.       \_ _ _/   ,  '--.
        .'   '.   .-~~~~~-. /     |--'`~~-.  \
       // / .---'/  .-~~-._/ / / /---..__.'  /
      ((_(_/    /  /      (_(_(_(---.__    .'
                | |     _              `~~`
                | |     \'.
                 \ '....' |
                  '.,___.'

                 ''')
           
           input("\nClick enter to investigate.\n")
           print("\n* Option 1: **Play Along with the Monkeys** – Join their antics and see if you can earn their trust or get clues from their playful nature.")
           print("* Option 2: **Search for Clues** – Look carefully around the area for any hidden hints or items amidst the monkeys' chaos.") 
           print("* Option 3: **Ignore the Monkeys** – Their antics might be distracting. Move on and find another way to continue your quest.\n") 
           choice3 = input("What option would you choose? Pick 1, 2 or 3: ")   

           if choice3 == "1":
               print(r'''
                        ____
                       / ___`\
           /|         ( (   \ \
      |^v^v  V|        \ \/) ) )
      \  ____ /         \_/ / /
      ,Y`    `,            / /
      ||  -  -)           { }
      \\   _\ |           | |
       \\ / _`\_         / /
       / |  ~ | ``\     _|_|
    ,-`  \    |  \ \  ,//(_}
   /      |   |   | \/  \| |
  |       |   |   | '   ,\ \
  |     | \   /  /\  _/`  | |
  \     |  | |   | ``     | |
   |    \  \ |   |        | |
   |    |   |/   |        / /
   |    |        |        | |

                     ''')
               print("\nThe monkeys love your company and make you their king. Who needs treasure when you have a banana throne? Still, it's Game Over.\n")

           elif choice3 == "2":
               print(r'''
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
                     ''')
               print("\nYou try to juggle bananas to impress the monkeys, but slip and fall into a ravine. Game Over.\n")
           elif choice3 == "3":
               print(r'''
                         ,,,,,,
                        /e   ''(
                       (_ `     \
                      ___>       \
                     / ,_\-.___   \_
                    /  _)/ /        \
                    |  \  /  ` _     |
                  __\____/    /    ' |
                 /  _        /______/
                / _/ \,_____/o     (
                \__)/`              \
                   /   \__________/_/_
                 _/     \  \   )/     \
                /      /   |  /\      (
                \_____/ ___/  \ \  _/  \
           ______/_/___|_|     ) \     /
          /       o\     o\   /  /    /\
  b'ger,,,'-----^--',,,,,,',,|_,,\_ ,,\/,,
                     ''')
               choice4 = input('\n\nIgnoring the monkeys\' distractions, you spot a barely noticeable path. \nFollowing it, you arrive at a clearing with a "Cave" and a small "Cabin". Which one holds the treasure?  ').lower()

               if(choice4 == "cave"):
                  print(r'''                              
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⢀⣿⣿⣿⣦⣾⣿⣦⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⣋⣽⡟⢉⣷⠞⠉⠀⠺⠛⠛⣻⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⣒⣯⣵⠖⠛⢉⡠⠤⣾⡟⢀⠀⠀⠀⠙⣧⡻⢟⣿⡿⣶⣦⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⢒⡿⠛⠉⠉⠋⠁⠀⢰⣿⠁⢀⣿⠁⣿⡄⠀⠺⣿⣤⠉⣁⣀⠀⠀⣹⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣳⣾⡟⠀⠀⠀⠀⠀⣸⡇⢸⣿⡀⠈⠿⣧⣌⠙⠳⠀⠈⠁⣼⡟⣿⠟⠿⠛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢑⣿⡿⠁⠀⠀⠀⠀⠀⢻⣇⠈⠹⣷⣄⠀⠈⠛⠣⣀⣀⢀⣄⣋⣑⡛⠛⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣡⠏⢉⣁⣠⡤⠤⢤⣀⡠⣿⡿⠀⠀⣦⣍⣷⣦⣶⣾⡿⠿⠟⠀⠀⠁⠈⠙⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⣷⡀⢾⣤⡀⠉⠀⠀⠀⠀⢍⡛⢧⡀⠀⠈⢡⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣇⠻⣷⣄⣉⣛⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠒⠻⢿⣿⡟⠃⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⢿⣏⣿⣦⣍⡛⢻⣛⠛⡛⠛⠉⠀⠀⠀⠀⠀⢀⣴⠾⢚⡿⠷⠤⡼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⠁⢸⣏⢹⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣷⠲⠷⣄⠀⣡⠾⠋⢡⡘⣦⣧⡙⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠗⠁⠀⠈⢿⣆⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣨⡷⢦⣴⣽⣶⣿⠟⠋⠻⣦⡝⠢⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣫⠄⠀⠀⠀⠈⠻⣦⠸⡿⢿⣿⣿⣿⣿⣿⠙⠻⠿⣿⠟⢳⣾⣿⣿⣿⣶⣒⡀⠀⠀⠛⢧⡀⠙⢆⠀⠀⠀⠀
⠀⠀⠀⣽⣡⠂⠀⠀⠀⠀⠀⢻⣄⠘⣄⠉⠛⠻⣿⡟⠀⠀⠀⡀⠀⣸⡅⠀⠙⠿⣿⣿⣿⣧⣤⠀⠈⢻⣆⢸⣄⠀⠀⠀
⠀⠀⠀⢹⢇⠀⠀⠀⠀⠀⠛⢿⣿⠳⢼⣶⣤⡶⠀⠀⠀⠀⣰⡿⠐⢿⡇⠀⠀⠀⠈⠉⠻⢿⣿⣿⣧⣄⠉⠀⠉⠳⡄⠀
⠀⠀⠀⢸⠸⣷⡀⠀⠀⠀⠀⠀⠙⣦⡈⣿⡋⠀⠀⠀⢀⣠⡿⠃⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⢿⣷⣦⣄⡀⢧⠀
⠀⠀⠀⢸⡄⠙⢿⣄⠀⠀⠀⠀⠀⠈⢻⣽⣷⣤⡀⠀⠞⠋⢀⢀⣀⣼⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣿⣿⡇⣸⠀
⠀⠀⠀⢠⣧⡀⠀⢙⠛⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣦⣄⣼⣿⡟⠋⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⠛⠁⠀
⠀⠀⠀⠈⣿⠇⠀⢾⣤⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⢷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⣿⡤⠀⢸⡟⠀⠀⠀⠀⢠⣾⢻⣿⣿⣿⣿⡿⠟⠠⠤⣤⣀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣽⠁⣠⠏⠀⢾⣧⣤⣾⣏⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣥⣄⣠⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡾⢁⣼⡏⠀⠀⠀⠀⠀⣼⡿⠋⠛⢿⣿⢿⡯⠤⠤⠖⠚⠉⠉⠙⠛⠃⣠⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠟⠁⠸⠿⢟⣠⣄⣠⣴⣿⢧⡀⠀⠀⠀⢀⡞⠀⠐⠀⢀⣴⡤⠤⠤⢴⣾⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⠀⠀⠀⠀⠈⠹⠽⠻⣉⢻⡓⣾⣦⠀⠀⠘⠧⣄⣀⣀⣈⠀⣀⣀⠀⠀⠉⢹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠦⠤⠖⠒⠒⠲⠦⠤⣾⣾⣽⢿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ''') 
                  print("\nYou bravely enter the cave and come face-to-face with the bear from every scary story ever.\nYou didn't even get a chance to scream. Guess what? Game Over.\n")

               elif(choice4 == "cabin"):
                   print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
                         ''')
                   print("You find a trapdoor beneath the floorboards, and voilà—treasure! \nLooks like the cabin was more of a “sitting on gold” situation. You Win!")
               else:
                  choice4 = input('\n[INVALID ANSWER]\nIgnoring the monkeys\' distractions, you spot a barely noticeable path. \nFollowing it, you arrive at a clearing with a "Cave" and a small "Cabin". Which one holds the treasure?  ').lower()   
           else:
               choice3 = input('\n[INVALID ANSWER]\nWhat option would you choose? Pick 1, 2 or 3: ').lower()                 
        else:
           choice2 = input('\n[INVALID ANSWER]\nYou\'ve come to a lake. \nType "Wait" to wait for a boat. \nType "Swim" to swim across.').lower()   


    else:  
        choice1 = input('\n[INVALID ANSWER]\nYou\'re at a crossroad. Where do you want to go?\nType "left" or "right": ').lower()




##########  Game loop ########## 
while True:
    game_over = start_game()
    
    if game_over:
        retry = input("Would you like to start again? Type 'yes' or 'no': ").lower()
        if retry != 'yes':
            break
    else:
        retry = input("Would you like to start again? Type 'yes' or 'no': ").lower()
        if retry != 'yes':
            break
        
