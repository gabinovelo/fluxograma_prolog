:- dynamic depends/2.

can_enroll(History, Course) :- forall(depends(Course, Req), member(Req, History)).

is_prerequisite(Course, Req) :- depends(Course, Req).

is_prerequisite(Course, Req) :- 
    depends(Course, Inter), 
    is_prerequisite(Inter, Req).