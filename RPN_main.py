import sys


def check_for_number(num):
    try:
        int(num)
    except:
        return False
    return True


def check_for_len(s):
    return len(s) >= 2


def check_for_starting_with_colon(s):
    if s[0] == ":":
        return True
    return False


def kill_first_digit(s):
    res = ''
    for i in range(len(s)):
        if i == 0:
            continue
        res += s[i]
    return res


stack = []
dict_of_binds = {}
stack_of_commands = sys.stdin.read().split()
stack_of_commands.reverse()
count = 0


def execute(command):
    global stack
    global stack_of_commands
    global count
    global dict_of_binds
    if check_for_number(command):
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            stack.append(int(command))
    elif command == "+":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(first + second)
    elif command == "-":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(second - first)
    elif command == "*":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(first * second)
    elif command == ".":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            print(stack.pop())
    elif command == "dup":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            new = stack.pop()
            stack.append(new)
            stack.append(new)
    elif command == "drop":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            stack.pop()
    elif command == "take":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            res = []
            find_index = stack.pop()
            index = 0
            for i in stack:
                if index == len(stack) - find_index - 1:
                    index += 1
                    element = i
                    continue
                res.append(i)
                index += 1
            res.append(element)
            stack = res
    elif command == "[":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            stack.append([])
        count += 1
    elif command == "]":
        count -= 1
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)

    elif command == "!":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            listy = []
            for i in stack.pop():
                listy.append(i)
            while listy:
                new = listy.pop()
                stack_of_commands.append(new)
    elif command == "<":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(second < first)
    elif command == ">":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(second > first)
    elif command == "<=":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(second <= first)
    elif command == ">=":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(second >= first)
    elif command == "=":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(second == first)
    elif command == "?":
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            first = stack.pop()
            second = stack.pop()
            if stack.pop():
                stack.append(second)
                stack_of_commands.append('!')
            else:
                stack.append(first)
                stack_of_commands.append('!')
    else:
        if count > 0:
            sth = stack.pop()
            sth.append(command)
            stack.append(sth)
        else:
            if check_for_starting_with_colon(command):
                if check_for_len(kill_first_digit(command)):
                    dict_of_binds[kill_first_digit(command)] = stack.pop()
                    return
            else:
                try:
                    stack.append(dict_of_binds[command])
                    stack_of_commands.append('!')
                except KeyError:
                    print('ERROR ' + command)
                    sys.exit()


while stack_of_commands:
    execute(stack_of_commands.pop())
