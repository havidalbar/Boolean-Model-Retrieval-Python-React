import re

def infix_to_postfix(query):
	list_operator = ['(', ')', 'or', 'and', 'not']
	priority_operator = [0, 0, 1, 2, 3]
	operator_stack = []
	postfix = []
	precedence = {}
	for i in range(len(list_operator)):
		precedence[list_operator[i]] = priority_operator[i]

	list_token = re.findall(r"([a-zA-Z]+|\(|\))", query)
	for token in list_token:
		if token not in precedence:
			postfix.append(token)
		elif token == '(':
			operator_stack.append(token)
		elif token == ')':
			head = operator_stack.pop()
			while head != '(':
				postfix.append(head)
				head = operator_stack.pop()
		else:
			while len(operator_stack) > 0 and (precedence[operator_stack[-1]] >= precedence[token]):
				postfix.append(operator_stack.pop())
			operator_stack.append(token)

	while len(operator_stack) > 0:
		postfix.append(operator_stack.pop())
	return postfix

