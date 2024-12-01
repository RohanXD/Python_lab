# WAP to implement to display a class Mathematics that contains a function SOS() that will display the sum os series of all elements passed in it

class Mathematics:
    def sos(self,*args):
        print(type(args))
        s=0
        for i in args:
            s=s+i
        print(s)

a=Mathematics()
a.sos(10,10,30)
a.sos(1,4,1,35,6,3,3,56,3,4)
a.sos(213,5345,23,4,53456,342,545)