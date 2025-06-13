class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels=['a','e','i','o','u','A',"E","I","O","U"]
        indexList=[] # index of each of the vowels
        vowelIndexList=[] # which values of the vowels
        for index,content in enumerate(s):
            if content in vowels:
                indexList.append(index)
                vowelIndexList.append(vowels.index(content))
        vowelIndexList.reverse()
        # begin replacing values
        for index,content in enumerate(indexList):
            s[content]=vowels[vowelIndexList[index]]

        #convert back to string
        return ''.join(s)
        
