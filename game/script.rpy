# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# imatges de nit
image bg boira08 = "IMG_0593.JPG"
image bg boira11 = "imatge04.JPG"
image bg boira04 = "IMG_0589.JPG"
image bg boira02 = "IMG_0585.JPG"
image bg boira05 = "IMG_0590.JPG"
image bg boira12 = "IMG_0598.JPG"
image bg boira01 = "imatge14b.png"
image bg boira09 = "IMG_0594.JPG"
image bg boira10 = "IMG_0588.JPG"
image bg boira03 = "IMG_0587.JPG"
image bg boira13 = "IMG_0595.JPG"
image bg boira07 = "IMG_0592.JPG"
image bg boira06 = "IMG_0596.JPG"
image bg boira14 = "casa_metge.JPG"
image bg boira15 = "placa_nit.jpg"
image bg boira16 = "monte_nit.JPG"
image bg boira19 = "carrern.JPG"
# imatges de dia
image bg escena01 = "imatge14.jpg"
image bg escena02 = "imatge01.jpg"
image bg escena03 = "imatge17.jpg"
image bg escena04 = "imatge06.jpg"
image bg escena05 = "imatge07.jpg"
image bg escena06 = "imatge13.jpg"
image bg escena07 = "imatge08.jpg"
image bg escena08 = "imatge10.jpg"
image bg escena09 = "imatge11.jpg"
image bg escena10 = "imatge05.jpg"
image bg escena11 = "imatge04_dia.JPG"
image bg escena12 = "templo.jpg"
image bg escena13 = "imatge12.jpg"
image bg escena14 = "imatge16.jpg"
image bg escena15 = "placa.jpg"
image bg escena16 = "monte_dia.JPG"
image bg escena17 = "bosc2.JPG"
image bg escena18 = "masia2.jpg"
image bg escena19 = "carrerd.JPG"
image bg escena20 = "bosc.JPG"
image bg escena21 = "fabrica.png"
# imatges interiors
image bg metge = "biblioteca.png"
image bg palau = "despatx.png"

image eileen normal ="eileen_happy.png"
image llave = "llave.png"
image alicia normal = "noia.png"
image tieta normal = "tieta.png"
image metge normal = "metge.png"
image desconegut normal = "desconegut.png"
image fontana= "font.JPG"
image sant = "stmiquel_detall.JPG"
image inscripcio = "palau_detall.JPG"
image pila = "pila_baptismal.JPG"
image bateig = "bateig.png"
image laura normal = "laura1.png"
image vigilant normal ="vigilant2.png"
image vigilant adormit ="vigilant1.png"
image foraster normal = "desconegut2.png"
image fruitera normal = "fruitera.png"
image secretaria normal = "secretaria.png"
image taula = "taula.jpeg"
image nen = "nen.png"
image valla = "valla.png"
image peix = "fish.png"
image joan petit = "joan_petit.png"

# Declare characters used by this game.
define j = Character('Jugador', color="#c3c3c3")
define n = Character('Neus', color="#c8ffc8", window_left_padding=160, show_side_image=Image("eileen_side.png", xalign=0.0, yalign=1.0))
define a = Character("Noia", color="#ffc8c8", window_left_padding=160, show_side_image=Image("noia_side.png", xalign=0.0, yalign=1.0))
define t = Character("Tieta", color="#c8c8ff", window_left_padding=160, show_side_image=Image("tieta_side.png", xalign=0.0, yalign=1.0))
define m = Character("Metge", color="#c8c8c8", window_left_padding=160, show_side_image=Image("metge_side.png", xalign=0.0, yalign=1.0))
define d = Character("Desconegut", color="#c8ffc8", window_left_padding=160, show_side_image=Image("desconegut_side.png", xalign=0.0, yalign=1.0))
define f = Character("Foraster", color="#c8ffc8", window_left_padding=160, show_side_image=Image("desconegut2_side.png", xalign=0.0, yalign=1.0))
define l = Character("Laura", color="#c8ffc8", window_left_padding=160, show_side_image=Image("noia_side.png", xalign=0.0, yalign=1.0))
define v = Character("Vigilant", color="#c8c8c8", window_left_padding=160, show_side_image=Image("vigilant_side.png", xalign=0.0, yalign=1.0))
define s = Character("Fruitera", color="#c8c8c8", window_left_padding=160, show_side_image=Image("fruitera_side.png", xalign=0.0, yalign=1.0))
define e = Character("Nen", color="#c8c8c8", window_left_padding=160, show_side_image=Image("nen_side.png", xalign=0.0, yalign=1.0))
define x = Character("Secretaria", color="#c8c8c8", window_left_padding=160, show_side_image=Image("secretaria_side.png", xalign=0.0, yalign=1.0))

