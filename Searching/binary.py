#Binary Search
#Requires a sorted array of data
#Method - Assume the correct element is in the middle of the structure, if incorrect compare
#         the selected element to the desired element and continue search accordingly
#O(n) - log(n)


def binary_search(lst, item):
	low = 0
	high = len(list)-1

	while low <= high:
		mid = (low + high)/2
		guess = lst[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

