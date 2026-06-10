class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        t = self.powerSum(n)
        while t not in nums and t != 1:
            nums.add(t)
            t = self.powerSum(t)
        if t == 1: return True
        return False
    
    def powerSum(self, n):
        cad = str(n)
        suma = 0
        for n in cad:
            digito = int(n)
            suma += digito * digito
        return suma 