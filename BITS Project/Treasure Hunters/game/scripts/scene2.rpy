# The scene starts here.

label scene2:

    scene scene2

    show harry
    show benji at Position(xpos=0.6, xanchor='center', ypos=1.08,
                   yanchor='bottom')
    show penny at Position(xpos=0.4, xanchor='center')
    show jax at Position(xpos =0.7) 
    
    # These display lines of dialogue.

    penny happy "Wow! Harry what a great phone!" 
    harry surprised "Yeah it came with a very strange note in the box though..."
    benji surprised "What did it say?"
    harry excited "The curious mind must be matched with a brave heart and kind soul..."
    penny happy "What do you suppose it means Harry?"


    #Big Noise - Train derailing
    # http://www.flashkit.com/soundfx/Transportation/Crashes/Skidstop-public_d-313/index.php
    play sound "FX/Skidstop-public_d-313_hifi.mp3"
    harry confused "ah, what?"


    jump scene2a
    # This ends the game.

    return
