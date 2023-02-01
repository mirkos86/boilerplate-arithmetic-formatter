def arithmetic_arranger(problems,Boolean=None):
    """This function takes a list of 5 strings at most and converts them into sums which,
    conditional upon the presence of a second optional argument set to True, are displayed as
    arithmetic operations arranged into columns."""
    
    # Here we define the number of rows the operations will take when displayed in columns: 
    # 4 if the results is to be displayed, 3 otherwise 
    
    if Boolean==True:
        op_rows=4
    elif Boolean == None: 
        op_rows=3
    
    # We must also check that there are no more than 5 arithmetic operations to perform 
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # We split the operations at the level of the operator string
    # If the operator string is found to be neither "+" nor "-" an exception is thrown
    # We remove potential and unneeded white spaces
    
    operations=[]
        
    for prob in problems:
        if "+" in prob:
            operations.append(prob.replace(" ","").split("+")+["+"])
        elif "-" in prob:
            operations.append(prob.replace(" ","").split("-")+["-"])
        elif "*" or "/" in prob:
            return "Error: Operator must be '+' or '-'."

    # It is now time to check IF operands contain only digits 
    # AND IF these digits are at most 4 for each operand
    # We also append, as a fourth element, the white space for the operator 
    
    for op in operations:
        if len(op[0]) > 4 or len(op[1]) > 4 :
            return "Error: Numbers cannot be more than four digits."
        if not op[0].isdigit() or not op[1].isdigit():
                return "Error: Numbers must only contain digits."
        else:
            op.extend([max(len(op[0]),len(op[1]))+2,max(len(op[0]),len(op[1]))-len(op[1])+1])
     
    # Now we create a list of the actual operations, including the results
        
    results=[]
    
    for op in operations:
        if op[2] == "+":
            results+=[[op[0],op[2]+" "*op[4]+op[1],"-"*op[3],str(int(op[0])+int(op[1]))]]
        else:
            results+=[[op[0],op[2]+" "*op[4]+op[1],"-"*op[3],str(int(op[0])-int(op[1]))]]
    
    # In the following lines, based on the value of op_rows, we arrange the operations
    # in a string that displays them all in columns  
    
    displayed=""
    
    for i in range(op_rows):
      for j in range(len(results)):
        width = str(operations[j][3])
        if j != len(results)-1:
          displayed+=('{:>'+width+'}    ').format(results[j][i])
        elif j == len(results)-1 and i != op_rows-1:
          displayed+=('{:>'+width+'}\n').format(results[j][i])
        else:
          displayed+=('{:>'+width+'}').format(results[j][i])
                                      
    return displayed