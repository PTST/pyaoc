import copy
from enum import Enum
from typing import Optional

class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class Computer():
    program = list[int]
    instruction_pointer = 0
    relative_base = 0
    paused = True
    inputs = []
    outputs = []

    @property
    def latest_output(self):
        return self.outputs[-1]

    @property
    def instruction(self):
        if self.instruction_pointer >= len(self.program):
            return None
        instruction = self.program[self.instruction_pointer]
        op_code = int(str(instruction).zfill(2)[-2:])
        parameter_modes = [ParameterMode(int(x)) for x in str(instruction).zfill(5)[::-1][2:]]
        return (op_code, parameter_modes)


    def __init__(self, program, *args, inputs:Optional[list[int]]=None):
        self.program = copy.deepcopy(program) + ([0] * 100000)
        self.outputs = []
        self.inputs = []
        self.paused = True
        self.relative_base = 0
        self.instruction_pointer = 0
        if inputs:
            self.inputs = inputs if isinstance(inputs, list) else [inputs]
        for i, x in enumerate(args):
            self.program[i+1] = x

    def add_input(self, value: int):
        self.inputs.append(value)

    def run(self):
        self.paused = False
        while self.instruction and not self.paused:
            self.compute_cycle()

    def clear_output(self):
        self.outputs = []

    def compute_cycle(self):
        instruction = self.instruction
        op_code = instruction[0]
        parameters = instruction[1]
        match op_code:
            case 1:
                self.add(self.get(self.instruction_pointer+1, parameters[0]), self.get(self.instruction_pointer+2, parameters[1]), self.get_store_index(self.instruction_pointer+3, parameters[2]))
                self.instruction_pointer+=4
            case 2:
                self.multiply(self.get(self.instruction_pointer+1, parameters[0]), self.get(self.instruction_pointer+2, parameters[1]), self.get_store_index(self.instruction_pointer+3, parameters[2]))
                self.instruction_pointer+=4
            case 3:
                self.input(self.get_store_index(self.instruction_pointer+1, parameters[0]))
                self.instruction_pointer += 2
            case 4:
                self.output(self.get(self.instruction_pointer+1, parameters[0]))
                self.instruction_pointer += 2
            case 5:
                self.jump_if_true(self.get(self.instruction_pointer+1, parameters[0]), self.get(self.instruction_pointer+2, parameters[1]))
            case 6:
                self.jump_if_false(self.get(self.instruction_pointer+1, parameters[0]), self.get(self.instruction_pointer+2, parameters[1]))
            case 7:
                self.less_than(self.get(self.instruction_pointer+1, parameters[0]), self.get(self.instruction_pointer+2, parameters[1]), self.get_store_index(self.instruction_pointer+3, parameters[2]))
                self.instruction_pointer += 4
            case 8:
                self.equals(self.get(self.instruction_pointer+1, parameters[0]), self.get(self.instruction_pointer+2, parameters[1]), self.get_store_index(self.instruction_pointer+3, parameters[2]))
                self.instruction_pointer += 4
            case 9:
                self.adjust_relative_base(self.get(self.instruction_pointer+1, parameters[0]))
                self.instruction_pointer += 2
            case 99:
                self.halt()
            case _ :
                raise NotImplementedError("Unknown opcode")

    # Opcode 1
    def add(self, a: int, b: int, result_pos: int):
        self.store(result_pos, a + b)

    # Opcode 2
    def multiply(self, a: int, b: int, result_pos: int):
        self.store(result_pos, a * b)

    # Opcode 3
    def input(self, index: int):
        if self.inputs:
            self.store(index, self.inputs.pop(0))
        else:
            self.instruction_pointer -= 2
            self.paused = True

    # Opcode 4
    def output(self, value: int):
        self.outputs.append(value)
        # print(self.outputs[-1])

    # Opcode 5
    def jump_if_true(self, condition, value):
        if condition != 0:
            self.instruction_pointer = value
        else:
            self.instruction_pointer += 3

    # Opcode 6
    def jump_if_false(self, condition, value):
        if condition == 0:
            self.instruction_pointer = value
        else:
            self.instruction_pointer += 3

    # Opcode 7
    def less_than(self, a, b, result_pos):
        self.store(result_pos, int(a < b))

    # Opcode 8
    def equals(self, a, b, result_pos):
        self.store(result_pos, int(a == b))

    # Opcode 9
    def adjust_relative_base(self, value):
        self.relative_base += value

    # Opcode 99
    def halt(self):
        self.paused = True

    def get(self, index: int, parameter_mode: ParameterMode) -> int:
        if parameter_mode == ParameterMode.POSITION:
            return self.program[self.program[index]]
        if parameter_mode == ParameterMode.RELATIVE:
            return self.program[self.program[index]+self.relative_base]
        return self.program[index]

    def get_store_index(self, index: int, parameter_mode: ParameterMode) -> int:
        if parameter_mode == ParameterMode.POSITION:
            return self.program[index]
        if parameter_mode == ParameterMode.RELATIVE:
            return self.program[index]+self.relative_base
        return index

    def store(self, index: int, value: int):
        self.program[index] = value