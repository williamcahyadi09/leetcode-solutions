class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = deque()
        operator_stack = deque()

        len_expression = len(expression)
        operator_list = ["!", "&", "|"]

        def parse_bool(c: str) -> bool:
            if c == "f":
                return False
            return True

        def run_operation(operation: str, exp1: Optional[bool], exp2: Optional[bool]):
            if exp2 is None:
                if operation == "&" or operation == "|":
                    return exp1
                return not exp1

            if operation == "&":
                return exp1 and exp2
            if operation == "|":
                return exp1 or exp2

        def reverse_map_exp(exp: bool):
            if exp:
                return "t"
            return "f"

        for i in range(len_expression):
            if expression[i] == ")":
                # print("stack : ", stack)
                # print("operator_stack : ", operator_stack)
                temp_expression = None
                only_one = True
                curr_operator = operator_stack.pop()
                # print("curr_operator : ", curr_operator)
                while(stack and stack[-1]!="("):
                    curr_char = stack.pop()
                    if curr_char != "f" and curr_char != "t":
                        continue

                    curr_expression = parse_bool(curr_char)
                    # print("curr_expression : ", curr_expression)
                    if temp_expression is None:
                        temp_expression = curr_expression
                        continue
                    
                    only_one = False
                    temp_expression = run_operation(curr_operator, temp_expression, curr_expression)

                if only_one:
                    temp_expression = run_operation(curr_operator, temp_expression, None)

                stack.pop()
                stack.append(reverse_map_exp(temp_expression))
                # print("stack after operation : ", stack)
                # print()
                continue
                
            if expression[i] in operator_list:
                operator_stack.append(expression[i])
            else:
                stack.append(expression[i])

        return parse_bool(stack[0])
        