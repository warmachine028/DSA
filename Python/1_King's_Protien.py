"""
CODE 7:
It’s been a month since Acland has won a war against their enemies. The country is still recovering from the damage that
war has caused to its infrastructure.Emperor of Acland who fought bravely to save his country from the enemies is now
facing severe health issues. Emperor is suffering from protein deficiency. His doctor has advised him to consume
strictly and exactly X grams of protein in a day. Now being the royal chef it’s your duty to fulfill the nutritional
needs of the Emperor. Before planning today’s menu for him you need to check out food stocks and figure out whether you
can achieve X grams of protein. You are given an array consisting of N items where i−th element is the amount of protein
 present in that particular item. You can combine any number of food items together to achieve the required amount of
 protein. If you are able to fulfill today’s nutritional needs of the Emperor print 1 else print 0.

Input Format
The first line contains an integer T (Number of Testcases). Then T test cases follow.
First line of a test case contains two space-separated integers N (number of items) and X (required amount of protein).
Second line of a test case contains N items where Ai item is the amount of protein present in that particular item.
Output Format
For each testcase, Print a single integer 0 or 1.

Constraints
1≤T≤20
1≤N≤100
1≤X≤105
1≤Ai≤100
Sample Input 1
3
4 8
2 4 6 1
5 9
3 5 1 2 3
6 4
1 5 8 9
Sample Output 1
1
1
0
"""


def kings_protein(n: int, arr: list[int]) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    for item in arr:
        remainder = n - item
        x = list(arr)
        x.remove(item)
        if kings_protein(remainder, x):
            return 1
    return 0


for TEST_CASE in range(int(input())):
    _, protein = map(int, input().split())
    print(kings_protein(protein, list(map(int, input().split()))))
