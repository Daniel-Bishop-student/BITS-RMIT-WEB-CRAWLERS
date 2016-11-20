##Ending scenario 3##
label choice7:

    scene scene7c
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

    # Dialogue for ending scenario 3

    harry "There that thick scrub, run we’ll be able to hide in there!"

    group surprised "All the kids, and Slim, run into the scrub."

    show harry mad at Position(xpos=0.30, ypos=0.95)
    show benji mad at Position(xpos=0.25, ypos=0.95)
    show penny mad at Position(xpos=0.20, ypos=0.95)
    show jax mad at Position(xpos =0.35)
    show slim mad at Position(xpos=0.37, ypos=0.95)

    killsalot mad3 "Find them!"

    soldiers "Yes Master!"

    group "The gang huddles together behind a giant bolder." 

    benji surprised "It’s no use %(harry_name)s, they’ll find us eventually. Maybe if we turn ourselves in they’ll spare our lives?"

    slim "They spare no one."

    penny sad "Well if we’re going out, let’s go out fighting.  Who’s with me?"

    narrator "Just then a ship floats overhead and shoots a beam down and scoops %(harry_name)s and the kids up in it."

    hide harry
    with dissolve
    hide benji
    with dissolve
    hide penny
    with dissolve
    hide jax
    with dissolve
    hide slim
    with dissolve

    stop music fadeout 1.0

    scene scene7c1
    with fade

    play music "FX/scene7c_spaceship.mp3"

    show harry surprised at Position(xpos=0.5, ypos=0.95)
    with dissolve
    show benji excited at Position(xpos=0.25, ypos=0.95)
    with dissolve
    show penny happy at Position(xpos=0.65, ypos=0.95)
    with dissolve
    show jax at Position(xpos =0.75)
    with dissolve
    show slim proud at Position(xpos=0.37, ypos=0.95)
    with dissolve
    show xeena excited at Position(xpos=.90, ypos=0.95)
    with dissolve

    #Aboard the ship
    
    slim "It’s ok! These people are the Amazon rebellion, an alliance formed from the few that survived the initial invasion"

    xeena "Welcome warriors! Any enemy of Killsalot is a friend of ours. Rest up. We have a long journey ahead of us."

    jax "Woof, Woof!"

    penny surprised "But where are we going? How many of you are there? Why..."

    xeena proud "All in good time my dear, all in good time..."

    stop music fadeout 1.0

    jump credits

    return 
