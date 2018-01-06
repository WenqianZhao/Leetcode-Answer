class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m == 0 or n == 0:
            return 0
        k = len(positions)
        if k == 0:
            return 0
        father = []
        ret = []
        grid = []
        count = 0
        for i in range(m*n):
            father.append(i)
            grid.append(0)
        for i in range(k):
            x = positions[i][0]
            y = positions[i][1]
            grid[x*n+y] = 1
            count += 1
            if y+1 < n and grid[x*n+y+1] == 1:
                count = self.union(father,x*n+y,x*n+y+1,count)
            if y > 0 and grid[x*n+y-1] == 1:
                count = self.union(father,x*n+y,x*n+y-1,count)
            if x+1 < m and grid[(x+1)*n+y] == 1:
                count = self.union(father,x*n+y,(x+1)*n+y,count)
            if x > 0 and grid[(x-1)*n+y] == 1:
                count = self.union(father,x*n+y,(x-1)*n+y,count)
            ret.append(count)
        return ret
    
    def find(self,father,a):
        if father[a] == a:
            return a
        else:
            father[a] = self.find(father,father[a])
            return father[a]
        
    def union(self,father,a,b,count):
        root_a = self.find(father,a)
        root_b = self.find(father,b)
        if root_a != root_b:
            father[root_a] = root_b
            count -= 1
        return count