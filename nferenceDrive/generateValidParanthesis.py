def generateParenthesis(n):
    res = []
    curr = []

    def backtrack(open, close):
        if open == close == n:
            res.append("".join(curr))

        if open < n:
            curr.append("(")
            backtrack(open + 1, close)
            curr.pop()
        
        if close < open:
            curr.append(")")
            backtrack(open, close + 1)
            curr.pop()
    backtrack(0,0)
    return res
