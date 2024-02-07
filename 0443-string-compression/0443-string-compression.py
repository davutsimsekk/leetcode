class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        flen = len(chars)

        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:

                counter += 1
            else:

                if counter != 1:
                    for j in str(counter):
                        chars.append(j)

                counter = 1

                chars.append(chars[i + 1])
            if i == flen - 2 and counter != 1:
                for j in str(counter):
                    chars.append(j)
        for i in range(flen - 1):
            chars.pop(1)
            

        
        return (len(chars))