func twoSum(nums []int, target int) []int {
    ht := make(map[int] int)

	for i,v := range nums {
		lack := target - v

		j , ok := ht[v]
		if ok {
			return []int{j, i}
		} else {
			ht[lack] = i
		}
	}
	return nil
}