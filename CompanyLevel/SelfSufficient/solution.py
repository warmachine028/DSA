class Solution:
    @staticmethod
    def solution(earnings, costs):
        for i, earning in enumerate(earnings):
            costs[i] -= earning
        print(sum(costs))


n = int(input())
earnings = list(map(int, input().split()))
costs = list(map(int, input().split()))
Solution.solution(earnings, costs)


# buy 1st book ($5) -> -$1 borrow it
# buy 2nd book ($3) -> $1
# buy 3rd Book ($4) -> -$2 borrow it
