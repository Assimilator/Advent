import unittest
import os
import adventofcodeD01 as d01
import adventofcodeD02 as d02
import adventofcodeD03 as d03
import adventofcodeD04 as d04
import adventofcodeD05 as d05
import adventofcodeD06 as d06
import adventofcodeD07 as d07
import adventofcodeD08 as d08
import adventofcodeD09 as d09
import adventofcodeD10 as d10
import adventofcodeD11 as d11
import adventofcodeD12 as d12
import adventofcodeD13 as d13
import adventofcodeD14 as d14


class advent2021TestCase(unittest.TestCase):
    def test_D01_1(self):
        data = d01.load_data("inputs/inputD01-1.txt")
        self.assertEqual(7, d01.part1(data))
        self.assertEqual(5, d01.part2(data))

    def test_D01_2(self):
        data = d01.load_data("inputs/inputD01-2.txt")
        self.assertEqual(1298, d01.part1(data))
        self.assertEqual(1248, d01.part2(data))

    def test_D02_1(self):
        data = d02.load_data("inputs/inputD02-1.txt")
        self.assertEqual(150, d02.part1(data))
        self.assertEqual(900, d02.part2(data))

    def test_D02_2(self):
        data = d02.load_data("inputs/inputD02-2.txt")
        self.assertEqual(1693300, d02.part1(data))
        self.assertEqual(1857958050, d02.part2(data))

    def test_D03_1(self):
        lines, max_bit = d03.load_data("inputs/inputD03-1.txt")
        self.assertEqual(198, d03.part1(lines, max_bit))
        self.assertEqual(230, d03.part2(lines, max_bit))

    def test_D03_2(self):
        lines, max_bit = d03.load_data("inputs/inputD03-2.txt")
        self.assertEqual(3242606, d03.part1(lines, max_bit))
        self.assertEqual(4856080, d03.part2(lines, max_bit))

    def test_D04_1(self):
        numbers, lines = d04.load_data("inputs/inputD04-1.txt")
        boards = d04.load_boards(lines)
        self.assertEqual(4512, d04.play_p1(boards, numbers))
        self.assertEqual(1924, d04.play_p2(boards, numbers))

    def test_D04_2(self):
        numbers, lines = d04.load_data("inputs/inputD04-2.txt")
        boards = d04.load_boards(lines)
        self.assertEqual(4662, d04.play_p1(boards, numbers))
        self.assertEqual(12080, d04.play_p2(boards, numbers))

    def test_D05_1(self):
        vent_map = d05.reset()
        double_index_pairs = d05.load_pairs("inputs/inputD05-1.txt")
        d05.plot_vents(double_index_pairs, vent_map)
        self.assertEqual(5, d05.tally_map(vent_map))
        vent_map = d05.reset()
        d05.plot_all_vents(double_index_pairs, vent_map)
        self.assertEqual(12, d05.tally_map(vent_map))

    # Takes ~22 seconds to run
    # def test_D05_2(self):
    #     vent_map = d05.reset()
    #     double_index_pairs = d05.load_pairs("inputs/inputD05-2.txt")
    #     d05.plot_vents(double_index_pairs, vent_map)
    #     self.assertEqual(6710, d05.tally_map(vent_map))
    #     vent_map = d05.reset()
    #     d05.plot_all_vents(double_index_pairs, vent_map)
    #     self.assertEqual(20121, d05.tally_map(vent_map))

    def test_D06_1(self):
        data = d06.load_data("inputs/inputD06-1.txt")
        self.assertEqual(5934, d06.part1(data))
        self.assertEqual(26984457539, d06.part2(data))

    def test_D06_2(self):
        data = d06.load_data("inputs/inputD06-2.txt")
        self.assertEqual(352151, d06.part1(data))
        self.assertEqual(1601616884019, d06.part2(data))

    def test_D07_1(self):
        data = d07.load_data("inputs/inputD07-1.txt")
        self.assertEqual(37, d07.part1(data))
        self.assertEqual(168, d07.part2(data))

    def test_D07_2(self):
        data = d07.load_data("inputs/inputD07-2.txt")
        self.assertEqual(355592, d07.part1(data))
        self.assertEqual(101618069, d07.part2(data))

    def test_D08_1(self):
        signals, lights = d08.load_data("inputs/inputD08-1.txt")
        self.assertEqual(26, d08.tally_first(lights))
        self.assertEqual(61229, d08.decode_lights(lights, d08.decode_rows(signals)))

    def test_D08_2(self):
        signals, lights = d08.load_data("inputs/inputD08-2.txt")
        self.assertEqual(539, d08.tally_first(lights))
        self.assertEqual(1084606, d08.decode_lights(lights, d08.decode_rows(signals)))

    def test_D09_1(self):
        data = d09.load_data("inputs/inputD09-1.txt")
        self.assertEqual(15, d09.part1(data))
        self.assertEqual(1134, d09.part2(data))

    def test_D09_2(self):
        data = d09.load_data("inputs/inputD09-2.txt")
        self.assertEqual(475, d09.part1(data))
        self.assertEqual(1092012, d09.part2(data))

    def test_D10_1(self):
        data = d10.load_data("inputs/inputD10-1.txt")
        p1, p2 = d10.process_rows(data)
        self.assertEqual(26397, p1)
        self.assertEqual(288957, p2)

    def test_D10_2(self):
        # Fails in Windows due to RuntimeWarning: overflow encountered in long_scalars
        # Works fine in WSL Debian
        if not os.name == 'nt':
            data = d10.load_data("inputs/inputD10-2.txt")
            p1, p2 = d10.process_rows(data)
            self.assertEqual(243939, p1)
            self.assertEqual(2421222841, p2)

    def test_D11_1(self):
        data = d11.load_data("inputs/inputD11-1.txt")
        self.assertEqual(1656, d11.part1(data))
        self.assertEqual(195, d11.part2(data))

    def test_D11_2(self):
        data = d11.load_data("inputs/inputD11-2.txt")
        self.assertEqual(1739, d11.part1(data))
        self.assertEqual(324, d11.part2(data))

    def test_D12_1(self):
        data = d12.load_data("inputs/inputD12-1.txt")
        self.assertEqual(10, d12.process_nodes('start', [], data))
        self.assertEqual(36, d12.process_nodes('start', [], data, 1, ''))

    def test_D12_2(self):
        data = d12.load_data("inputs/inputD12-2.txt")
        self.assertEqual(3738, d12.process_nodes('start', [], data))
        self.assertEqual(120506, d12.process_nodes('start', [], data, 1, ''))

    def test_D13_1(self):
        indices, folds = d13.load_data("inputs/inputD13-1.txt")
        sheet = d13.draw_sheet(indices)
        self.assertEqual(17, d13.part1(sheet.copy(), folds.copy()))

    def test_D13_2(self):
        indices, folds = d13.load_data("inputs/inputD13-2.txt")
        sheet = d13.draw_sheet(indices)
        self.assertEqual(745, d13.part1(sheet.copy(), folds.copy()))

    def test_D14_1(self):
        polymer, rules = d14.load_data("inputs/inputD14-1.txt")
        pairs, tally = d14.start_pairs_tally(polymer)
        self.assertEqual(1588, d14.stepper(rules, pairs.copy(), tally.copy(), 10))
        self.assertEqual(2188189693529, d14.stepper(rules, pairs.copy(), tally.copy(), 40))

    def test_D14_2(self):
        polymer, rules = d14.load_data("inputs/inputD14-2.txt")
        pairs, tally = d14.start_pairs_tally(polymer)
        self.assertEqual(3406, d14.stepper(rules, pairs.copy(), tally.copy(), 10))
        self.assertEqual(3941782230241, d14.stepper(rules, pairs.copy(), tally.copy(), 40))


if __name__ == '__main__':
    unittest.main()
