## The script of the game goes in this file.
# Run the declarations and code stored in the declarations directory
call image_declarations
call character_declarations
# call other_declarations
## Declare characters used by this game. The color argument colorizes the name
## of the character.


## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene scene1

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show harry happy
    show benji neutral at right
    show penny neutral at left
    show jax at Position(xpos =100) 
    ## These display lines of dialogue.

    "Happy Birthday dear Harry, happy birthday to you"

    grandma "Open your present Harry"

    harry "It's a new phone !, thanks Grandma"

    jump scene2
    ## This ends the game.


    return