func twoSum(nums []int, target int) []int {
    ht := make(map[int] int)
	result := []int{}

	for i,v := range nums {
		lack := target - v

		_, ok := ht[v]
		if ok {
			result = append(result, ht[v], i)
		} else {
			ht[lack] = i
		}
	}

	return result
}