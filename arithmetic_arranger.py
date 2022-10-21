def arithmetic_arranger(problems,solve=False):
    
    values = []
    for value in range(len(problems)):
        values.append(problems[value].split())

    values_top = []
    values_bottom = []
    operations = []
    for value in values:
        values_top.append(value[0])
        values_bottom.append(value[2])
        operations.append(value[1])
        
        
    def validations():
        if len(problems) > 5:
            return "Error: Too many problems."
        else:
            for [i,j,k] in zip(values_top,values_bottom,operations):
                if i.isdigit() and j.isdigit():
                    pass
                else:
                    return "Error: Numbers must only contain digits."
                if len(i) <= 4 and len(j) <= 4:
                    pass
                else:
                    return "Error: Numbers cannot be more than four digits."
                if k == "+" or k == "-":
                    pass
                else:
                    return "Error: Operator must be '+' or '-'."
            return True
        

    def formatting(solve = False):
        length = []
        line = "-"
        for [t,b] in zip(values_top,values_bottom):
            length.append(max(len(t),len(b))+2)
        if solve == True:
            answers = []
            for [i,j,k] in zip(values_top,values_bottom,operations):
                if k == "+":
                    answers.append(int(i)+int(j))
                else:
                    answers.append(int(i)-int(j))
            if len(problems) == 1:
                top = f'{values_top[0].rjust(length[0]," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'
                line2 = f'{line*(length[0])}'
                answer = f'{str(answers[0]).rjust(length[0]," ").rstrip()}'
                string = top + '\n' + bottom + '\n' + str(line2) + '\n' + answer
                return string
            elif len(problems) == 2:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'
                line2 = f'{line*(length[0])}' + "    "+ f'{line*(length[1])}'
                answer = f'{str(answers[0]).rjust(length[0]," ")}{str(answers[1]).rjust(length[1]+4," ").rstrip()}'
                string = top + '\n' + bottom + '\n' + str(line2) + '\n' + answer
                return string
            elif len(problems) == 3:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}{values_top[2].rjust(length[2]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'+ "    " +f'{operations[2]} {values_bottom[2].rjust(length[2]-2," ")}'
                line2 = f'{line*(length[0])}' + "    "+ f'{line*(length[1])}' + "    " + f'{line*(length[2])}'
                answer = f'{str(answers[0]).rjust(length[0]," ")}{str(answers[1]).rjust(length[1]+4," ")}{str(answers[2]).rjust(length[2]+4," ")}'
                string = top + '\n' + bottom + '\n' + str(line2) + '\n' + answer
                return string
            elif len(problems) == 4:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}{values_top[2].rjust(length[2]+4," ")}{values_top[3].rjust(length[3]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'+ "    " +f'{operations[2]} {values_bottom[2].rjust(length[2]-2," ")}'+ "    " +f'{operations[3]} {values_bottom[3].rjust(length[3]-2," ")}'
                line2 = f'{line*length[0]}' + "    " + f'{line*length[1]}' + "    "+ f'{line*length[2]}'+"    "+f'{line*length[3]}'
                answer = f'{str(answers[0]).rjust(length[0]," ")}{str(answers[1]).rjust(length[1]+4," ")}{str(answers[2]).rjust(length[2]+4," ")}{str(answers[3]).rjust(length[3]+4," ")}'
                string = top + '\n' + bottom + '\n' + str(line2) + '\n' + answer
                return string
            elif len(problems) == 5:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}{values_top[2].rjust(length[2]+4," ")}{values_top[3].rjust(length[3]+4," ")}{values_top[4].rjust(length[4]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'+ "    " +f'{operations[2]} {values_bottom[2].rjust(length[2]-2," ")}'+ "    " +f'{operations[3]} {values_bottom[3].rjust(length[3]-2," ")}'+ "    " +f'{operations[4]} {values_bottom[4].rjust(length[4]-2," ")}'
                line2 = f'{line*(length[0])}' + "    "+ f'{line*(length[1])}' + "    " + f'{line*(length[2])}' + "    " + f'{line*(length[3])}' + "    " + f'{line*(length[4])}'
                answer = f'{str(answers[0]).rjust(length[0]," ")}{str(answers[1]).rjust(length[1]+4," ")}{str(answers[2]).rjust(length[2]+4," ")}{str(answers[3]).rjust(length[3]+4," ")}{str(answers[4]).rjust(length[4]+4," ")}'
                string = top + '\n' + bottom + '\n' + str(line2) + '\n' + answer
                return string
            else:
                pass
        else:
            if len(problems) == 1:
                top = f'{values_top[0].rjust(length[0]," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'
                line2 = f'{line*(length[0])}'
                string = top + '\n' + bottom + '\n' + str(line2)
                return string
            elif len(problems) == 2:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'
                line2 = f'{line*(length[0])}' + "    "+ f'{line*(length[1])}'
                string = top + '\n' + bottom + '\n' + str(line2)
                return string
            elif len(problems) == 3:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}{values_top[2].rjust(length[2]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'+ "    " +f'{operations[2]} {values_bottom[2].rjust(length[2]-2," ")}'
                line2 = f'{line*(length[0])}' + "    "+ f'{line*(length[1])}' + "    " + f'{line*(length[2])}'
                string = top + '\n' + bottom + '\n' + str(line2)
                return string
            elif len(problems) == 4:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}{values_top[2].rjust(length[2]+4," ")}{values_top[3].rjust(length[3]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'+ "    " +f'{operations[2]} {values_bottom[2].rjust(length[2]-2," ")}'+ "    " +f'{operations[3]} {values_bottom[3].rjust(length[3]-2," ")}'
                line2 = f'{line*length[0]}' + "    " + f'{line*length[1]}' + "    "+ f'{line*length[2]}'+"    "+f'{line*length[3]}'
                string = str(top) + '\n' + str(bottom) + '\n' + str(line2)
                return string
            elif len(problems) == 5:
                top = f'{values_top[0].rjust(length[0]," ")}{values_top[1].rjust(length[1]+4," ")}{values_top[2].rjust(length[2]+4," ")}{values_top[3].rjust(length[3]+4," ")}{values_top[4].rjust(length[4]+4," ")}'
                bottom = f'{operations[0]}{values_bottom[0].rjust(length[0]-1," ")}'+ "    " +f'{operations[1]}{values_bottom[1].rjust(length[1]-1," ")}'+ "    " +f'{operations[2]} {values_bottom[2].rjust(length[2]-2," ")}'+ "    " +f'{operations[3]} {values_bottom[3].rjust(length[3]-2," ")}'+ "    " +f'{operations[4]} {values_bottom[4].rjust(length[4]-2," ")}'
                line2 = f'{line*(length[0])}' + "    "+ f'{line*(length[1])}' + "    " + f'{line*(length[2])}' + "    " + f'{line*(length[3])}' + "    " + f'{line*(length[4])}'
                string = top + '\n' + bottom + '\n' + str(line2)
                return string
            else:
                pass
        
        
    if validations() == True and solve == True:
        pass
        return formatting(True)
    elif validations() == True and solve == False:
        return formatting()
    elif validations() != True:
        return validations()
