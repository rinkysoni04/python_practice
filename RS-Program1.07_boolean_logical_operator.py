C=6
D=2
if C>D:
    print("#1 it worked")

if not(C>D):
    print("#2 it worked!")


if C>=6 and D>1:
    print("#3 it worked!")


if not(C>=6 and D>1):
    print("#4 it worked!")

if C>5 or D>5:
    print("#5 it worked!")


if C>6 or D>3:
    print("#6 it worked!")


if ((C>6 and D>3) or (C>=6 or D>3)):
    print("#7 it worked!")


if not(((C>6 and D>3) or (C>=6 or D>3))):
    print("#8 it worked!")
