from d17p1 import execute, read_input

def test_full_input():
    output = []
    registers, program_codes = read_input("testinput.txt")
    execute(registers, program_codes, output)
    assert ",".join(output) == "4,6,3,5,6,3,5,2,1,0"

def test_one():
    #If register C contains 9, the program 2,6 would set register B to 1.
    registers = {"A":0, "B": 0, "C": 9}
    program_codes = [2,6]
    execute(registers, program_codes, [])
    assert registers["B"] == 1

def test_two():
    # If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
    registers = {"A": 10, "B": 0, "C": 9}
    program_codes = [5,0,5,1,5,4]
    output = []
    execute(registers, program_codes,output)
    assert ",".join(output) == "0,1,2"

def test_three():
    # If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A
    registers = {"A": 2024, "B": 0, "C": 0}
    program_codes = [0,1,5,4,3,0]
    output = []
    execute(registers, program_codes,output)
    assert ",".join(output) == "4,2,5,6,7,7,7,7,3,1,0"
    assert registers["A"] == 0

def test_four():
    # If register B contains 29, the program 1,7 would set register B to 26`
    registers = {"A": 2024, "B": 29, "C": 0}
    program_codes = [1,7]
    output = []
    execute(registers, program_codes,output)
    assert registers["B"] == 26

