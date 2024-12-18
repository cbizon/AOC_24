from math import pow

def read_input(infile):
    regvals = {}
    with (open(infile) as f):
        for register in ["A", "B","C"]:
            line = f.readline()
            value = int(line.strip().split(":")[-1])
            regvals[register] = value
        _ = f.readline()
        programvals = f.readline().split(":")[1].strip()
        program = programvals.split(",")
    return regvals, [int(i) for i in program]

def adv(operand,registers,output,ep):
    val = get_value(operand,registers)
    numerator = registers["A"]
    denominator = pow(2,val)
    registers["A"] = int(numerator / denominator)
    return ep + 2

def bxl(operand, registers, output, ep):
    result = operand ^ registers["B"]
    registers["B"] = result
    return ep + 2

def bst(operand, registers, output, ep):
    val = get_value(operand,registers)
    result = val % 8
    registers["B"] = result
    return ep + 2

def jnz(operand, registers, output, ep):
    if registers["A"] == 0:
        return ep + 2
    return operand

def bxc(operand, registers, output, ep):
    registers["B"] = registers["B"] ^ registers["C"]
    return ep + 2

def out(operand, registers, output, ep):
    value = get_value(operand,registers)
    output.append( str(value % 8 ) )
    return ep + 2

def bdv(operand,registers,output, ep):
    val = get_value(operand)
    numerator = registers["A"]
    denominator = pow(2,val)
    registers["B"] = int(numerator / denominator)
    return ep + 2

def cdv(operand,registers,output, ep):
    val = get_value(operand,registers)
    numerator = registers["A"]
    denominator = pow(2,val)
    registers["C"] = int(numerator / denominator)
    return ep + 2

ops = [adv,bxl,bst,jnz,bxc,out,bdv,cdv]

def get_value(combo,registers):
    #Combo operands 0 through 3 represent literal values 0 through 3.
    #Combo operand 4 represents the value of register A.
    #Combo operand 5 represents the value of register B.
    #Combo operand 6 represents the value of register C.
    #Combo operand 7 is reserved and will not appear in valid programs.
    if combo in [0,1,2,3]:
        return combo
    if combo == 4:
        return registers["A"]
    if combo == 5:
        return registers["B"]
    if combo == 6:
        return registers["C"]
    print("uh oh", combo)
    exit()

def execute(registers, program_codes, output):
    execution_pointer = 0
    while execution_pointer >=0 and execution_pointer < len(program_codes):
        op = program_codes[execution_pointer]
        combo = program_codes[execution_pointer+1]
        execution_pointer = ops[op](combo,registers,output,execution_pointer)

def go():
    output=[]
    registers, program_codes = read_input("input.txt")
    execute(registers, program_codes, output)
    print(",".join(output))

if __name__ == "__main__":
    go()