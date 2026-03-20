from pyswip import Prolog

prolog = Prolog()
prolog.consult("database/engine.pl")

def get_prolog():
    return prolog