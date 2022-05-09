from person import Person

liam = Person("liam", 30, "6'7'") 

katy = Person("katy", 30, "5'2'")

demi = Person("Demi", 30, "5'8'")

timmy = Person("Timmy", 29, "6'1'")

def talking(): 
    liam.talk()
    katy.talk()
    demi.talk()
    timmy.talk()

talking() 