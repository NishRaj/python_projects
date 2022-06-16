class OddProducts:
    def __init__(self,num_seq):
        self.num_seq = num_seq
    
    def odd_product_pair(self):
        num_list = list(self.num_seq)
        odd_list = list()
        for idx in range(len(num_list)):
            if num_list[idx] % 2 !=0:
                odd_list.append(num_list[idx])
        if len(odd_list) > 1:
            return True
        return False
    
    # Time complexity is O(n)
    def is_distinct_number(self):
        num_list = list(self.num_seq)
        for i in range (len(num_list)-1):
            if num_list[i] == num_list[i+1]:
                return False
        return True               



op = OddProducts([1,1,4,5,5])
print(op.is_distinct_number())