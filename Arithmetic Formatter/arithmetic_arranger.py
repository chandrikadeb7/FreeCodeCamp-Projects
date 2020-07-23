def arithmetic_arranger(problems, showAns = False):

  if len(problems)>5:
    return "Error: Too many problems."
  else:
    
    topLine = ""
    secondLine = ""
    dashLine = ""
    answerLine = ""

    arranged_problems = []
    for i, problem in enumerate(problems):
      x = problem.split()
      n1 = x[0]
      n2 = x[2]
      operand = x[1]

      if operand not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'." 
      else:
        for digit in n1:
          if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
            return "Error:  Numbers must only contain digits." 
          else: 
            continue

        for digit in n2:
          if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
            return "Error: Numbers must only contain digits." 
          else: 
            continue

        if len(n1)>4 or len(n2)>4:
          return "Error: Numbers cannot be more than four digits."
        else: 

            if operand == '+':
              answer = int(n1) + int(n2)
            else: 
              answer = int(n1) - int(n2)
            
            width = max(len(n1),len(n2)) +2
            topLine += str(n1.rjust(width))
            secondLine +=  str(operand + n2.rjust(width-1)) 
            dashLine += str("-" * width)
            answerLine += str(answer).rjust(width)

            if i < len(problems)-1:
              topLine += "    "
              secondLine += "    "
              dashLine += "    "
              answerLine += "    "
            
            if showAns == True: 
              arranged_problems = (topLine + "\n" + secondLine + "\n" + dashLine + "\n" + answerLine)
            else: 
              arranged_problems = (topLine + "\n" + secondLine + "\n" + dashLine)


    return arranged_problems
