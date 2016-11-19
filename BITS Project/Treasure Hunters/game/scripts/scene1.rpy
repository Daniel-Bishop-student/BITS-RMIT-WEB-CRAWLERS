## The game scene here.

label scene1:

    $ renpy.music.set_volume(0.3, 0, channel='music')

    play music "FX/scene1_happy_birthday.mp3" fadeout 2.0 fadein 1.0 

    scene scene1

    show harry happy at Position(xpos=0.5, ypos=0.95)
    show benji happy at Position(xpos=0.25, ypos=0.95)
    show penny happy at Position(xpos=0.70, ypos=0.95)
    show jax at right
    show grandma at Position(xpos=0.37)

    
    # Dialogue for scene1

    group "Happy Birthday dear Harry, happy birthday to you!"

    grandma "Open your present Harry..."

    harry "It's a new phone! Thanks Grandma!"

    stop music fadeout 1.0

    jump scene2

    return