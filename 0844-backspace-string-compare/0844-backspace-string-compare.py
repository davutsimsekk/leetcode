class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack=[]
        t_stack=[]

        for i in range(len(s)):
            if s[i]!="#":
                s_stack.append(s[i])
            elif s[i]=="#":
                if len(s_stack)!=0:
                    s_stack.pop()
        print(s_stack)
        for i in range(len(t)):
            if t[i]!="#":
                t_stack.append(t[i])
            elif t[i]=="#":
                if len(t_stack)!=0:
                    t_stack.pop()
        print(t_stack)
        return(t_stack==s_stack)