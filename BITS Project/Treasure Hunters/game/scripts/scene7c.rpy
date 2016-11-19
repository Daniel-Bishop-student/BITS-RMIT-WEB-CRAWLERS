##Ending scenario 3##
label choice7:

    scene scene7c
    with fade

    $ renpy.music.set_volume(0.8, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 1.0 

    show harry mad
    show benji mad at right
    show penny mad at left
    show jax mad at Position(xpos =100)
    show slim mad
    show killsalot mad3 at Position(xpos=600)
    show soldiers
    show group 


    # Dialogue for ending scenario 3


    harry "There that thick scrub, run we’ll be able to hide in there!"

    group "All the kids and Slim run into the scrub."

    killsalot "Find them!"

    soldiers "Yes Master!"

    group "Kids huddled together behind a giant bolder." 

    benji "It’s no use Harry, they’ll find us eventually. Maybe if we turn ourselves in they’ll spare our lives?"

    slim "They spare no one."

    penny "Well if we’re going out, let’s go out fighting.  Who’s with me?"

    stop music fadeout 1.0

    scene scene7c1
    with fade

    play music "FX/scene7c_spaceship.mp3"

    show harry surprised
    show benji excited at right
    show penny happy at left
    show jax at Position(xpos =100)
    show slim proud 
    show xeena excited

    "Just then a ship floats overhead and shoots a beam down and scoops Harry and the kids up in it."

    #Aboard the ship
    
    slim "It’s ok! These people are the Amazon rebellion, an alliance formed from the few that survived the initial invasion"

    xeena "Welcome warriors! Any enemy of killsalot is a friend of ours. Rest up. We have a long journey ahead of us."

    penny "But where are we going? How many of you are there? Why..."

    show xeena proud

    xeena "All in good time my dear, all in good time..."

    stop music fadeout 1.0

    jump credits

    return 
