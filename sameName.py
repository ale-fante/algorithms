def spam():
	eggs = 'spam local'
	print(eggs) # prints 'spam local'

def bacon():
	eggs = 'bacon local'
	print(eggs) # prints 'bacon local'
	spam()
	print(eggs) # prints bacon local


eggs = 'global'
bacon()
print(eggs) # prints 'global'


# Theere are four rules to tell whether a variable is in local scope or global scope:
# 1) If a variable is being used in the global scope (that is, outside of all functions), then it's always a global variable
# 2) If there is a global statement for that variable in a function, it is a global variable
# 3) Otherwise, if a variable is used in an assignment statement in the function, it is a local variable
# 4) But if the variable is not used in an assignment statement, it is a global variable

