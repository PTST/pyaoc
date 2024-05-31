from utils import Computer
import utils
from day07 import Day07


def test_day02():
    comp = Computer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    comp.run()
    assert [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50] == comp.program[:12]

    comp = Computer([1, 0, 0, 0, 99])
    comp.run()
    assert [2, 0, 0, 0, 99] == comp.program[:5]

    comp = Computer([2, 3, 0, 3, 99])
    comp.run()
    assert [2, 3, 0, 6, 99] == comp.program[:5]

    comp = Computer([2, 4, 4, 5, 99, 0])
    comp.run()
    assert [2, 4, 4, 5, 99, 9801] == comp.program[:6]

    comp = Computer([1, 1, 1, 4, 99, 5, 6, 0, 99])
    comp.run()
    assert [30, 1, 1, 4, 2, 5, 6, 0, 99] == comp.program[:9]

    comp = Computer(utils.get_input_array_int(2, 2019), 12, 2)  # part 1
    comp.run()
    assert 3058646 == comp.program[0]

    comp = Computer(utils.get_input_array_int(2, 2019), 89, 76)  # part 2
    comp.run()
    assert 19690720 == comp.program[0]


def test_day05():
    comp = Computer([3, 0, 4, 0, 99], inputs=[22])
    comp.run()
    assert comp.latest_output == 22

    comp = Computer([3, 0, 4, 0, 99], inputs=[23])
    comp.run()
    assert comp.latest_output == 23

    comp = Computer([3, 0, 4, 0, 99], inputs=[2568])
    comp.run()
    assert comp.latest_output == 2568

    comp = Computer(utils.get_input_array_int(5, 2019), inputs=1)  # part 1
    comp.run()
    assert 16574641 == comp.latest_output

    comp = Computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], inputs=8)
    comp.run()
    assert 1 == comp.latest_output

    comp = Computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], inputs=1)
    comp.run()
    assert 0 == comp.latest_output

    comp = Computer([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], inputs=8)
    comp.run()
    assert 0 == comp.latest_output

    comp = Computer([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], inputs=1)
    comp.run()
    assert 1 == comp.latest_output

    comp = Computer([3, 3, 1108, -1, 8, 3, 4, 3, 99], inputs=8)
    comp.run()
    assert 1 == comp.latest_output

    comp = Computer([3, 3, 1108, -1, 8, 3, 4, 3, 99], inputs=1)
    comp.run()
    assert 0 == comp.latest_output

    comp = Computer([3, 3, 1107, -1, 8, 3, 4, 3, 99], inputs=8)
    comp.run()
    assert 0 == comp.latest_output

    comp = Computer([3, 3, 1107, -1, 8, 3, 4, 3, 99], inputs=1)
    comp.run()
    assert 1 == comp.latest_output

    comp = Computer(utils.get_input_array_int(5, 2019), inputs=5)  # part 1
    comp.run()
    assert 15163975 == comp.latest_output


def test_day07():
    assert 43210 == Day07.calc_amplified_trust(
        [4, 3, 2, 1, 0],
        [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
    )

    assert 54321 == Day07.calc_amplified_trust(
        [0, 1, 2, 3, 4],
        [
            3,
            23,
            3,
            24,
            1002,
            24,
            10,
            24,
            1002,
            23,
            -1,
            23,
            101,
            5,
            23,
            23,
            1,
            24,
            23,
            23,
            4,
            23,
            99,
            0,
            0,
        ],
    )

    assert 11828 == Day07().part_1()

    assert 18216 == Day07.calc_amplified_trust_2(
        [9, 7, 8, 5, 6],
        [
            3,
            52,
            1001,
            52,
            -5,
            52,
            3,
            53,
            1,
            52,
            56,
            54,
            1007,
            54,
            5,
            55,
            1005,
            55,
            26,
            1001,
            54,
            -5,
            54,
            1105,
            1,
            12,
            1,
            53,
            54,
            53,
            1008,
            54,
            0,
            55,
            1001,
            55,
            1,
            55,
            2,
            53,
            55,
            53,
            4,
            53,
            1001,
            56,
            -1,
            56,
            1005,
            56,
            6,
            99,
            0,
            0,
            0,
            0,
            10,
        ],
    )

    assert 139629729 == Day07.calc_amplified_trust_2(
        [9, 8, 7, 6, 5],
        [
            3,
            26,
            1001,
            26,
            -4,
            26,
            3,
            27,
            1002,
            27,
            2,
            27,
            1,
            27,
            26,
            27,
            4,
            27,
            1001,
            28,
            -1,
            28,
            1005,
            28,
            6,
            99,
            0,
            0,
            5,
        ],
    )

    assert 1714298 == Day07().part_2()


def test_day09():
    program = [109, 19, 204, -34, 99]
    comp = Computer(program)
    comp.relative_base = 2000
    comp.program[1985] = 123
    comp.run()
    assert 123 == comp.latest_output

    program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    comp = Computer(program)
    comp.run()
    assert program == comp.outputs

    comp = Computer([104, 1125899906842624, 99])
    comp.run()
    assert 1125899906842624 == comp.latest_output

    comp = Computer([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
    comp.run()
    assert 16 == len(str(comp.latest_output))

    comp = Computer(utils.get_input_array_int(9, 2019), inputs=1)  # part 1
    comp.run()
    assert 3429606717 == comp.latest_output

    comp = Computer(utils.get_input_array_int(9, 2019), inputs=2)  # part 2
    comp.run()
    assert 33679 == comp.latest_output
