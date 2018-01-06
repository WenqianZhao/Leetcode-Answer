class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        a = b = c = 0
        table = [1]
        while(len(table) < n):
            next_val = min(table[a]*2,table[b]*3,table[c]*5)
            table.append(next_val)
            if table[a]*2 == next_val:
                a += 1
            if table[b]*3 == next_val:
                b += 1
            if table[c]*5 == next_val:
                c += 1
        return table[n-1]