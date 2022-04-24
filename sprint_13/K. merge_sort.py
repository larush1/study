def merge_sort(arr, left, right):
    if left >= right:
        return
    mid = (left + right)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr, left, mid+1, right+1)


def merge(arr, left, mid, right):
	left_sub = arr[left:mid]
	right_sub = arr[mid:right]
	# result = [None] * len(array)
	l, r = 0, 0
	k = left
	while l < len(left_sub) and r < len(right_sub):
		if left_sub[l] <= right_sub[r]:
			arr[k] = left_sub[l]
			l += 1
		else:
			arr[k] = right_sub[r]
			r += 1
		k += 1
	while l < len(left_sub):
		arr[k] = left_sub[l]
		l += 1
		k += 1
	while r < len(right_sub):
		arr[k] = right_sub[r]
		r += 1
		k += 1
	return arr






# def test():
# 	a = [1, 4, 9, 2, 10, 11]
# 	b = merge(a, 0, 3, 6)
# 	expected = [1, 2, 4, 9, 10, 11]
# 	print(b)
# 	assert b == expected
# 	c = [1, 4, 2, 10, 1, 2]
# 	merge_sort(c, 0 , 6)
# 	expected = [1, 1, 2, 2, 4, 10]
# 	print(c)
# 	assert c == expected

# test()

array = [9,3,7,5,2]

print(merge_sort(array, 0, 5))
