class MyEnumerate():
    def __init__(self, data, label):
        self.data = data
        self.label = label
        self.i = 0

    def __iter__(self):
        # print("iterating")
        
        return iter(self.__next__, [3])

    def __next__(self):
        if self.i >= len(self.label):
            raise StopIteration 

        # print("next")
        self.i += 1
        return self.i-1, self.data[self.i-1], self.label[self.i-1]

def main():

    data = [[174, 63], [165, 45], [168, 61], [180, 85], [163, 52]]
    label = ['male', 'female', 'male', 'male', 'female']

    for index, info, target in MyEnumerate(data, label):
        print(f"id:{index} | height:{info[0]} weight:{info[1]} -> {target}")

    # the output should look like the following:
    # id:0 | height:174 weight:63 -> male
    # id:1 | height:165 weight:45 -> female
    # id:2 | height:168 weight:61 -> male
    # id:3 | height:180 weight:85 -> male
    # id:4 | height:163 weight:52 -> female


if __name__ == "__main__":
    main()