label scene6:
    
    scene scene6-7a
    with fade

    

    show harry mad
    show benji mad at right
    show penny mad at left
    show jax mad at Position(xpos =100)
    show slim mad
    show killsalot mad1 at Position(xpos=600)
    show choice

    # Dialogue for scene6

    killsalot " Well what have we got here? "
    slim "Killsalot, the leader of the soldiers that attacked us "
    killsalot  "I believe you have something I want "
    slim "We have nothing" 
    killsalot "Not you, him!, the transporter, give it to me!"
    harry "Transporter? What I don’t.."
    penny "I think he means your phone Harry"
    benji "He can’t have it or we’ll never get home "
    slim "He’s right and with the transporter he will be able to terrorise dimensions other than ours and possibly yours Harry"
    killsalot "The Transporter! Give it to me or it will be taken from you, Soldiers, grab them!"


#The gang turns to run but the soldiers grab the everyone except for Harry who makes it to a nearby cave?? and hides.


    killsalot "Come out with that transporter boy, or I will kill your friends…. Slowly and make you watch"


#(Harry) Reveals himself holding up the transporter in one hand:
    harry "Let them go, Killsalot, or I will smash this transporter"


    killsalot "Ahh, such bravery, such sacrifice. You have impressed me, boy. Give to me the transporter and, as I am nothing if not gracious, I will release you and your friends and you will be allowed to leave this place without any harm coming to you. You have my word"
    

    #######CHOICE SECTION#########

    choice "Killsalot wants you to give him your phone. What will you do? Continue to make your choice"

    
    menu:
        "Give the transporter to Killsalot and save your friends.":
            jump choice3

        "​Smash the phone.":
            jump choice4

label choice3:
    
    "You didn’t actually think that would work do you? Killsalot was lying through his crooked black teeth. He kills Slim and Jax, forces Penny to marry him and turns Benji and you into live punching bags for his troops. Then he uses the transporter to terrorise the Universe, enslaving all that get in his way….. Bad choice and your adventure ends here."
    return
label choice4:
    "You smash the phone knowing your friends may die there in front of you but that the sacrifice must be made in order to save the Universe. The transporter, sensing your despair and anger, starts to glow and…"

    jump scene7a
    

    return 
