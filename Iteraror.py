class Sequence:
    def __init__(self,elements=1):
        self._seq = [0]*elements
        self._currIdx = -1
    
    def __len__(self):
        return len(self._seq)
    
    def __setitem__(self,k,val):
        #print(k)
        self._seq[k] = val
        
    def __getitem__(self,j):
        if j > len(self._seq):
            raise IndexError("Index out of range")
        return self._seq[j]
    
    def __next__(self):
        self._currIdx +=1
        if self._currIdx < len(self._seq):
            return (self._seq[self._currIdx])
        else:
            raise StopIteration("There are no more elements")
    def __iter__(self):
        return self
    
seq = Sequence(12)

for i in range(0, len(seq)-1):
    seq[i] = i*2
