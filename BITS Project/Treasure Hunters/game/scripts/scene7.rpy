label scene7a:
    
    scene scene6-7a
    with fade

    $ renpy.music.set_volume(0.6, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 1.0 

    show harry mad at Position(xpos=0.5, ypos=0.95)
    show benji mad at Position(xpos=0.25, ypos=0.95)
    show penny mad at Position(xpos=0.42, ypos=0.95)
    show jax mad at Position(xpos =0.30)
    show slim mad at Position(xpos=0.37, ypos=0.95)
    show killsalot mad2 at Position(xpos=0.90, ypos=0.95)
    show soldiers at Position(xpos=0.70)

    # Dialogue for scene7
    
    ######Scene 7a#######

    benji "%(harry_name)s your phone, it’s glowing again!"

    play sound "FX/transporter.mp3"

    group surprised "A big flash and the gang, including Jax, are now in battle suits bristling with special weapons!"

    jax "Grr, Grr!"

    killsalot "Attack them!!"

    soldiers "Many soldiers rush to %(harry_name)s, Slim and the gang."

    play sound "FX/scene7_shooting.mp3" loop

    penny "LET'S GET IT ON!"

    #####Battle Scene - kids fighting soldiers 7b? ###############
    group surprised "You and your group fight a desparate battle....."

    benji "%(harry_name)s there’s too many!"
    slim "%(benji_name)s is right! You must retreat %(harry_name)s. You must not let the transporter fall into Killsalot’s hands."
    penny "Use the transporter %(harry_name)s! Get us out of here!"
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
    
    "%(harry_name)s hears his friend’s words but all he sees is red. His is pumped up, he is angry and he wants blood. Something deep within him has awoken."


    "There is a lull in the fighting as Killsalots men regroup..."


    harry "NO! Here is where we stand, here is where we fight back. If we run now, we will never stop running."


    slim "We must do what the Protector needs us to do. Stand together. Stand and fight!"


#####Cut scenes as each of the group get their own brief close up in a battle pose.######


    "Suddenly %(benji_name)s get hit and goes down, swamped by Kilsalots soldiers."

    hide benji
    with dissolve

    harry "%(benji_name)s!"
    slim "You can’t stop to help!"

    show penny sad 
    penny "But I have to!"


    "%(penny_name)s goes to %(benji_name)s’s aid but is cut down down before she can help..."

    hide penny
    with dissolve

    harry "NOOOOO!"
    slim "You must hold fast! We can help them when we have finished this fight!"


    "It’s too much for %(harry_name)s who calls Jax to his side and they both charge the enemy."

    jax "GRRRR!!"

    "Jax is killed and %(harry_name)s runs out of ammunition."

    hide jax
    with dissolve

    "Just before %(harry_name)s is shot by Killsalot's soldiers, Slim jumps in and takes the bullet."

    hide slim
    with dissolve

    harry "RRRAAAAGGHHH"

    stop sound

    play sound "FX/scene7_battle.mp3" noloop

    "%(harry_name)s charges, Killsalots men with his bare hands."

    $ renpy.music.set_volume(0.7, 0, channel='sound')

    play sound "FX/choice1part1.mp3"

    "You fought bravely, you fought well, and many of Killsalots soldiers were sent screaming to their graves."

    play sound "FX/choice1part2.mp3"
    
    "But 3 kids, an old man and a dog can only defeat so many crazed, highly trained killers."
    
    hide harry
    with dissolve

    play sound "FX/choice1part3.mp3"

    "It was all very dramatic and songs of your tragic, valiant ending start being sung in drinking halls throughout the Universe." 

    play sound "FX/choice1part4.mp3"
   
    "Until Killsalot uses the transporter he took from your lifeless hands to brutally conquer the galaxy and burn those drinking halls to the ground."

    play sound "FX/choice1part5.mp3"
    
    "You should have run away to fight another day. You have been defeated. Your adventure ends here."

    stop sound
    
    stop music fadeout 1.0 
    
    jump credits

    return 
