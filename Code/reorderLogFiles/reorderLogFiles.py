"""
제약 조건
1. 로그에 대해 첫 번째 단어는 문자와 숫자를 식별하는 식별자이다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다. 
"""

from typing import List

class Solution:
    def reorderLogFiles(self, logs:List[str])->List[str]:
        letters = list()
        digits = list()

        for log in logs:
            # isdigit()함수를 사용하여 log값의 첫 글자가 숫자인지 문자인지 구분해준다.
            if log.split()[1].isdigit():
                # 숫자인경우 digits리스트에 추가
                digits.append(log)
            else:
                # 문자인경우 letters리스트에 추가
                letters.append(log)

        # 람다식을 사용
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters+digits

def main():
    logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

    solution = Solution()

    print(solution.reorderLogFiles(logs))


if __name__ == "__main__":
    main()