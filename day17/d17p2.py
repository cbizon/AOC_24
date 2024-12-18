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
    output.append( value % 8 )
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
    # The difference is that we'll run until we find out that this is not a self-creating program/register
    execution_pointer = 0
    while execution_pointer >=0 and execution_pointer < len(program_codes):
        op = program_codes[execution_pointer]
        combo = program_codes[execution_pointer+1]
        execution_pointer = ops[op](combo,registers,output,execution_pointer)
    return output

def go():
    # We originally took a brute force approach, but that's clearly not going to work.  If you look at the program
    # that runs, it's basically shifting the A register by 3 bits every pass through the code until it's complete.
    # So the final output has to be made from the first three bits in A.
    # The next to the last output is made from the first 6 bits, but the first 3 are already fixed
    # And so on
    # So we only need to run through 8 possibilities to add the next 3 bits.
    # So instead of the 2**48 numbers that we could search, we only need to look at 8 * 14, which is a lot more manageable.
    #
    # Unfortunately it's slightly more complicated.  Because within each triplet there might be more than one soluton
    # And taking the smallest one doesn't necessarily admit a solution in the next triplet.  So we have to do some
    # backtracking (nasty)
    registers, program_codes = read_input("input.txt")
    valid_partial_solutions = ['']
    solutions = []
    while len(valid_partial_solutions) > 0:
        A_bits = valid_partial_solutions.pop()
        for i in range(8):
            test_A = int( A_bits + format(i,'03b'), 2)
            registers["A"] = test_A
            output = []
            execute(registers, program_codes, output)
            no = len(output)
            if output == program_codes[-no:]:
                newbits = A_bits + format(i, '03b')
                if len(output) == len(program_codes):
                    solutions.append( newbits )
                else:
                    valid_partial_solutions.append(newbits)
    print("solutions:",solutions)
    dec = [int(s,2) for s in solutions]
    print(min(dec))

def go_test():
    registers, program_codes = read_input("testinput2.txt")
    registers["A"] = 117440
    output= []
    found = execute(registers, program_codes, output)
    print(found,output,program_codes)

if __name__ == "__main__":
    go()