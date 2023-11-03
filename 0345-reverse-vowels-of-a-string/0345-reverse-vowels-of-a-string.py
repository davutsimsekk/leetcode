class Solution:
    def reverseVowels(self, s: str) -> str:
        
        
        liste3 = []
        liste2 = []
        liste1 = []
        
        a = len(liste2) - 1
        b = 0
        vowels=("AaEeIiOoUu")
        
        for i in range(len(s)):
            liste3.append(s[i])
            if s[i] in vowels:
                liste2.append(i)
                liste1.append(s[i])

        while b < len(liste2):
            liste3[int(liste2[a])] = liste1[b]
            b = b + 1
            a = a - 1

        s = ''.join(liste3)
        print(liste1, liste2, liste3, s)
        return s

                