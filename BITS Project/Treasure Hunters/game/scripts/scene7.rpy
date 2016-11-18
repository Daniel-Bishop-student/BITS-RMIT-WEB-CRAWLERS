label scene7a:
    
    scene scene6-7a
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

    # Dialogue for scene7
    
    ######Scene 7a#######
    soldiers gang "Many soldiers rush to Harry, Slim and the gang..."
    benji excited "Harry your phone, it’s glowing again"
    jax bark "Woof Woof"
    all_characters surprised "A big flash and the gang including jax are now in battle suits with a special weapon each"
    penny mad "Let's get it on!"

    #####Battle Scene - kids fighting soldiers 7b? ###############
    all_characters surprised "{i}Near the end of the battle{/i}"
    benji confused "Harry there’s too many"
    slim mad "He’s right. You must retreat Harry. You must not let the transporter fall into Killsalot’s hands "
    penny sad "Use the transporter Harry! Get us out of here!"
    slim proud "No! Remember, the Rebellion is nearby. If we can find them, they may be able to help us."






    #######CHOICE SECTION#########
    choice_character choice "Make your choice"
    
    menu:
        "You don’t need any help, and only cowards run away. Stay and fight!":
            jump choice5

        "​Use transporter to escape":
            jump choice6

        "​Run and try to find the rebellion":
            jump choice7

label choice5:
    
    "Harry hears his friend’s words but all he sees is red. His is pumped up, he is angry and he wants blood. Something deep within him has awoken."


    "There is a lull in the fighting as Killsalots men regroup"


    harry mad "NO! Here is where we stand, here is where we fight back. If we run now, we will never stop running."


    slim "We must do what the Protector needs us to do. Stand together. Stand and fight!"


#####Cut scenes as each of the group get their own brief close up in a battle pose.######


    "Suddenly Benji get hit and goes down, swamped by Kilsalots men."


    harry "Benji!"
    slim "You can’t stop to help!"
    penny "But I have to!"


    "Penny goes to Benji’s aid but is cut down down before she can help"


    harry "NOOOOO!"
    slim "You must hold fast! We can help them when we have finished this fight"


    "It’s too much for Harry who calls Jax to his side and they both charge the enemy. Jax is killed and Harry runs out of ammo. Just before he his shot, Slim jumps in and takes the bullet."


    "harry (Incoherent scream of rage) RRRAAAAGGHHH"


    "Harry charges, Killsalots men with his bare hands."# Fade to black


##This text comes up over black screen: 


    "You fought bravely, you fought well, and many of Killsalots soldiers were sent screaming to their graves. But 3 kids, an old man and a dog can only defeat so many crazed, highly trained killers. You have been defeated. It was all very dramatic and songs of your tragic, valiant ending start being sung in drinking halls throughout the Universe … Until Killsalot uses the transporter he took from your lifeless hands to brutally conquer the galaxy and burn those drinking halls to the ground…. You should have run away to fight another day. Your adventure ends here."
#Jump to credits after credit scene is created#
   # jump credits


    
    
    

    return 