# The game starts here.
label start:
    $ fase = 1
    $ dia = False
    $ items = []
    scene bg boira11
    with fade
    show eileen normal
    
    n "A les sis de la matinada del 20 de gener de 1864, el termòmetre marca sis graus i hi ha boira,"
    n "sembla que a Víc tothom dorm, però en realitat no és així. Narcisa i Josep necessiten del teu ajut."
    n "Troba la seva casa al Carrer Sant Hipòlit i esbrina que està pasant..."
    $ est = True
    
    hide eileen
    play music "Ghost.ogg"
    
    $ n_allowed = True
    $ s_allowed = True
    $ e_allowed = False
    $ o_allowed = False
    $ t_allowed = False
    $ porta_allowed = False
    $ veure_allowed = True
    $ agafar_allowed = True
    $ parlar_allowed = True
    $ inventari_allowed = True
    $ galleda_allowed = False
    $ diari_allowed = False
    $ branca_allowed = False
    $ galleda = False
    $ branca = False

    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena04
    elif destino == "s":
        jump escena08
    elif destino =="v":
        jump escena11
    elif destino =="i":
        $ showpunts = True;
    

# Palau episcopal.================================================================

label escena04:

    if dia:
        scene bg escena04
        with dissolve
    else:
        scene bg boira04
        with fade
    
    $ n_allowed = True
    $ s_allowed = True
    $ e_allowed = False
    $ o_allowed = True
    $ porta_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        $ porta_allowed = False
        jump escena02
    elif destino == "s":
        $ porta_allowed = False
        jump escena11
    elif destino == "o":
        $ porta_allowed = False
        jump escena19
    elif destino == "v":
        n "Estem al costat d'una plaça"
        n "Hi ha un edifici amb una inscripció"
        $ renpy.pause(0)
        scene black 
        with Pause(0.5)
        show inscripcio at truecenter
        with dissolve
        with Pause(2.0)
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    elif destino == "t":
        $ porta_allowed = False
        jump escena22

    jump escena04

# Catedral del Víc.================================================================

label escena02:

    if dia:
        scene bg escena02
        with dissolve
    else:
        play sound "campanes.mp3"
        scene bg boira02
        with fade
        
    if fase == 6:
        show tieta normal at right
        t "Hola, tenim un problema, Joan, el marit de la Narcisa"
        t "vol posar al nen, com a tercer nom, el Sant del dia..."
        t "però no sabem quin és...."
        $ fase = 7
    if fase == 7:
        show tieta normal

    $ n_allowed = True
    $ s_allowed = True
    $ e_allowed = True
    $ o_allowed = False
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena05
    elif destino == "s":
        jump escena04
    elif destino == "e":
        jump escena13
    elif destino == "v":
        n "Hi ha una església molt gran"
        n "dins hi ha una pila baptismal"
        $ renpy.pause(0)
        scene black 
        with Pause(0.5)
        show pila at truecenter
        with dissolve
        with Pause(2.0)
    elif destino == "p":
        n "No hi ha res a dir"
    elif destino == "a":
        if fase == 7:
            if "diari" in items:
                "Mira, el diari d'avui"
                t "Diu que avui és Sant Sebástià! "
                t "gràcies!!"
                t "Anem a batejar a {p=1.0} Joan Lluís Sebastià Collell Cuatrecasas!"
                play sound "campanes.mp3"
                $ fase = 8
                scene black 
                with Pause(0.5)
                show bateig at truecenter
                with dissolve
                with Pause(2.0)
                jump escena11
            else:
                t "Prova de trobar un diari..."
        else:        
            "de moment no hi ha res que poguem fer aquí..."
    elif destino == "i":
        call inventory

    jump escena02

