label scene7b:
    
    scene scene7b1
    with fade

    $ renpy.music.set_volume(0.8, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')
    
    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 1.0 

    show harry mad
    show benji mad at right
    show penny sad at left
    show jax mad at Position(xpos =100)
    show slim proud
    show killsalot mad2 at Position(xpos=600)
    show group surprised


    ###Ending Scenario 2
label choice6:

    penny "Harry if we fight and die we dont help anybody, there will be another day and we will be ready.  Then Killsalot will get what he deserves."

    slim "She is wise but our rebellion will not go unpunished."

    benji "Harry! He’s coming!"

    harry "We should go..." 

    "Harry hits the phone button."

    play sound "FX/transporter.mp3"

    group "Your group uses the transporter to escape!"

    killsalot  "They have escaped me, but I will make them suffer."

    killsalot "The villages nearby, their friends, their families ... Burn them all!"


#The next day: Other location on brenner 456
    show slim mad

    slim "I have received word that Killsalot burned the village after we left.  There were only a few survivors."

    harry "What, why? They had nothing to do with it."

    show penny mad
    
    penny "That bastard!"
    
    benji "We’ve got to help them Harry!"
    
    harry "I know and we will..."
    
    harry "I vow that we will rid this place of that vile creature Killsalot."
    
    benji "Yeah! Too right Harry."

    show slim proud

    slim "And so it begins..."

##Jump to credits####
   # jump credits
##The end of scenario 2
    return