label scene7a:
    
    scene scene6-7a
    with fade

    $ renpy.music.set_volume(0.8, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 1.0 

    show harry mad
    show benji mad at right
    show penny mad at left
    show jax mad at Position(xpos =100)
    show slim mad
    show killsalot mad1 at Position(xpos=600)

    # Dialogue for scene7
    
    ######Scene 7a#######
    killsalot "Attack them!!"

    play sound "FX/scene7_shooting.mp3" loop

    soldiers "Many soldiers rush to Harry, Slim and the gang."
    benji "Harry your phone, it’s glowing again!"

    stop sound

    play sound "FX/transporter.mp3"

    group surprised "A big flash and the gang, including Jax, are now in battle suits bristling with special weapons!"

    penny "LET'S GET IT ON!"

    play sound "FX/scene7_shooting.mp3" loop

    #####Battle Scene - kids fighting soldiers 7b? ###############
    group surprised "You and your group fight a desparate battle....."

    benji "Harry there’s too many!"
    slim "He’s right! You must retreat Harry. You must not let the transporter fall into Killsalot’s hands."
    penny "Use the transporter Harry! Get us out of here!"
    slim "No! Remember, the Rebellion is nearby. If we can find them, they may be able to help us."

    stop sound 

    #######CHOICE SECTION#########

    
    menu:
        "You don’t need any help, and only cowards run away. Stay and fight!":
            jump choice5

        "​Use transporter to escape.":
            jump choice6

        "​Run and try to find the rebellion.":
            jump choice7

label choice5:

    play sound "FX/scene7_shooting.mp3" loop
    
    "Harry hears his friend’s words but all he sees is red. His is pumped up, he is angry and he wants blood. Something deep within him has awoken."


    "There is a lull in the fighting as Killsalots men regroup..."


    harry "NO! Here is where we stand, here is where we fight back. If we run now, we will never stop running."


    slim "We must do what the Protector needs us to do. Stand together. Stand and fight!"


#####Cut scenes as each of the group get their own brief close up in a battle pose.######


    "Suddenly Benji get hit and goes down, swamped by Kilsalots soldiers."

    harry "Benji!"
    slim "You can’t stop to help!"

    show penny sad 
    penny "But I have to!"


    "Penny goes to Benji’s aid but is cut down down before she can help..."


    harry "NOOOOO!"
    slim "You must hold fast! We can help them when we have finished this fight!"


    "It’s too much for Harry who calls Jax to his side and they both charge the enemy. Jax is killed and Harry runs out of ammunition. Just before he his shot, Slim jumps in and takes the bullet."


    harry "RRRAAAAGGHHH"

    stop sound

    play sound "FX/scene7_battle.mp3"


    "Harry charges, Killsalots men with his bare hands."# Fade to black


##This text comes up over black screen: 


    "You fought bravely, you fought well, and many of Killsalots soldiers were sent screaming to their graves."
    "But 3 kids, an old man and a dog can only defeat so many crazed, highly trained killers."
    "It was all very dramatic and songs of your tragic, valiant ending start being sung in drinking halls throughout the Universe." 
    "Until Killsalot uses the transporter he took from your lifeless hands to brutally conquer the galaxy and burn those drinking halls to the ground."
    "You should have run away to fight another day. You have been defeated. Your adventure ends here."

    stop sound
    
    stop music fadeout 1.0 
#Jump to credits after credit scene is created#
   # jump credits


    return 
