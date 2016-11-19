label scene3a:
    
    scene scene3a
    with fade

    $ renpy.music.set_volume(0.3, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene3aFXbirds.mp3" fadeout 2.0 fadein 1.0

    show harry excited at Position(xpos=0.5, ypos=0.95)
    show benji excited at Position(xpos=0.25, ypos=0.95)
    show penny happy at Position(xpos=0.70, ypos=0.95)
    show slim happy at Position(xpos=0.37, ypos=0.95)
    show jax at right
 
    # fade all characters in and make transperent?

    # Dialogue for scene3a

    slim "Brenner-456 used to be warm, bright and full of life. There was plenty of food, happiness and community spirit."

    slim "Kids ran free in the fields without worry and people worked together to build, teach and enjoy life."

    slim "The people would gather on the seventh day and pay tribute to the Ora."

    benji "What's the Ora?"

    slim "The Ora is the Great Mountain, it is the life source and in return for our loyalty the Ora provides us with Kia, a precious earth gem which holds great power."

    harry "What kind of power?"

    slim "Great powers of healing and growth. It fertilises our soil and purifies our water and regulates our seasons and much more."

    slim mad "One day a cloud descended upon Brenner. This cloud bore fire and the noise of thunder, only much louder."

    slim mad "Soldiers descended from the cloud as an endless waterfall. The soldiers ran through the Ora attacking the Protectors."

    penny "The Protectors?"

    slim "Those assigned the task of protecting the Ora and maintaining the rate of Kia extraction. The Ora is generous but too much Kia extraction forces an imbalance in our eco-system and makes soil acidic so nothing will grow."

    scene scene3
    with fade

    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 1.0

    show harry surprised at Position(xpos=0.5, ypos=0.95)
    show benji mad at Position(xpos=0.25, ypos=0.95)
    show penny sad at Position(xpos=0.70, ypos=0.95)
    show slim mad at Position(xpos=0.37, ypos=0.95)
    show jax mad at right

    slim "Our water turns to sludge and becomes infected with bacteria, the sky turns the color of blood as you see above you and the air a dusty, barely breathable haze."

    harry "How did this happen?"

    slim "After most of the protectors were killed, the soldiers started extracting the Kia from the mountain at a rate that could not be sustained."

    slim "The surviving Protectors are still fighting here in the Rebellion today"

    benji "Why did these soldiers want the Kia?"

    slim "(Sighs) The Kia is very powerful but when in the wrong hands can have its power used for terrible things."

    harry "Like What?"

    slim "To make high powered weapons, hyper drives and to unlease other untold horrors!"

    scene scene3a
    with fade

    play music "FX/scene3aFXbirds.mp3" fadeout 2.0 fadein 1.0

    show harry excited at Position(xpos=0.5, ypos=0.95)
    show benji excited at Position(xpos=0.25, ypos=0.95)
    show penny surprised at Position(xpos=0.70, ypos=0.95)
    show slim proud at Position(xpos=0.37, ypos=0.95)
    show jax at right

    harry "What’s all this got to do with me or us?"

    slim "Some of the village people, fearing the worst, asked witch doctors to open a portal. These portals had been opened before but no one was sure where they went or if they were even safe."

    slim "Facing almost certain death a lucky few managed to send their loved ones through the portal. Your great grandmother was one of those sent through the portal."

    slim "And it was written by the prophets that {i} '65 moon cycles from the day of the fire cloud he would return and right what was wronged.'{/i}"

    slim "Today marks exactly 65 moon cycles since the fire cloud... and here you are!"

    penny "I still don’t understand? Wait unless.....Harry your phone!?"

    harry "Yeah?"

    penny "It made a big flash right before we came to, and now all of a sudden we’re here in this place!"

    slim "May I see this.... Phone?"

    stop music fadeout 1.0

    jump scene5

    return 