# Temple romà. ======================================================================

label escena12:

    if dia:
        scene bg escena12
        with dissolve
        show valla
    else:
        scene bg boira12
        with fade
        
    if fase == 12:
        show nen behind valla 
        
    $ n_allowed = True
    $ s_allowed = False
    $ e_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena07
    elif destino == "e":
        jump escena06
    elif destino == "o":
        jump escena13
    elif destino == "v":
        n "Això sembla un temple romà"
    elif destino == "p":
        if fase == 12:
            e "Hola"
            e "Estic super avorrit, estaba jugant a fer volar un estel"
            e "i s'ha trencat el cordill"
            menu:
                "Em pots donar el cordill que et queda?":
                    e "D'acord"
                    play sound "magia.mp3"
                    "Ja tinc un cordil"
                    "Gràcies!!"
                    $ fase = 13
                    $ items.append("cordill")
                    e "de res, adèu"
                    show nen at left with move
                    hide nen
                "No res":
                    jump escena12
        else:  
            n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory

    jump escena12

# Rierol =============================================================================

label escena11:

    if dia:
        scene bg escena11
        with dissolve
    else:
        scene bg boira11
        with fade

    $ n_allowed = True
    $ s_allowed = True
    $ e_allowed = False
    $ o_allowed = False
    
    if fase == 8:
        show eileen normal
        n "Han pasat 8 anys i avui és un dia molt important per la vida d'en Joan Collell"
        n "ves a casa seva i descobreix perquè"
        hide eileen
        $ fase = 9
        
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena04
    elif destino == "s":
        jump escena08
    elif destino == "v":
        n "En aquest rierol hem començat la nostra aventura..."
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        if "branca" in items and "cordill" in items and "clip" in items and "poma" in items:
            "Amb el clip fas un ham..."
            "li lligues el cordill..."
            "lligues el cordill a la branca..."
            "poses una mica de poma en el clip..."
            "Ep! ja tens una canya de pescar!"
            "Anem a pescar una mica..."
            play sound "magia.mp3"
            "Ja tinc un Peix!"
            $ renpy.pause(0)
            scene black 
            with Pause(0.5)
            show peix at truecenter
            with dissolve
            with Pause(2.0)
            $ items.append("peix")
        else:
            n "De moment no hi ha res a fer aquí"
    elif destino == "i":
        call inventory

    jump escena11

# Segona residència =====================================================================

label escena08:

    if dia:
        scene bg escena08
        with dissolve
    else:
        scene bg boira08
        with fade
        
    play sound "gos.mp3"
    
    $ n_allowed = True
    $ s_allowed = True
    $ e_allowed = False
    $ o_allowed = False
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena11
    elif destino == "s":
        jump escena17
    elif destino == "v":
        n "Estem sortint de la localitat..."
    elif destino == "p":
        n "Sembla que el gos no vol parlar..."
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory

    jump escena08


# Església de la Pietat ================================================================

label escena13:

    if dia:
        scene bg escena13
        with dissolve
        if "diari" in items:
            $ diari_allowed = False
        else:
            $ diari_allowed = True
    else:
        scene bg boira13
        with fade
        
    $ n_allowed = True
    $ s_allowed = False
    $ e_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        $ diari_allowed = False
        jump escena14
    elif destino == "e":
        $ diari_allowed = False
        jump escena12
    elif destino == "o":
        $ diari_allowed = False
        jump escena02
    elif destino == "v":
        n "Hi ha una església"
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "d":
        play sound "magia.mp3"
        n "Tens un diari d'avui"
        $ items.append("diari")
    elif destino == "i":
        call inventory
    jump escena13

# Primera casa de la Congregació =======================================================

