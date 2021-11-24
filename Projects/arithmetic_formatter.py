"""
Arithmetic Formatter

https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
"""


def arithmetic_arranger(problems, show_answers=False):
    lines_per_problem = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        left_operand, operator, right_operand = problem.split()

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if len(left_operand) > 4 or len(right_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        if left_operand.isdigit() is False or right_operand.isdigit() is False:
            return "Error: Numbers must only contain digits."

        longest_operand = left_operand if len(left_operand) > len(right_operand) else right_operand

        max_line_length = len(operator + ' ' + longest_operand)

        first_line = left_operand.rjust(max_line_length)
        second_line = operator + ' ' + right_operand.rjust(max_line_length - 2)
        separator_line = '-' * max_line_length

        lines = [first_line, second_line, separator_line]

        if show_answers:
            a = int(left_operand)
            b = int(right_operand)
            result = None

            if operator == '+':
                result = a + b
            elif operator == '-':
                result = a - b

            lines.append(str(result).rjust(max_line_length))

        lines_per_problem.append(lines)

    arranged_problems = ""

    for i in range(len(lines_per_problem[0])):
        line = []
        for problem_lines in lines_per_problem:
            line.append(problem_lines[i])
        arranged_problems += "    ".join(line) + "\n"

    return arranged_problems.rstrip()


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
