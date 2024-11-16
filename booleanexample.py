#Python's Boolean operators are and, or, and not. The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True. Otherwise, it evaluates to False.

#This should print True
print ( 1 == 1 and 2 ==2)
#This should print False
print ( 1 == 1 and 2 ==3)

#The or operator also takes two arguments. It evaluates to True if either (or both) of its arguments are True, and False if both arguments are False.

#This should print True
print(1 == 1 or 2 == 4)

#Boolean Not: Unlike other operators we've seen so far, not only takes one argument, and inverts it. The result of not True is False, and not False goes to True.

#This should print False
print(not 1 == 1)
