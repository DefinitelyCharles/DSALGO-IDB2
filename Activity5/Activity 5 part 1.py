def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') <= 1):
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        elif token in precedence:
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return ' '.join(output)


def evaluate_postfix(expression):
    stack = []

    def apply_operator(op, operand1, operand2):
        if op == '+':
            return operand1 + operand2
        elif op == '-':
            return operand1 - operand2
        elif op == '*':
            return operand1 * operand2
        elif op == '/':
            if operand2 == 0:
                raise ValueError("Division by zero is not allowed")
            return operand1 / operand2
        else:
            raise ValueError(f"Unsupported operator: {op}")

    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') <= 1):
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(token, operand1, operand2)
            stack.append(result)

    return stack.pop()


def main():
    infix_expression = input("Enter an infix expression (with spaces): ")

    try:
        postfix_expression = infix_to_postfix(infix_expression)
        print(f"Postfix expression: {postfix_expression}")

        result = evaluate_postfix(postfix_expression)
        print(f"Result of the postfix expression: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
