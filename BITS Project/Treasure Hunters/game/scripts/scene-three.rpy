# You can place the script of your game in this file.

label scene3:

    scene scene3

    #show # harry surprised
    #show # penny surprised at Position right
    #show # Benji surprised at Position left
    #show jax at Position (xpos = 100)

    # Dialogue for scene 3

    # code for playing music

    penny "Harry! I think your new phone is ringing"

    "What do you do? Try to save your group from getting crushed by the tram or answer the phone?"

    menu:
        "Ignore the phone and try to get your friends out of the way of the tram?":
            jump choice1

        "​Ignore the onrushing tram and answer the phone: Result - You answer the phone and it starts to glow":
            jump scene4

label choice1:
    
    "As quick as you think you are, the tram is quicker. It runs straight through the middle of all of you, tearing flesh and slicing limbs, crushing you with it’s heavy metal bulk. You, and your group are killed. Your adventure ends here. "

    return
