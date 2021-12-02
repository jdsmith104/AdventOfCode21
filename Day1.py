class FileParser:
    def __init__(self):
        self.file_data = list()

    def open(self, path):
        with open(path+".txt") as f:
            for data in f:
                self.file_data.append(int(data))
        return self.file_data

class AdventOfCode:
    def __init__(self, input: list) -> None:
        self.input = input

class Day1(AdventOfCode):
    def __init__(self, input: list) -> None:
        super(Day1, self).__init__(input)
        self.input_len = len(input)
    def solve_1(self):
        increased = 0
        for i in range(1, self.input_len):
            depth = self.input[i]
            previous_depth = self.input[i-1]
            if depth > previous_depth:
                increased +=1
        print("Increased:", increased)

    def solve_2(self):
        increased = 0
        preivous_depth_sum = self.get_sum_to(2)
        for i in range(3, self.input_len, 1):
            depth_sum = self.get_sum_to(i)
            if depth_sum > preivous_depth_sum:
                increased +=1
            preivous_depth_sum = depth_sum
        print("Increased:", increased)

    # Returns the sum of the elements from index-2 to index
    def get_sum_to(self, index: int) -> int:
        assert(index < self.input_len, "Index too high")
        assert(index >= 2)
        sum = self.input[index]+self.input[index-1]+self.input[index-2]
        return sum


if __name__ == "__main__":
    file_parser = FileParser()
    input = file_parser.open("inputs/day1")
    day1 = Day1(input)
    day1.solve_2()    

    