label escena07:

    if dia:
        scene bg escena07
        with dissolve
    else:
        scene bg boira07
        with fade
    
    $ n_allowed = False
    $ s_allowed = True
    $ e_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "o":
        jump escena14
    elif destino == "s":
        jump escena12
    elif destino == "e":
        jump escena20
    elif destino == "v":
        n "Un carrer com tants altres"
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena07

# Plaça del pes ====================================================================

label escena05:

    if dia:
        scene bg escena05
        with dissolve
    else:
        scene bg boira05
        with fade
    
    if fase== 10:
        show alicia normal at left
        a "Pobre de mi..."
    
    $ n_allowed = False
    $ s_allowed = True
    $ e_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "e":
        jump escena14
    elif destino == "o":
        jump escena09
    elif destino == "s":
        jump escena02
    elif destino == "a":
        if fase == 4: 
            if galleda:
                play sound "magia.mp3"
                "Omples la galleda amb aigua de la font"
                $ fase = 5
            else:
                "Aquí tens aigua però no tens on ficar-la"
            jump escena05
    elif destino == "v":
        n "Hi ha una plaça amb una font"
        $ renpy.pause(0)
        scene black 
        with Pause(0.5)
        show fontana at truecenter
        with dissolve
        with Pause(2.0)
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "i":
        call inventory
    jump escena05
    
# Tercera Casa de la Congregació =============================================================

label escena09:

    if dia:
        scene bg escena09
        with dissolve
    else:
        scene bg boira09
        with fade
    
    $ n_allowed = False
    $ s_allowed = True
    $ e_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "s":
        jump escena01
    elif destino == "e":
        jump escena05
    elif destino == "o":
        jump escena15
    elif destino == "v":
        n "Hi ha una casa amb la imatge d'un Sant i una inscripció"
        $ renpy.pause(0)
        scene black 
        with Pause(0.5)
        show sant at truecenter
        with dissolve
        with Pause(2.0)
        jump escena09
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena09

# Plaça de Vic ============================================================================

label escena15:

    if dia:
        scene bg escena15
        with dissolve
    else:
        scene bg boira15
        with fade
    
    if fase == 10:
        show fruitera normal at left
        show taula
        s "Fruita!"
        s "Es ven fruita!!!"
    
    if fase > 10 and not "poma" in items:
        show fruitera normal at left
        show taula
    
    $ n_allowed = False
    $ s_allowed = True
    $ e_allowed = True
    $ o_allowed = False
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "s":
        jump escena10
    elif destino == "e":
        jump escena09
    elif destino == "v":
        n "Una plaça molt gran"
    elif destino == "p":
        if fase == 10:
            menu:
                "Què saps on puc comprar un llibre d'aritmètica?":
                    s "Com vens tant tard,ja només quedo jo al mercat"
                    s "hi ha un libreter ambulant que acaba de passar per Vic i que ha marxat cap a Barcelona..."
                    s "Potser si corres encara el pots trobar en el camí del sud"
                    s "Jo estic tancant la paradeta que és hora de dinar"
                    $ fase = 11
                    jump escena15
                "Quina fruita més maca":
                    s "Sí, l'he collit aquest matí a nostre hort"
                    s "Vols comprar quelcom?"
                    "No, no tinc diners gràcies"
                    s "I com penses pagar el llibre?"
                    "No ho se, ja pensarè quelcom..."
                    s "Té, agafa aquesta poma, està una mica tocada i no la puc vendre…"
                    play sound "magia.mp3"
                    $ items.append("poma")
                    "Tinc una poma!"
                    "Moltes gràcies"
                    s "De res, que tinguis un bon dia!"
                    jump escena15
                "Marxo, bon dia...":
                    s "Bon dia"
        elif fase > 10 and not "poma" in items:
            menu:
                "Quina fruita més maca":
                    s "Sí, l'he collit aquest matí a nostre hort"
                    s "Vols comprar quelcom?"
                    "No, no tinc diners gràcies"
                    s "I com penses pagar el llibre?"
                    "No ho se, ja pensarè quelcom..."
                    s "Té, agafa aquesta poma, està una mica tocada i no la puc vendre…"
                    play sound "magia.mp3"
                    $ items.append("poma")
                    "Tinc una poma!"
                    "Moltes gràcies"
                    s "De res, que tinguis un bon dia!"
                    jump escena15
                "Marxo, bon dia...":
                    s "Bon dia"
        else:
            n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena15


