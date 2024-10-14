dim = float(input('What is the intended measurement?\n'))
actual = float(input('What is the actual measurement?\n'))
tol = float(input('What is the tolerance?\n'))

test = abs(dim-actual)

if(test <= tol):
    print("The part is within spec")
else:
    print("The part is out of spec")
