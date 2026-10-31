n, m = map(int, input().split())
shopping_list = set(input().split())
for line in range(n-1):
    shopping_list.intersection_update(set(input().split())) 

print(len(shopping_list))
for item in sorted(shopping_list):
    print(item)