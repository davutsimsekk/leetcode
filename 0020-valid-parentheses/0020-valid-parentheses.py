class Solution:
    def isValid(self, s: str) -> bool:
        if s.count("(")!=s.count(")") or s.count("[")!=s.count("]") or s.count("{")!=s.count("}"):
            return(False)
        else:
            hash_map={"(":")","[":"]","{":"}"}
            currently_open=[]
            for i in s:
                if i in hash_map.keys():
                    currently_open.append(i)
                elif i in hash_map.values():
                    try:
                        if i!=hash_map[currently_open[-1]]:
                            return(False)
                        else:
                            currently_open.pop()
                    except Exception:
                        return False
            return(True)