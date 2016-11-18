# You can place the script of your game in this file.

label scene2a:

    scene scene2a

    # code for playing music

    # Dialogue for scene2a

    penny "Harry! I think your new phone is ringing"

    choice "What do you do? Try to save your group from getting crushed by the tram or answer the phone? Continue to make your choice...."

    menu:
        "Ignore the phone and try to get your friends out of the way of the tram?":
            jump choice1

        "​Ignore the onrushing tram and answer the phone: Result - You answer the phone and it starts to glow":
            jump scene3

label choice1:
    
    "As quick as you think you are, the tram is quicker. It runs straight through the middle of all of you, tearing flesh and slicing limbs, crushing you with it’s heavy metal bulk. You, and your group are killed. Your adventure ends here. "
    
    jump credits
    
    return
