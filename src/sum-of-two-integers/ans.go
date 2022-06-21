package sum_of_two_integers

func getSum(a int, b int) int {
	// using half adder logic (taken from google)
	if b == 0 {
		return a
	}

	return getSum(a^b, (a&b)<<1)
}
