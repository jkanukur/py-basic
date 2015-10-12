#function definition

#argument types:
#   *requried
#   *default
#   **variable-length**
#   *keyword

def va(a,*b,**c):
    print a     #required argument
    print b     #variable-length argument, taken as tuples
    print c     #variable-length argument, taken as a dictionary

#va(1,2,3,4,y=14,z=12,t=6)


## Global and local variable

k = 1

def fu(a,k):
    def nf():
        print 'inside'
    a=7
    nf()
    print a
    k=[2,3,4]


a=6
k=[1,2,3]

fu(a,k)
print a


#   Single Line function

def inlinef(a,k):
    l = lambda x,y : x*y
    print k
    print l(4,3)
    k.append(3)

print inlinef(a,k)