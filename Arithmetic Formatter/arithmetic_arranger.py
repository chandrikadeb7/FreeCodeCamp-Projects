def arithmetic_arranger(problems, show_ans=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    arranged_problems = []
    for i, problem in enumerate(problems):
        x = problem.split()
        n1 = x[0]
        n2 = x[2]
        operand = x[1]

        if operand not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        for digit in n1:
            if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return "Error:  Numbers must only contain digits."

        for digit in n2:
            if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return "Error: Numbers must only contain digits."

        if len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."

        answer = int(n1) - int(n2)

        if operand == '+':
            answer = int(n1) + int(n2)

        width = max(len(n1), len(n2)) + 2
        top_line += str(n1.rjust(width))
        second_line += str(operand + n2.rjust(width - 1))
        dash_line += str("-" * width)
        answer_line += str(answer).rjust(width)

        if i < len(problems) - 1:
            top_line += "    "
            second_line += "    "
            dash_line += "    "
            answer_line += "    "

        arranged_problems = (top_line + "\n" + second_line + "\n" + dash_line)
        if show_ans:
            arranged_problems = (top_line + "\n" + second_line + "\n" + dash_line + "\n" + answer_line)

    return arranged_problems
