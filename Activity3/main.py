from ArrayStack import ArrayStack as Stack

open_parenthesis = ["[" , "{" , "("]
close_parenthesis = ["]" , "}" , ")"]

def is_matching(expression):
    stack = Stack()
    for i in expression:
        if i in open_parenthesis:
            stack.push(i)
        elif i in close_parenthesis:
            pos = close_parenthesis.index(i)
            if not stack.is_empty() and open_parenthesis[pos] == stack.top():
                stack.pop()
            else:
                return "Unbalanced"

    return "Balanced" if stack.is_empty() else "Unbalanced"

string = input("Enter an expression to check for balanced or unbalanced parentheses: ")
print("The user inputs \"", string, "\" and is ", is_matching(string))


def reverse_file(filename):
    with open(filename, "r") as file:
        content = file.readlines()

    content.reverse()

    with open(filename, 'w') as file:
        for line in content:
            file.write(line)

reverse_file("textFile.txt")

