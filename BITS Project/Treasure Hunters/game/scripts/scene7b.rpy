label scene7b:
    
    scene scene7b1
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


    ###Ending Scenario 2
label choice6:

    penny "%(harry_name)s if we fight and die we dont help anybody, there will be another day and we will be ready.  Then Killsalot will get what he deserves."

    slim proud "%(penny_name)s is wise but our rebellion will not go unpunished."

    benji surprised "%(harry_name)s! He’s coming!"

    harry surprised "We should go..." 

    narrator "%(harry_name)s hits the phone button."

    group surprised "Your group uses the transporter to escape!"

    play sound "FX/transporter.mp3"

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

    killsalot surprised "They have escaped me, but I will make them suffer."

    killsalot "The villages nearby, their friends, their families ... Burn them all!"

    scene scene4
    with fade

    play music "FX/scene3FXwind.mp3" fadeout 2.0 fadein 1.0

    show harry mad at Position(xpos=0.5, ypos=0.95)
    show benji mad at Position(xpos=0.25, ypos=0.95)
    show penny sad at Position(xpos=0.70, ypos=0.95)
    show slim mad at Position(xpos=0.37, ypos=0.95)
    show jax mad at right

    slim "I have received word that Killsalot burned the village after we left.  There were only a few survivors."

    harry "What, why? They had nothing to do with it."
    
    penny mad "That bastard!"

    jax "Grr Grr"
    
    benji surprised "We’ve got to help them %(harry_name)s!"
    
    harry surprised "I know %(benji_name)s, and we will..."
    
    harry mad "I vow that we will rid this place of that vile creature Killsalot."
    
    benji mad "Yeah! Too right %(harry_name)s."

    show slim proud

    slim "And so it begins..."

    jump credits

    return