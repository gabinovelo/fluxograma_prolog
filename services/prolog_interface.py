from pyswip import Prolog
from models.course import Course
from database.prolog_mgr import prolog

def assert_course(id: str, requirements: str):

    requirements = requirements if requirements else []

    for req in requirements:
        prolog.assertz(f"depends({id}, {req})")

def retract_course(id: str):

    prolog.retractall(f"depends({id}, _)")
    prolog.retractall(f"depends(_, {id})")

def verify_enrollment(history: list[str], id: str):

    history_atoms = [f"'{item}'" for item in history]
    history_pl = "[" + ",".join(history_atoms) + "]"

    query_str = f"can_enroll({history_pl}, '{id}')"

    result = list(prolog.query(query_str))

    return len(result) > 0
