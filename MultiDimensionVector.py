class MultiVector:
    def __init__(self,d):
        self._coord = [0]*d
    
    def __len__(self):
        return len(self._coord)

    def __add__(self, other):
        print("Hi this is addition")
        if len(self) != len(other):
            raise ValueError("Dimensions must be same")
        mv = MultiVector(len(self))
        for i in range(len(mv)):
            mv[i] = self[i] + other[i]
        return mv
    
    def __setitem__(self, j, val):
        if j > len(self._coord):
            raise IndexError("Index out of bound")
        self._coord[j] = val
    
    def __getitem__(self, j):
        if j > len(self._coord):
            raise IndexError("Index out of bound")
        return self._coord[j]
    
    def __eq__(self, other):
        return self._coord == other._coord
    
    def __ne__(self , other):
        return not self == other

  



mv = MultiVector(6)
mv[0]=1
for i in range(len(mv)-1):
    mv[i] = i
mv2 = MultiVector(6)
for j in range(len(mv2)-1):
    mv2[j]=j
print(mv!=mv2)

