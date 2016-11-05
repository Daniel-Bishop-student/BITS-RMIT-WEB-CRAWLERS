## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.


## The game starts here.

label scene2:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene scene2

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show harry happy
    show benji neutral at Position(xpos=0.6, xanchor='center', ypos=1.08,
                   yanchor='bottom')
    show penny neutral at Position(xpos=0.4, xanchor='center')
    show jax at Position(xpos =0.7) 
    
    ## These display lines of dialogue.

    penny "Wow Harry what a great phone" 
    harry "Yeah it came with a very strange note in the box though"
    benji "What did it say"
    harry "The curious mind must be matched with a brave heart and kind soul"
    penny  "What do you suppose it means Harry?"


    ##Big Noise - Train derailing


    "ah, what?"


    jump scene3
    ## This ends the game.

    return
