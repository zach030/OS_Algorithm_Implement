import stack

# 存页的栈
page_stack = stack.Stack()
# 辅助存储的栈
tmp_stack = stack.Stack()
# 栈最大值
max_size = 3
# 待进入页list
page_list = [2, 0, 3, 0, 1, 3, 1, 2, 0, 1]

if __name__ == '__main__':
    for p in page_list:
        if page_stack.size() != max_size:
            page_stack.push(p)
            print("Current stack is:", page_stack.items)
            continue
        while page_stack.size() != 0:
            top = page_stack.pop()
            if top != p and not page_stack.is_empty():
                tmp_stack.push(top)
            else:
                break
        while tmp_stack.size() != 0:
            page_stack.push(tmp_stack.pop())
        page_stack.push(p)
        print("Current stack is:", page_stack.items)
