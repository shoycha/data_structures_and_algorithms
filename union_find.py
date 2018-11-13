class U(object):
    
    def __init__(self, n):
        self.id = [ i for i in range(n)]

    def __str__(self):

        return " ".join(str(e) for e in self.id)

    def union(self, p, q):
        """
        >>> u = U(10)
        >>> print(u)
        0 1 2 3 4 5 6 7 8 9
        >>> u.union(4,3)
        >>> print(u)
        0 1 2 3 3 5 6 7 8 9
        >>> u.union(3,8)
        >>> u.union(6,5)
        >>> u.union(9,4)
        >>> u.union(2,1)
        >>> print(u)
        0 1 1 8 8 5 5 7 8 8
        """
        if self.connected( p, q):
            return
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] ==  pid:
                self.id[i] = qid

    def connected(self, p, q):
        """
        >>> u = U(10)
        >>> u.union(4,3)
        >>> u.union(3,8)
        >>> u.union(6,5)
        >>> u.union(9,4)
        >>> u.union(2,1)
        >>> u.connected(8,9)
        True
        >>> u.connected(5,0)
        False
        >>> u.union(5,0)
        >>> print(u)
        0 1 1 8 8 0 0 7 8 8
        >>> u.union(7,2)
        >>> print(u)
        0 1 1 8 8 0 0 1 8 8
        >>> u.union(6,1)
        >>> print(u)
        1 1 1 8 8 1 1 1 8 8
        """
        return self.id[p] == self.id[q]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
