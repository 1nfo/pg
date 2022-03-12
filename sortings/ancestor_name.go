package main

import (
	"fmt"
	"sort"
	"strings"
)

var rome2num = map[rune]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
}

type NameWrapper struct {
	fullName string
	name     string
	number   int
}

func (n NameWrapper) less(o NameWrapper) bool {
	if n.name < o.name {
		return true
	} else if o.name < n.name {
		return false
	} else {
		return n.number < o.number
	}
}

type Names []NameWrapper

func (s Names) Len() int           { return len(s) }
func (s Names) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s Names) Less(i, j int) bool { return s[i].less(s[j]) }

func parseName(s string) (string, int) {
	strs := strings.Split(s, " ")
	number := 0
	for i, c := range strs[1] {
		if i+1 < len(strs) && rome2num[c] < rome2num[[]rune(strs[1])[i+1]] {
			number -= rome2num[c]
		} else {
			number += rome2num[c]
		}
	}
	return strs[0], number
}

func sortNames(input []string) {
	names := []NameWrapper{}
	for _, s := range input {
		name, number := parseName(s)

		NameWrapper := NameWrapper{
			fullName: s,
			name:     name,
			number:   number,
		}
		names = append(names, NameWrapper)
	}

	sort.Sort(Names(names))
	for _, n := range names {
		fmt.Println(n.fullName, n.number)
	}
}

func main() {
	sortNames([]string{"Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"})
}
