def rage_person(person):
    person.setattack(person.getattack() * 2)
    person.setspeed(person.getspeed() * 2)


def heal_person(person):
    if(person.get_health()*1.5) > person.getmaxhealth():
        person.sethealth(person.getmaxhealth())
    else:
        person.sethealth(person.get_health()*1.5)


def heal(game):
    if game.isQueen():
        queen = game.get_attackers().get_queen()
        if not queen.is_dead():
            heal_person(queen)
    else:
        king = game.get_attackers().get_king()
        if not king.is_dead():
            heal_person(king)

    barbarian = game.get_attackers().get_barbarians()
    archers = game.get_attackers().get_archers()
    balloons = game.get_attackers().get_balloons()

    for barb in barbarian:
        if not barb.is_dead():
            heal_person(barb)

    for archer in archers:
        if not archer.is_dead():
            heal_person(archer)

    for balloon in balloons:
        if not balloon.is_dead():
            heal_person(balloon)


def rage(game):
    if game.isQueen():
        queen = game.get_attackers().get_queen()
        if not queen.is_dead():
            rage_person(queen)
    else:
        king = game.get_attackers().get_king()
        if not king.is_dead():
            rage_person(king)

    barbarian = game.get_attackers().get_barbarians()
    archers = game.get_attackers().get_archers()
    balloons = game.get_attackers().get_balloons()

    for barb in barbarian:
        if not barb.is_dead():
            rage_person(barb)

    for archer in archers:
        if not archer.is_dead():
            rage_person(archer)

    for balloon in balloons:
        if not balloon.is_dead():
            rage_person(balloon)
