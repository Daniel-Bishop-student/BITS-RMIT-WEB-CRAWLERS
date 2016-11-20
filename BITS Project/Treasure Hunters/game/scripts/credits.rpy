## Credits, attribution, and references

## Scrolling credit Code is not my original work and is sourced from
## https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=24079
label credits:

    $ credits_speed = 35 #scrolling speed in seconds
    scene black
    with dissolve
    show cred at Move((0.5, 6.5), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    hide thanks
    return

    init python:
        credits = ('BITS Assignment 3 - WEB CRAWLERS Team', 'Daniel Bishop, Joa, Dan A, James P'), ('Scene 1', 'https://www.vecteezy.com/vector-art/113932-free-living-room-vector-illustration \n Type: Free Stock Image'), ('Scene 2', 'http://www.bigstockphoto.com/image-114787442/stock-vector-vector-retro-classic-open-coffee-shop-exterior\nType: Stock Image','bought using free 7 day trial account'),('Scene 3','http://www.shutterstock.com/pic.mhtml?utm_medium=Affiliate&utm_source=120413&utm_campaign=VectorHQ.com&language=en&irgwc=1&id=110244560&tpl=120413-50655 \nType: Stock Image, bought using my personal account'),('Scene 4', 'https://www.dreamstime.com/stock-illustration-red-planet-mars-space-space-landscape-illustration-vector-format-image64618113\nType: Stock Image bought using my personal Account'),('Scene 5','https://imgur.com/gallery/R8oUo/comment/277448544\nType: Released Under Imgur License, See \"USE of IMGUR CONTENT\" https://imgur.com/tos \nYou may use UGC for anything that qualifies as fair use under copyright law, for example journalism (news, comment, criticism, etc.), but please include an attribute (\"Imgur\" or \"courtesy of Imgur\") next to where it is displayed. \nAlso see https://www.alrc.gov.au/publications/4-case-fair-use-australia/what-fair-use point 4.12'),('Scene 6-7a','https://www.dreamstime.com/stock-illustration-red-planet-mars-space-space-landscape-illustration-vector-format-image64618113\nType: Stock photo bought using my personal account'),('Scene 7a - derivative of scene 6\nScene 7\nMade using Adobe Illustrator'),('Scene 7b1','http://www.123rf.com/photo_10553791_camels-with-pyramids-in-wild-africa-landscape.html\nType: Stock Vector bought using personal account'),('Scene 7c', 'http://www.istockphoto.com/tr/vector/arizona-landscape-gm148122028-12301718?st=_p_mesa%20%20arizona\nType: Stock Vector bought using personal account'),('Characters','http://www.freepik.com/free-vector/pack-of-great-video-game-characters_947121.htm'),('Quick menu icon','http://www.iconarchive.com/show/small-n-flat-icons-by-paomedia/cog-icon.html'),('Soldier-image','http://www.freepik.com/free-vector/pack-of-great-video-game-characters_947121.htm'),('Spaceship Image','http://www.freepik.com/free-vector/variety-of-colorful-ufo_799060.htm'),('Scene1 fx reference:','http://www.flashkit.com/loops/Easy_Listening/Classical/Happy_Bi-Connie-10463/index.php'),('scene 3 fx reference','http://soundbible.com/1716-Mystic-Chanting-4.html'),('scene 7b fx reference','http://www.flashkit.com/soundfx/Transportation/Space/Beam_In-monty-9025/index.php'),('scene 7c fx reference','http://www.flashkit.com/soundfx/Transportation/Space/Engine_r-sequence-8632/index.php'),('scene 7 fx reference','http://www.flashkit.com/soundfx/Mayhem/Fighting/firing_g-Public_D-400/index.php'),('scene 6 fx reference','http://soundbible.com/2046-Incoming-Suspense.html'),('scene 2a fx reference','https://www.freesound.org/people/cognito%20perceptu/sounds/82827/'),('scene2 FX reference','http://www.flashkit.com/soundfx/Ambience/Restaurant/Restaura-J_Fairba-8430/index.php'),('scene3a FX reference','http://www.flashkit.com/soundfx/Ambience/Nature/Deep_For-ITE-8210/index.php'),('scene3, 5, 6, 7 FX reference','http://www.flashkit.com/soundfx/Nature/Wind/wind-Erin_Owe-8719/index.php')

        credits_s = "{size=80}Credits\n\n"
        c1 = ''
        for c in credits:
            if not c1==c[0]:
                credits_s += "\n{size=40}" + c[0] + "\n"
            credits_s += "{size=30}" + c[1] + "\n"
            c1=c[0]
        credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.99.11" #Don't forget to set this to your Ren'py version
    
    init:
#       image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
        image cred = Text(credits_s, text_align=0.5)
        image theend = Text("{size=80}The end", text_align=0.5)
        image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)




    return
##########end scrolling credit code####################





    return
##########end scrolling credit code####################


    
    
    
    



    