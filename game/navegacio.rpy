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
return