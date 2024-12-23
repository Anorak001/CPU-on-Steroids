![image](https://github.com/user-attachments/assets/f0f8ae0f-62ec-4bc6-ad2a-6ff4c7d2feb7)
```python3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
```
