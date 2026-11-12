func isPalindrome(s string) bool {
	r := []rune(s)

	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		if !(unicode.IsLetter(r[i]) || unicode.IsDigit(r[i])) {
			j++
			continue
        }
		if !(unicode.IsLetter(r[j]) || unicode.IsDigit(r[j])) {
			i--
			continue
        }
		fmt.Println(string(r[i]), string(r[j]))

    	if unicode.ToLower(r[i]) != unicode.ToLower(r[j]) {
        	return false
    	}
	}
	return true
}
