label scene6:
    
    scene scene6
    with fade

    

    show harry
    show benji at right
    show penny at left
    show jax at Position(xpos =100)
    show killsalot at Position(xpos=600)

    #show # harry surprised
    #show # penny surprised at Position right
    #show # benji surprised at Position left
    #show jax at Position (xpos = 100)
    #show slim happy at Position ? 
    # fade all characters in and make transperent?

    # Dialogue for scene6

    killsalot surprised "Well what have we got here?"
    slim mad "Killsalot, the leader of the soldiers that attacked us!"
    killsalot mad1 "I believe you have something I want..."
    slim mad "We have nothing" 
    killsalot mad2 "Not you, him!, the transporter, give it to me!"
    harry confused "Transporter? What I don’t..."
    penny mad "I think he means your phone Harry"
    benji surprised "He can’t have it or we’ll never get home "
    slim mad "He’s right and with the transporter he will be able to terrorise dimensions other than ours and possibly yours Harry"
    killsalot mad3 "The Transporter! Give it to me or it will be taken from you, Soldiers, grab them!"


    soldiers gang "{i}The gang turns to run but the soldiers grab the everyone except for Harry who makes it to a nearby cave?? and hides.{/i}"


    killsalot mad1 "Come out with that transporter boy, or I will kill your friends…. Slowly and make you watch"


    harry mad "{i}{b}(Harry) Reveals himself holding up the transporter in one hand:{/b}{/i}"
    harry mad " Let them go, Killsalot, or I will smash this transporter"


    killsalot mad2 "Ahh, such bravery, such sacrifice. You have impressed me, boy. Give to me the transporter and, as I am nothing if not gracious, I will release you and your friends and you will be allowed to leave this place without any harm coming to you. You have my word"
    

    #######CHOICE SECTION#########

    choice_character choice "Choose wisely!"
    
    menu:
        "Give the transporter to Killsalot and save your friends!":
            jump choice3

        "​Smash the phone!":
            jump choice4

label choice3:
    
    "You didn’t actually think that would work do you? Killsalot was lying through his crooked black teeth. He kills Slim and Jax, forces Penny to marry him and turns Benji and you into live punching bags for his troops. Then he uses the transporter to terrorise the Universe, enslaving all that get in his way….. Bad choice and your adventure ends here."
    return
label choice4:
    "You smash the phone knowing your friends may die there in front of you but that the sacrifice must be made in order to save the Universe. The transporter, sensing your despair and anger, starts to glow and…"

    jump scene7a
    

    return 
