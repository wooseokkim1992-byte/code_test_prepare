def build_lps(pattern):
    lps = [0]* len(pattern)
    length =0
    i=1
    while i<len(pattern):
        if pattern[i]==pattern[length]:
            length+=1
            lps[i]=length;
            i+=1
        else:
            if length !=0:
                length = lps[length-1]
            else :
                lps[i]=0
                i+=1
    return lps

    
def solution(str1, str2):
    answer = 0
    lps = build_lps(str2)
    i=0
    j=0
    while i<len(str1):
        if str1[i]==str2[j]:
            i+=1
            j+=1
            if j==len(str2):
                return 1
        else:
            if j>0:
                j=lps[j-1]
            else:
                i+=1
        
    return 2