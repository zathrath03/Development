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
        stack: list[int] = []
        operators = {"+": lambda a, b: a + b,
                     "-": lambda a, b: a - b,
                     "*": lambda a, b: a * b,
                     "/": lambda a, b: a / b}
        for token in tokens:
            if token in operators:
                operation = operators[token]
                num2, num1 = stack.pop(), stack.pop()
                token = operation(num1, num2)
            stack.append(int(token))
        return stack[0]


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
