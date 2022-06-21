package number_of_1_bits

func hammingWeight(num uint32) int {
	var count uint32 = 0
	var i uint32
	for i = 0; i < 32; i++ {
		count += num >> i & uint32(1)
	}
	return int(count)
}
