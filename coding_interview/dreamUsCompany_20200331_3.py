# 여러 단어들이 주어지고, 입력 받은 문자열들과 매칭되는 단어를 검색해야합니다.
# 단어의 prefix가 입력 받은 문자열과 동일할 경우, 단어와 문자열은 매칭되는 것으로 간주합니다.
# 즉, 단어들과 문자열을 입력받고 문자열과 매칭되는 모든 단어들을 반환하는 함수를 작성하십시오.
# Time complexity와 space complexity를 고려하여 최적화에 신경써주세요.
# 서비스에 사용된다면 어떻게 적용되는지를 상상하면서 작성하시면 더 좋을 것 같습니다.

# Example 1)
# Input: words=[apple, banana, pineapple], keyword=appl
# Output: [apple]
# Example 2)
# Input: words=[apple, banana, pineapple], keyword=a
# Output: [apple]
# Example 3)
# Input: words=[apple, applewatch, applekeyboard], keyword=apple
# Output: [apple, applewatch, applekeyboard]

def solution(words, keyword):
    answer = []
    k = len(keyword)
    for word in words:
        if len(word) < k: continue

        i = 0
        while i < k:
            if word[i] != keyword[i]:
                break
            i+=1

        if i == k:
            answer.append(word)
    return answer