# Casa on va néixer Joan Collell ============================================================

label escena01:

    if dia:
        scene bg escena01
        with dissolve
    else:
        scene bg boira01
        with fade
    
    if fase == 1:
        $ fase = 2
        show tieta normal
        t "Uff, per fi veig a algú!"
        t "Ens hauríes d'ajudar, la meva germana Narcisa està de part i ens caldria un metge"
        t "afanyat que és urgent!"
        hide tieta
    elif fase == 5:
        $ fase = 6
        show tieta normal
        t "gràcies per portar aigua!"
        $ renpy.pause(0)
        scene black
        show text "...uns minuts més tard..." 
        with dissolve
        with Pause(1.0)
        hide text 
        with dissolve
        play sound "porta.mp3"
        scene bg boira01
        with fade
        show metge normal at right
        show tieta normal 
        m "Ha tingut un nen!!"
        t "t'esperem demà al bateig a la catedral!"
        t "fins demà..."
        hide tieta
        hide metge
        scene black
        show text "...al dia següent..." 
        with dissolve
        with Pause(1.0)
        hide text 
        with dissolve
        play sound "gallo.mp3"
        $ dia = True
        jump escena01
    elif fase == 9:
        show tieta normal
        t "Hola, ets tu!, quant de temps..."
        t "Mira, avui Joan comença les classes al Seminari, i ens falta el llibre d'aritmètica"
        t "ja sé que sempre t'estic demanant coses, però... ens podries ajudar?"
        $ fase = 10
        hide tieta
        
    elif fase == 14:
        show tieta normal
        t "Hola..."
        t "Veig que has portat el llibre..."
        t "Moltes gràcies"
        show joan petit with dissolve
        
        $ fase = 15
        hide tieta
        
    $ n_allowed = True
    $ s_allowed = True
    $ e_allowed = False
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena09
    elif destino == "s":
        jump escena19
    elif destino == "o":
        jump escena10
    elif destino == "v":
        n "Aquesta casa em sona molt..."
    elif destino == "p":
        n "Ara, no hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena01

# Carrer de Sant Just (Seminari) ============================================================

label escena10:

    if dia:
        scene bg escena10
        with dissolve
    else:
        scene bg boira10
        with fade
        
    play sound "zumbido.mp3"
    
    $ n_allowed = True
    $ s_allowed = False
    $ e_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "o":
        jump escena03
    elif destino == "n":
        jump escena15
    elif destino == "e":
        jump escena01
    elif destino == "v":
        n "Un carrer estret..."
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena10

# Capella del Seminari =============================================================================================
        
label escena03:

    if dia:
        scene bg escena03
        with dissolve
    else:
        scene bg boira03
        with fade    
    
    if fase == 2:
            show desconegut normal at left
        
    $ n_allowed = False
    $ s_allowed = False
    $ e_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "e":
        jump escena10
    elif destino == "o":
        jump escena16
    elif destino == "v":
        n "Hi ha una capella"
    elif destino == "p":
        if fase == 2:
            d "Hola, on aneu a aquestes hores pel carrer?"
            menu:
                "Passetjant una mica...":
                    d "No són hores per passetjar, crec jo..."
                    jump escena03
                "Estic cercant un metge, és urgent...":
                    d "El metge viu a l'altra punta de Vic, al final del carrer Nou, al nord de la església de la Pietat"
                    d "Piqueu tres cops a la porta per tal que us obrin."
                    $ fase = 3
                    jump escena03
                "Marxo, bona nit...":
                    d "Bona nit"
        else:
            n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena03

# Casa on va morir ============================================================================

