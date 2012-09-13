#a method is a function that is associated with a particular class


#Exercise 3.3

space = ' '

def right_just(word, number):
    print space * (number - len(word)) + word

right_just('name',100)


#Exercise 3.4


def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


do_four(print_twice, 'spam')

#Exercise 3.5

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print '+ - - - -',

# the commna here is meant to keep all posts in same line when we repeat the function later on
def print_post():
    print '|        ',

def print_beams():
    do_twice(print_beam)
    print '+'

# Here we don't need a comma at the end because the print_post() function ends with a comma
def print_posts():
    do_twice(print_post)
    print '|'

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()



#Chapter 5 Conditionals and Recursion

#Exercise 5.1.1
# Fermant's Last Theorem says that there exists no intergers a, b and c s.t. a^n + b^n = c^n


def check_fermant(a, b, c, n):
    if n <= 2:
        print "n must be greater than 2"
    
    else:
        if a^n + b^n == c^n:
            print "Holy smokes, Fermat was wrong"
        else:
            print "No, that doesn't work"


# Key board input
# this is not working in the order it is supposed to work 

#name = raw_input('enter name \n')
#print name



#Exercise 5.1.2

#Requires user input


#Exercise 5.2.1

#function to check if three lines can be used to form a triangle

def test_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b :
        print 'not possible'
    else:
        print 'possible'
        

test_triangle(1,2,4)

# Fruitful Functions

# exercise 6.1. return does not print it only stores the value

def eval(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1
    
print eval(2,3)


# Exercise 6.2; incremental development of functions allows for testing which may be helpful in limiting errors

def hypo(first_side, second_side):
    square_of_first = first_side**2
    square_of_second = second_side**2
    sum_of_squares = square_of_first + square_of_second
    return sum_of_squares**0.5

print hypo(3,4)


# Exercise 6.3 

def is_between(x, y, z):
    if x <= y <= z:
        print 'Yes'
    else:
        print 'No'


# same function using Boolean

def is_between(x, y, z):
    if x <= y <= z:
        print x <= y <= z
    else:
        print 'False'

is_between(4,2,3)

# exercise 6.4

def b(z):
    prod = a(z,z)
    print z, prod
    return prod

def a(x,y):
    x = x + 1
    return x * y

def c(x, y, z):
    sum = x + y + z
    pow = b(sum)**2
    return pow

x = 1
y = x + 1

print c(x, y+3, x+y)

# exercise 6.5 Akerman function

def A(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m-1,1)
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))
    elif m < 0:
        return 'm must be greater or equal to zero'


print A(3,4)

# for larger values of m and n "RuntimeError: maximum recursion depth exceeded

#Exercise 6.6 using recursion 

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_plaindrome(first_word, second_word):
    if len(first_word) != len(second_word):
        print 'No'
    else:
        if first(first_word) != last(second_word):
            print 'No'
        else:
            first_word = middle(first_word)
            second_word = middle(second_word)
            is_plaindrome(first_word, second_word)
            print 'Yes'


# exercise 6.7

def is_power(a,b):
    if a / b == 0:
        a = a/b
        print 'True'
    else:
        print 'False'

# exercise 6.8 GCF using Euclid's algorithm

def gcf(x, y):
    if x >= y and x % y == 0:
        return y
    elif x >= y and x % y != 0:
        x = x % y
        gcf(x,y)      
    elif x <= y and y % x == 0:
        return x
    elif x <= y and y % x != 0:
        y = y % x
        gcf(x,y)

# Chapter 7

# exercise 7.1

# print n function using recursion from section 5.8

def countdown_recursion(n):
    if n <= 0:
        print 'Blastoff!'
    else:
        print n
        countdown(n-1)
        
# print n function using iteration

def countdown_iteration(n):
    while n>0:
        print n
        n = n-1
    print 'Blastoff!'

countdown_iteration(3)


# exercise 7.2

while True:
    line = raw_input('>')
    if line == 'done':
        break
    print line
print 'Done!'

