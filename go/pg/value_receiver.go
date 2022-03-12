package pg

type X struct {
	name string
	id   int
}

func (x X) copy() int {
	return len(x.name) + x.id
}

func (x *X) ref() int {
	return len(x.name) + x.id
}
