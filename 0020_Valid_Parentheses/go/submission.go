func isValid(s string) bool {
	length := len(s)

	if length%2 != 0 {
		// Can't possibly have matching parentheses pairs if the string length is odd
		return false
	} else {
		stack := New()

		for i := 0; i < length; i++ {
			char := s[i]

			if char == '(' || char == '{' || char == '[' {
				stack.Push(char)
			} else {
				height := stack.Size()

				if height <= 0 {
					return false
				} else if char == ')' {
					if stack.Peek() != '(' {
						return false
					}
					stack.Pop()
				} else if char == '}' {
					if stack.Peek() != '{' {
						return false
					}
					stack.Pop()
				} else if char == ']' {
					if stack.Peek() != '[' {
						return false
					}
					stack.Pop()
				}
			}
		}

		if stack.Size() > 0 {
			return false
		} else {
			return true
		}
	}
}

type Stack struct {
	Top    *Node
	Height int
}

type Node struct {
	Value    byte
	Previous *Node
}

func New() *Stack {
	return &Stack{nil, 0}
}

func (this *Stack) Size() int {
	return this.Height
}

func (this *Stack) Peek() byte {
	if this.Height == 0 {
		return 0
	}
	return this.Top.Value
}

func (this *Stack) Pop() byte {
	if this.Height == 0 {
		return 0
	}

	n := this.Top
	this.Top = n.Previous
	this.Height--
	return n.Value
}

func (this *Stack) Push(value byte) {
	n := &Node{value, this.Top}
	this.Top = n
	this.Height++
}