label escena06:

    if dia:
        scene bg escena06
        with dissolve
    else:
        scene bg boira06
        with fade
    play sound "ambiente.mp3"
    
    $ n_allowed = True
    $ s_allowed = False
    $ e_allowed = False
    $ o_allowed = True
    
    if galleda:
        $ galleda_allowed = False
    else:
        $ galleda_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "o":
        $ galleda_allowed = False
        jump escena12
    elif destino == "n":
        $ galleda_allowed = False
        jump escena20
    elif destino == "g":
        play sound "magia.mp3"
        $ galleda = True
        $ items.append("galleda")
        "Tinc una galleda!"
    elif destino == "v":
        n "Hi ha una casa amb un balcó..."
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "Si hi ha un objecte que t'interesa, fes clic sobre ell"
    elif destino == "i":
        call inventory
    jump escena06   

# Casa del metge ====================================================================

label escena14:

    if dia:
        scene bg escena14
        with dissolve
    else:
        scene bg boira14
        with fade
    
    $ n_allowed = False
    $ s_allowed = True
    $ e_allowed = True
    $ o_allowed = True
    $ porta_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "o":
        $ porta_allowed = False
        jump escena05
    elif destino == "s":
        $ porta_allowed = False
        jump escena13
    elif destino == "e":
        $ porta_allowed = False
        jump escena07
    elif destino == 't':
        play sound "cierre_1.mp3"
        pause 1.5
        play sound "cierre_1.mp3"
        pause 1.5
        play sound "cierre_1.mp3"
        pause 1.5
        if fase == 3:
            play sound "porta.mp3"
            scene black
            show text "...uns minuts més tard..." 
            with dissolve
            with Pause(2.0)
            hide text 
            with dissolve
            scene bg metge with fade
            show metge normal at right
            m "Què vols?"
            menu:
                "Ha de venir amb mi la senyora Narcisa està de part!":
                    $ fase = 4
                    m "d'acord, agafo unes coses i vaig cap allà!"
                    m "tu ves a aconseguir aigua!"
                    m "gràcies!!!"
                    jump escena14
                "No res...":
                    jump escena14
        else:
            n "No contesta ningú"
    elif destino == 'a':
        play sound "cierre_1.mp3"
        pause 1.5
        play sound "cierre_1.mp3"
        pause 1.5
        play sound "cierre_1.mp3"
        pause 1.5
    elif destino == "v":
        if fase == 3:
            n "Aquesta deu ser la casa que m'ha dit el desconegut"
        else:
            n "Un carrer ample..."
    elif destino == "p":
        n "No hi ha ningú amb qui parlar, prova de picar la porta"
    elif destino == "i":
        call inventory
        
    jump escena14
        
# Muntanya ============================================================

label escena16:

    if dia:
        scene bg escena16
        with dissolve
    else:
        scene bg boira16
        with fade
        
    play sound "zumbido.mp3"
    
    $ n_allowed = False
    $ s_allowed = False
    $ e_allowed = True
    $ o_allowed = False
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "e":
        jump escena03
    elif destino == "v":
        n "La muntanya..."
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena16
    
# Bosc 1 ============================================================

label escena17:

    if dia:
        scene bg escena17
        with dissolve
        $ e_allowed = True
    else:
        scene black
        with fade
        $ e_allowed = False
        
    play sound "zumbido.mp3"
    
    if fase > 10 and fase < 14:
        show foraster normal
    
    $ n_allowed = True
    $ s_allowed = False
    $ o_allowed = False
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena08
    elif destino == "e":
        jump escena18
    elif destino == "v":
        n "No es veu res"
    elif destino == "p":
        if fase == 11:
            f "Bon dia"
            menu:
                "Bon dia!":
                    jump escena17
                "Necessito un llibre d'aritmètica!":
                    $ fase = 12
                    f "Tens sort, tinc un que et pot servir"
                    f "si el vols el puc canviar per qualsevol cosa per menjar"
                    f "tinc gana"
                    f "saps què? em ve de gust peix..."
                    f "et canvío el libre per un peix"
                    f "torna quan tinguis un peix"
                    jump escena17
                "No res...":
                    jump escena17
        elif fase > 11 and fase < 14:
            if "peix" in items:
                f "Quin peix mes maco, ara el faré a la brassa"
                f "aquí tens el llibre que et vaig prometre..."
                play sound "magia.mp3"
                $ items.remove("peix")
                $ items.append("llibre")
                "Tinc el llibre d'aritmètica!"
                "Moltes gràcies"
                $ fase = 14
            else:
                f "Si no em portes un peix no hi ha tracte!"
                jump escena17
        else:
            n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena17
    
