def subList(list1 = [],  list2 = []):

	resultList = []

	for item in list1:
		if item not in list2:
			resultList.append(item)

	return resultList