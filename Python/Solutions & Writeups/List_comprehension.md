![image](https://github.com/user-attachments/assets/db1aefa3-7557-4fb6-a1ed-2bfa2ce35f2d)


```python3
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    combs = []
    # Directly create a list of lists
    lists = [[a, b, c] for a in range(x + 1)
                         for b in range(y + 1)
                         for c in range(z + 1)
                         if a + b + c != n]
    print(lists)


```
