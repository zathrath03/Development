"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another
expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any
division by zero operation.

Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
range [-200, 200].
"""


import unittest


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # initialize a stack
        stack: list[int] = []
        # initialize a set of operators
        operators = {"+", "-", "*", "/"}
        # loop through each token in tokens
        for token in tokens:
            # if it is not an operator, push it onto the stack
            # if it is an operator, pop two values, execute the operation, push result
            if token in operators:
                token = self.process_operator(stack, token)
            stack.append(int(token))
        # return the last item on the stack
        return stack[0]

    def process_operator(self, stack, token):
        num2 = stack.pop()
        num1 = stack.pop()

        match token:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return num1 / num2
            case _:
                raise LookupError


class Test(unittest.TestCase):
    test_cases = (
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
         22)
    )

    def test_evalRPN(self):
        sol = Solution()
        for tokens, expected in self.test_cases:
            assert sol.evalRPN(tokens) == expected
            print(f"{tokens} passed")


if __name__ == "__main__":
    unittest.main()
