class Solution(object):
    """
        使用并查集解决
        就本题而言，DFS的效率可能更高
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        father = []
        count = 0
        for i in range(m*n):
            father.append(i)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    if j+1 < n and grid[i][j+1] == '1':
                        count = self.union(father,i*n+j,i*n+j+1,count)
                    if j > 0 and grid[i][j-1] == '1':
                        count = self.union(father,i*n+j,i*n+j-1,count)
                    if i+1 < m and grid[i+1][j] == '1':
                        count = self.union(father,i*n+j,(i+1)*n+j,count)
                    if i > 0 and grid[i-1][j] == '1':
                        count = self.union(father,i*n+j,(i-1)*n+j,count)
        return count
    
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