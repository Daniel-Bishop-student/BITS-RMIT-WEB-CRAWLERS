# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    imagemap:
        ground "images/menu/mm_ground.png"
        idle "images/menu/mm_idle.png"
        hover "images/menu/mm_hover.png"
        
        alpha False
        # This is so that everything transparent is invisible to the cursor. 
       
        hotspot (993, 126, 236, 105) action Start()
        hotspot (1032, 263, 197, 99) action ShowMenu("load")
        hotspot (970, 397, 254, 97) action ShowMenu("preferences")
        hotspot (703, 296, 79, 36) action Help()
        hotspot (1013, 528, 210, 107) action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation

    imagemap:
        ground "images/menu/save_ground.png"
        idle "images/menu/save_idle.png"
        hover "images/menu/save_hover.png"
        selected_idle "images/menu/save_selected_idle"
        selected_hover "images/menu/save_selected_hover"
        
        alpha False
        cache False
     
        hotspot (53, 100, 754, 157) clicked FilePage(1) activate_sound "sounds/click.mp3" hover_sound "sounds/hover.mp3"
        hotspot (52, 286, 755, 158) clicked FilePage(2) activate_sound "sounds/click.mp3" hover_sound "sounds/hover.mp3"
        hotspot (52, 469, 753, 158) clicked FilePage(3) activate_sound "sounds/click.mp3" hover_sound "sounds/hover.mp3"
        
        hotspot (53, 100, 754, 157) clicked FileSave(1):
            use load_save_slot(number=1)
        hotspot (52, 286, 755, 158) clicked FileSave(2):
            use load_save_slot(number=2)
        hotspot (52, 469, 753, 158) clicked FileSave(3):
            use load_save_slot(number=3)

        hotspot (926, 430, 158, 161) action Return()



screen load():

    tag menu

    use navigation

    imagemap:
        ground "images/menu/load_ground.png"
        idle "images/menu/load_idle.png"
        hover "images/menu/load_hover.png"
        selected_idle "images/menu/load_selected_idle"
        selected_hover "images/menu/load_selected_hover"
        
        alpha False
        cache False
        
        hotspot (53, 100, 754, 157) clicked FilePage(1) activate_sound "sounds/click.mp3" hover_sound "sounds/hover.mp3"
        hotspot (52, 286, 755, 158) clicked FilePage(2) activate_sound "sounds/click.mp3" hover_sound "sounds/hover.mp3"
        hotspot (52, 469, 753, 158) clicked FilePage(3) activate_sound "sounds/click.mp3" hover_sound "sounds/hover.mp3"
        
        hotspot (53, 100, 754, 157) clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (52, 286, 755, 158) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (52, 469, 753, 158) clicked FileLoad(3):
            use load_save_slot(number=3)
       
        hotspot (926, 430, 158, 161) action Return() activate_sound "sounds/click.mp3" hover_sound "sounds/hover.mp3"

screen load_save_slot:
    
    $ slot_str = FileSlotName(number, 12)
    $ time_str = FileTime(number, empty=("Slot Available"))

    add FileScreenshot(number) xpos 550 ypos 15

    text slot_str xcenter 100 ycenter 50 size 60 color "#ffffff" outlines [ (3,"#000000") ]    
    text time_str xcenter 110 ycenter 120 size 24 color "#ffffff" outlines [ (2,"#000000") ]
    
    key "save_delete" action FileDelete(number)
    
init -2 python:
    
    config.thumbnail_width = 183
    config.thumbnail_height = 133

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu


    # Include the navigation.
    use navigation
    
    imagemap:
        ground "images/menu/config_ground.png"
        idle "images/menu/config_idle.png"
        hover "images/menu/config_hover.png"
        selected_idle "images/menu/config_selected_idle.png" 
        selected_hover "images/menu/config_selected_hover.png" 
        alpha True
        
        hotspot (1099, 139, 159, 159) action ShowMenu("load")
        hotspot (928, 89, 152, 150) action ShowMenu("save")
        hotspot (1099, 487, 159, 155) action Quit()
        hotspot (1090, 311, 184, 161) action MainMenu()
        hotspot (926, 430, 158, 161) action Return()
        hotspot (78, 442, 303, 224) action Preference("display", "fullscreen")
        hotspot (472, 440, 306, 226) action Preference("display", "window")
        
        bar pos (113, 136) value Preference("text speed") style "pref_slider"
        bar pos (112, 246) value Preference("sound volume") style "pref_slider"
        bar pos (112, 358) value Preference("music volume") style "pref_slider"

init -2 python:
    style.pref_slider.left_bar = "images/menu/left-bar.png"
    style.pref_slider.right_bar = "images/menu/right-bar.png"

    style.pref_slider.xmaximum = 635
    style.pref_slider.ymaximum = 31

    style.pref_slider.thumb = "images/menu/thumb.png"
    style.pref_slider.thumb_offset = 5
    style.pref_slider.thumb_shadow = None


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    imagemap:
        ground 'images/menu/menu_idle.png'
        idle 'images/menu/menu_idle.png' 
        hover 'images/menu/menu_hover.png'
        
        alpha False
        
        hotspot (1109, 681, 48, 29) action ShowMenu("save")
        hotspot (1072, 681, 30, 29) action ShowMenu("preferences")
        hotspot (1164, 682, 50, 29) action ShowMenu("load")
        hotspot (1221, 681, 50, 29) action Return()
    # hbox:
    #     style_group "quick"

    #     xalign 1.0
    #     yalign 1.0

    #     textbutton _("Prefs") action ShowMenu('preferences')
    #     textbutton _("Save") action ShowMenu('save')
    #     textbutton _("Q.Load") action ShowMenu("load")
    #     textbutton _("Skip") action Skip()
        

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
insensitive_color "#4448"

