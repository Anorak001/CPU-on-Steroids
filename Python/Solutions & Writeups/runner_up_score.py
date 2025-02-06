# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up. (duplicates exist in the given array )
# first input is array size
# second input is array elements
# output should be runnner up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_set = set(arr)  # Remove duplicates
    sorted_list = sorted(new_set, reverse=True)  # Sort in descending order
    print(sorted_list[1])  # Print the second largest element
  
