
data = {"검암경서동": "gumam", "연희동": "yeonhi", "청라1동": "cheongna1", "청라3동": "cheongna3", "청라2동": "cheongna2", "가정1동": "gajeong1", "가정2동" :",gajeong2" , "가정3동" : "gajeong3", "신현원창동" : "sinhyun", "석남1동" :"seoknam1", "석남2동" : "seoknam2", "석남3동" : "seoknam3" , "가좌1동" :"gajwa1", "가좌2동" :"gajwa2" , "가좌3동" : "gajwa3" , "가좌4동" :"gajwa4", "검단동" :"gumdan1", "불로대곡동" :"gumdan2","원당동":"gumdan3", "당하동":"gumdan4","마전동":"majeon", "오류왕길동":"gumdan5"}

def get_bigram(string):
    s = string.replace(' ', '')
    return [s[i:i+2] for i in range(len(string)-1)]


def get_similarity(str1, str2):
    pair1 = get_bigram(str1)
    pair2 = get_bigram(str2)
    union = len(pair2)+len(pair1)
    hit_count = 0
    for x in pair1:
        for y in pair2:
            if x == y:
                hit_count += 1
                break
    return (2.0 * hit_count) / union


def pop_all(lists):
    while(len(lists) > 0):
        lists.pop()


def most_similar_list(string):
    maximum = 0
    previous = 0
    stack = []
    for key, value in data:
        if maximum < get_similarity(key, string):
            maximum = get_similarity(key, string)
        if previous < maximum:
            pop_all(stack)
            stack.append({string: value})
        if previous == maximum:
            stack.append({string: value})
        previous = get_similarity(string, stack[-1][key])
        ''' 이전에 위치한 similarity 값을 previous에,
        현재 위치한 값의 similarity를 stack에 넣으면서 previous > current_simil 이라면 pass,
        previous==current_simil라면 append,
        previous < current_simil이라면 pop all and append
        '''
    return stack