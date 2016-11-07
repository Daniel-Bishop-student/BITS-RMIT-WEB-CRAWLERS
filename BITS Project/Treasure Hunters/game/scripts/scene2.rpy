# The scene starts here.

label scene2:

    scene scene2

    show harry
    show benji at Position(xpos=0.6, xanchor='center', ypos=1.08,
                   yanchor='bottom')
    show penny at Position(xpos=0.4, xanchor='center')
    show jax at Position(xpos =0.7) 
    
    # These display lines of dialogue.

    penny "Wow Harry what a great phone" 
    harry "Yeah it came with a very strange note in the box though"
    benji "What did it say"
    harry "The curious mind must be matched with a brave heart and kind soul"
    penny  "What do you suppose it means Harry?"


    #Big Noise - Train derailing


    "ah, what?"


    jump scene2a
    # This ends the game.

    return
