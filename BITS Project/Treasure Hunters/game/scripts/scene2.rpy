# The scene starts here.

label scene2:

    scene scene2 

    $ renpy.music.set_volume(0.3, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene2aFXtraffic.mp3" fadeout 0.5 fadein 4.0 
    play sound "FX/scene2FXcafe.mp3" fadeout 0.5 fadein 4.0 

    show harry happy at Position(xpos=0.5)
    show benji happy at Position(xpos=0.25)
    show penny happy at Position(xpos=0.70)
    show jax at Position(xpos=0.85, ypos=1.05)
    
    # These display lines of dialogue.

    penny "Wow Harry, what a great phone." 

    harry "Yeah it came with a very strange note in the box though."
    
    benji "What did it say?"
    
    harry "{i}'The curious mind must be matched with a brave heart and kind soul.'{/i}"
    
    penny  "What do you suppose it means Harry?"

    play music "FX/scene2_Train_Honk_Horn.mp3"

    group surprised "Ahh, What!?"

    stop music fadeout 1.0
    stop sound

    jump scene2a
    # This ends the game.

    return
