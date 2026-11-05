class MinStack:

    def __init__(self):
        self.arr = []
        self.minEl = []

    def push(self, val: int) -> None:
        if self.minEl == []:
            self.minEl.append(val)
        elif val <= self.minEl[-1]:
            self.minEl.append(val)

        self.arr.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.minEl[-1]:
            self.minEl.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minEl[-1]
