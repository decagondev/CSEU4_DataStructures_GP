# recursive solution
def smallest_missing(arr, left, right):

    #base case
    if left > right:
        return left    

    middle = left + (right - left) // 2

    if arr[middle] == middle:
        return smallest_missing(arr, middle + 1, right)
    else:
        return smallest_missing(arr, left, middle - 1)

if __name__ == '__main__':
  A = [0, 1, 2, 6, 9, 11, 15]
  print(f"The smallest missing element is {smallest_missing(A, 0, len(A) - 1)}")

  A = [1, 2, 3, 4, 6, 9, 11, 15]
  print(f"The smallest missing element is {smallest_missing(A, 0, len(A) - 1)}")

  A = [0, 1, 2, 3, 4, 5, 6] 
  print(f"The smallest missing element is {smallest_missing(A, 0, len(A) - 1)}")