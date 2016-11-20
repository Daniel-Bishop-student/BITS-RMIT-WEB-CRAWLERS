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

    "Before we start this adventure, you, the reader, get to choose the names of the the three main characters."
    choice "Would you like to change them?"

    $ harry_name = "Harry"
    $ benji_name = "Benji"
    $ penny_name = "Penny"
    
    menu:
        "Yes":
            $ harry_name = renpy.input("Enter a new name for Harry!")
            $ harry_name = harry_name.strip()
            

            $ benji_name = renpy.input("Enter a new name for Benji!")
            $ benji_name = benji_name.strip()
            

            $ penny_name = renpy.input("Enter a new name for Penny!")
            $ penny_name = penny_name.strip()

        "​no":
            "Lets continue then!"

    group "Happy Birthday dear %(harry_name)s, Happy Birthday to you!"

    jax "Woff Woof"

    grandma "Open your present %(harry_name)s..."

    harry "It's a new phone! Thanks Grandma!"

    stop music fadeout 1.0

    jump scene2

    return