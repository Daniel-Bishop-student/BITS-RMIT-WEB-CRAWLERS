# You can place the script of your game in this file.

label scene2a:

    scene scene2a

    $ renpy.music.set_volume(0.3, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene2a_train_screech.mp3" fadeout 0.5 fadein 1.0 

    show harry surprised at Position(xpos=0.5, ypos=0.95)
    show benji surprised at Position(xpos=0.25, ypos=0.95)
    show penny mad at Position(xpos=0.70, ypos=0.95)
    show jax at right

    # Dialogue for scene2a

    group surprised "Look out! The tram has derailed!!"

    play sound "FX/scene2a_harry_phone.mp3"

    penny "Harry! I think your new phone is ringing!"

    choice "What do you do? Try to save your group from getting crushed by the tram or answer the phone? Continue to make your choice...."

    menu:
        "Ignore the phone and try to get your friends out of the way of the tram?":
            jump choice1

        "​Ignore the onrushing tram and answer the phone... ":
        
            jump choice2

label choice2:
    
    "You answer the phone and it starts to glow...."

    jump scene3

label choice1:

    play music "FX/scene2a_Train_Hits_Group.mp3" noloop

    play sound ["<silence 5.0>", "FX/endingChoice1.mp3"]
    
    "As quick as you think you are, the tram is quicker. It runs straight through the middle of all of you, tearing flesh and slicing limbs, crushing you with it’s heavy metal bulk. You, and your group are killed. Your adventure ends here. "

    stop music fadeout 1.0

    return
