"""
A stack can be utilized to verify if parentheses in an expression are well-matched,
i.e. every bracket has a corresponding pair. For example, parentheses in string "()[{}]"
are well-matched, while in strings "([]()", ")()[]{}", "([)]", and "[{})" they are not.

Let's break down the solution into simple steps:

We start by creating a dictionary that maps each closing bracket to its corresponding
opening bracket and an empty stack. Then, we iterate over each character paren in the string paren_string:

If paren is an opening bracket, it gets appended to the stack.
If paren is a closing bracket and the top element in the stack is the corresponding opening bracket,
we remove the top element from the stack.
If neither of the above conditions is met, we return False.
Finally, if the stack is empty (all opening brackets had matching closing brackets), we return True.
If there are some unmatched opening brackets left, we return False.

Python

"""

bracket_stack = []
bracket_dict = {
    "(": bracket_stack,
    "{": bracket_stack,
    "[": bracket_stack,
    ")": bracket_stack,
    "}": bracket_stack,
    "]": bracket_stack,
}


def balance_parens(paren_string):
    for paren in paren_string:
        if paren not in bracket_dict.keys():
            return False
        if paren in list(bracket_dict.keys())[:3]:
            bracket_dict[paren].append(paren)
        elif (
            paren in list(bracket_dict.keys())[2:]
            and bracket_dict[paren][0] == "("
            or bracket_dict[paren][0] == "{"
            or bracket_dict[paren][0] == "["
        ):
            bracket_dict.pop(0)
    for paren, stack in bracket_dict.items():
        if stack:
            return False
    return True


"""
NOTE: CODE SIGNAL SOLUTION


def is_paren_balanced(paren_string):
    stack = []
    is_balanced = True
    index = 0
    opening_paren = {')': '(', ']' : '[', '}': '{'} # a matching opening parenthesis for every closing one
    # Traversing all string characters
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            # We met an opening parenthesis, just putting it on stack
            stack.append(paren)
        else:
            # We met a closing parenthesis
            if not stack:
                # The parenthesis is closing, but there are no items in the stack
                is_balanced = False
            else:
                if stack[-1] != opening_paren[paren]:
                    # The parenthesis on top of the stack doesn't match
                    is_balanced = False
                else:
                    stack.pop()
        index += 1
    if stack:
        # If after traversing all characters, there is something left, it's bad
        is_balanced = False
    return is_balanced
"""


if __name__ == "__main__":
    balanced = "()[{}]"
    not_balanced = "([]()"
    print(balance_parens(balanced))
