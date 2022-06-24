class Progression:
    def __init__(self,start=0):
        self._current = start
    
    def _advance(self):
        self._current +=1
    
    def __next__(self):
        if self._current is None:
            StopIteration()
        val = self._current
        self._advance()
        return val
    
    def __iter__(self):
        return self
    
    def print_progression(self,n):
        print(' '.join(str(next(self)) for idx in range(n)))

prog = Progression()
prog.print_progression(10)
class ArithemeticProgression(Progression):
    def __init__(self, start=0, commondif=1):
        super().__init__(start)
        self.__commondif = commondif
    
    def _advance(self):
        self._current += self.__commondif

ap = ArithemeticProgression(0,2)
ap.print_progression(10)