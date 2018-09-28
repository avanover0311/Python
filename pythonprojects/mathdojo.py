class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, bNum, *aNum):
        self.result += bNum
        for i in range(0,len(aNum)):
            self.result += aNum[i]
        return self
    def subtract(self, bNum, *aNum):
        self.result -= bNum
        for i in range(0,len(aNum)):
            self.result -= aNum[i]
        return self

md= MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)





