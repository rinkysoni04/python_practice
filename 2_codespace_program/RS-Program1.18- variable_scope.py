a = 25.5
b = [1, 2, 3]
c = "random_global"

def percentage(n):
    c = "random.local"
    answer = ((n/100)*100)
    return answer

result = percentage(a)
print(result)
print(a)
print(c)
print(type(b))
