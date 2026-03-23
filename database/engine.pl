:- dynamic depends/2.

can_enroll(History, Course) :- forall(depends(Course, Req), member(Req, History)).
