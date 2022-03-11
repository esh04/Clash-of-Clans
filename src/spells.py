def rage_person(person):
    person.setattack(person.getattack() * 2)
    person.setspeed(person.getspeed() * 2)


def heal_person(person):
    if(person.get_health()*1.5) > person.getmaxhealth():
        person.sethealth(person.getmaxhealth())
    else:
        person.sethealth(person.get_health()*1.5)


def heal(game):
    king = game.get_attackers().get_king()
    barbarian = game.get_attackers().get_barbarians()
    if not king.is_dead():
        heal_person(king)
    for barb in barbarian:
        if not barb.is_dead():
            heal_person(barb)


def rage(game):
    king = game.get_attackers().get_king()
    barbarian = game.get_attackers().get_barbarians()
    if not king.is_dead():
        rage_person(king)
    for barb in barbarian:
        if not barb.is_dead():
            rage_person(barb)
