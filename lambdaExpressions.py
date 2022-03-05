g=lambda x:3*x+1
print(g(2))
full_name=lambda fn,ln:fn.strip().title() + " "+ ln.strip().title()
print(full_name(" emilY", "    schWARzowskI                  "))
calculate=lambda x,y,z:x**y-z
print(calculate(4,2,3))
authors=["Isaac Asimov", "Ray Brandburry", "Robert Heinlein", "Arthur C. Clarke", "Douglas Adams",
         "H. G. Wells", "Princess Diana"]
authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(authors)
def quadratic_functions_family(a,b,c):
    return lambda x:a*x**2+b*x+c

f=quadratic_functions_family(1,2,3)
print(f(3))
g=quadratic_functions_family(3,2,1)(4) # not practical
print(g)
