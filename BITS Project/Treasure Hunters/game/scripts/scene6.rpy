label scene6:
    
    scene scene6-7a
    with fade

    $ renpy.music.set_volume(0.6, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 6.0 

    play sound "FX/scene6_Suspense.mp3"
    
    show harry mad at Position(xpos=0.5, ypos=0.95)
    show benji mad at Position(xpos=0.25, ypos=0.95)
    show penny mad at Position(xpos=0.65, ypos=0.95)
    show jax mad at Position(xpos =0.75)
    show slim mad at Position(xpos=0.37, ypos=0.95)
    show killsalot mad1 at Position(xpos=0.90, ypos=0.95)


    # Dialogue for scene6

    killsalot "Well, well, well. What have we got here? "

    slim "Its Killsalot! This is the evil leader of the soldiers that attacked our world!"

    killsalot mad2 "I believe you have something I want."

    slim "We have nothing!" 

    killsalot mad1 "Not you, him! The transporter, give it to me!"

    harry surprised "Transporter? What I don’t.."

    penny sad "I think he means your phone %(harry_name)s..."

    benji surprised "He can’t have it or we’ll never get home!"

    slim "%(benji_name)s is right and with the transporter he will be able to terrorise dimensions other than our own and possibly yours %(harry_name)s."
    
    killsalot mad3 "The Transporter! Give it to me or it will be taken from you. Soldiers, grab them!"

    show penny mad at Position(xpos=0.42, ypos=0.95)
    with dissolve
    show jax mad at Position(xpos =0.30)
    with dissolve
    show killsalot mad2 at Position(xpos=0.90, ypos=0.95)
    show soldiers at Position(xpos=0.70)
    with dissolve 


    group surprised "You turn to run but the soldiers grab everyone but you manage to get away"

    show harry mad at Position(xpos=0.25, ypos=0.95)
    show benji mad at Position(xpos=1.0, ypos=0.95)
    show penny mad at Position(xpos=1.0, ypos=0.95)
    show jax mad at Position(xpos =1.0)
    show slim mad at Position(xpos=1.0, ypos=0.95)


    killsalot "Come out with that transporter boy, or I will kill your friends…. Slowly and make you watch."


#(Harry) Reveals himself holding up the transporter in one hand:
    harry "Let them go, Killsalot, or I will smash this transporter!"


    killsalot mad2 "Ahh, such bravery, such sacrifice. You have impressed me, boy."

    killsalot mad3 "Give to me the transporter and, as I am nothing if not gracious, I will release you and your friends"

    killsalot mad1 "You will be allowed to leave this place without any harm coming to you. You have my word."
    

    #######CHOICE SECTION#########

    choice "Killsalot wants you to give him your phone. What will you do? Continue to make your choice."

    
    menu:
        "Give the transporter to Killsalot and save your friends.":
            jump choice3

        "​Smash the phone.":
            jump choice4

label choice3:
    play sound "FX/scene6_Evil_Laugh.mp3"
    
    narrator "You didn’t actually think that would work do you?"
    narrator "Killsalot was lying through his crooked black teeth." 
    narrator "He kills Slim and Jax, forces %(penny_name)s to marry him and turns %(benji_name)s and you into live punching bags for his soldiers."
    narrator "Then he uses the transporter to terrorise the Universe, enslaving all that get in his way... Bad choice and your adventure ends here."

    stop sound

    return
    
label choice4:
    "You smash the phone knowing your friends may die there in front of you but that the sacrifice must be made in order to save the Universe. The transporter, sensing your despair and anger, starts to glow and..."

    stop music fadeout 1.0

    jump scene7a
    
    return 
