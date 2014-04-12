label inventory:
    $ objectes = len(items)
    n "Et trobes a la fase: [fase]"
    if objectes == 0:
        n "No tens res"
    else:
        if "galleda" in items:
            n "Tens una galleda"
        if "diari" in items:
            n "Tens un diari"
        if "poma" in items:
            n "Tens uma poma"
        if "cordill" in items:
            n "Tens una cordill"
        if "branca" in items:
            n "Tens una branca"
        if "clip" in items:
            n "Tens un clip"
        if "peix" in items:
            n "Tens un peix"
        if "llibre" in items:
            n "Tens un llibre"
        if "invitacio" in items:
            n "Tens una invitació"
return

label badge:
    play sound "magia.mp3"
    scene black
    show text "Has guanyat una medalla!" 
    with dissolve
    with Pause(1.0)
    hide text 
    with dissolve
    scene black 
    with Pause(0.5)
    if fase == 6:
        show aprenent at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 8:
        show ajudant at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 15:
        show assessor at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 18:
        show jugador at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 22:
        show professional at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 30:
        show expert at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 38:
        show mestre at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 43:
        show geni at truecenter 
        with dissolve 
        with Pause(3.0)
    elif fase == 50:
        show guru at truecenter 
        with dissolve 
        with Pause(3.0)
return