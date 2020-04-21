def get_bigram(string):
    s = string.replace(' ','')
    return [s[i:i+2] for i in range(len(string)-1) ]

def get_similarity(str1,str2):
    pair1 = get_bigram(str1)
    pair2 = get_bigram(str2)
    
    union = len(pair2)+len(pair1)
    hit_count = 0
    for x in pair1:
        for y in pair2:
            if x == y:
                hit_count+=1
                break
    return (2.0 * hit_count) / union

def max_similarity_chr(string,lists):
    maximum = 0 
    maximum_index = 0
    for i in lists:
        if maximum<get_similarity(string,i):
            maximum= get_similarity(string,i)
            maximum_index = i
    if maximum == 0:
        return False
    else :
        return maximum_index