# Masia ============================================================

label escena18:

    
    scene bg escena18
    with dissolve
    show laura normal
    
    $ e_allowed = False
    $ n_allowed = False
    $ s_allowed = False
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "o":
        jump escena17
    elif destino == "v":
        n "Hi ha una masia"
    elif destino == "p":
        l "Hola"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena18
    
# Enllaç ============================================================

label escena19:

    if dia:
        scene bg escena19
        with dissolve
    else:
        scene bg boira19
        with fade
    
    $ n_allowed = True
    $ s_allowed = False
    $ e_allowed = True
    $ o_allowed = False
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "n":
        jump escena01
    elif destino == "e":
        jump escena04
    elif destino == "v":
        n "Aquest carrer fa pujada"
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory

    jump escena19
    
# Bosc 2 ============================================================

label escena20:

    if dia:
        scene bg escena20
        with dissolve
        $ e_allowed = True
        if branca:
            $ branca_allowed = False
        else:
            $ branca_allowed = True
    else:
        scene black
        with fade
        $ e_allowed = False
        play sound "zumbido.mp3"
        n "Per aquí no podem seguir, no es veu res"
        
    play sound "zumbido.mp3"
    
    $ n_allowed = False
    $ s_allowed = True
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "s":
        $ branca_allowed = False
        jump escena06
    elif destino == "e":
        $ branca_allowed = False
        jump escena21
    elif destino == "o":
        $ branca_allowed = False
        jump escena07
    elif destino == "v":
        n "No es veu res"
    elif destino == "p":
        n "No hi ha ningú amb qui parlar"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    elif destino == "b":
        play sound "magia.mp3"
        $ branca = True
        $ items.append("branca")
        "Tinc una branca!"
    jump escena20
    
# Fabrica ============================================================

label escena21:

    
    scene bg escena21
    with dissolve
    show vigilant normal
    
    $ e_allowed = False
    $ n_allowed = False
    $ s_allowed = False
    $ o_allowed = True
    
    call screen buttons
    
    $ destino = _return
    
    if destino == "o":
        jump escena20
    elif destino == "v":
        n "Hi ha una fàbrica"
    elif destino == "p":
        v "Per aquí només poden pasar els treballadors de la fàbrica!"
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory
    jump escena21
    
label final:
    
    n "molt bé!"

    return
    
# Dins del Palau =====================================================================

label escena22:

    scene bg palau
    with fade
    
    show secretaria normal at right
    
    $ n_allowed = False
    $ s_allowed = True
    $ e_allowed = False
    $ o_allowed = False
    $ porta_allowed = False
    
    call screen buttons
    
    $ destino = _return
        
    if destino == "s":
        jump escena04
    elif destino == "v":
        n "Estem al despatx del Palau Episcopal..."
    elif destino == "p":
        x "Hola, que vol?"
        menu:
            "Puc parlar amb el Bisbe?":
                x "No, el Bisbe ha sortit"
                jump escena22
            "Em pot donar un clip?":
                x "Sí, aquí tens un ..."
                play sound "magia.mp3"
                $ items.append("clip")
                "Tinc un clip!"
                x "Mai hagués pensat que un clip pogués fer tant feliç a algú!"
                "Gracies"
                x "de res."
                jump escena17
            "No res...":
                jump escena22
    elif destino == "a":
        n "No hi ha res a fer aquí"
    elif destino == "i":
        call inventory

    jump escena22

