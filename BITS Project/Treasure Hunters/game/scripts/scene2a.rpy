# You can place the script of your game in this file.

label scene2a:

    scene scene2a

    show harry
    show benji at right
    show penny at left
    show jax at Position(xpos =100)

    #show # harry surprised
    #show # penny surprised at Position right
    #show # Benji surprised at Position left
    #show jax at Position (xpos = 100)

    # code for playing music

    # Dialogue for scene2a

    penny surprised "Harry! I think your new phone is ringing..."
    # http://www.flashkit.com/soundfx/Communication/Telephones/Mr-Steven_B-7370/index.php
    play sound "FX/Mr-Steven_B-7370_hifi.mp3"

    choice_character choice "What do you do? Try to save your group from getting crushed by the tram or answer the phone?"

    menu:
        "Ignore the phone and try to get your friends out of the way of the tram?":
            jump choice1

        "​Ignore the onrushing tram and answer the phone?":
            jump scene3

label choice1:
    
    "As quick as you think you are, the tram is quicker. It runs straight through the middle of all of you, tearing flesh and slicing limbs, crushing you with it’s heavy metal bulk. You, and your group are killed. Your adventure ends here. "

    return
