
Part 1: Discussion Questions
Recursion

    In your own words, what is recursion? In the method definition of a recursive function,
    the method calls  itself in its return object (analogy: nested dools), 
    with a different parameter.
    It can always replace loops in which case it usually necessitates less code.
    
    Why is it necessary to have a base case?
    ==> It is necessary to have a base case to tell the function at which point it 
    should stop calling itself (if there is no end point it will continue working over and over).
    When using Python, 1000  is the  limit number of  recursive call.
    Often base case are degenerate case.

Graphs

    - What is a graph?A graph is a succession of nodes linked to each other by 
    an edge (not all nodes are necessary linked to each other). The relationships 
    can be directed or non directed. Each node can have a weight.
   - How is a graph different from a tree? A tree is a graph but a graph is not 
   necessarily a tree. Indeed a graph can be directed or non directed and can be cyclic or acyclic.
    Whereas trees can only be directed and acyclic. Finally trees have hierarchy, graphs do not.
    Give an example of something that would be good to model with a graph.
    ==> carpooling model
    ==> scheduling exams in a university
    ==> friends relationship on facebook

