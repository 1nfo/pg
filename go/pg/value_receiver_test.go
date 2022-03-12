package pg

import "testing"

func TestX(t *testing.T) {
	x := X{"abcdefghik", 1}

	if x.copy() != 11 {
		t.Errorf("Not equal %d != 10", x.copy())
	}
}

func BenchmarkXCopy(b *testing.B) {
	for i := 0; i < b.N; i++ {
		X{"abcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghik", 1}.copy()
	}
}

func BenchmarkXRef(b *testing.B) {
	for i := 0; i < b.N; i++ {
		(&X{"abcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghikabcdefghik", 1}).ref()
	}
}
