import io

def list_as_new_line_stings(input: list):
    return "\n".join([i for i in input])


def read_input():
    data = []
    while True:
        try:
            data.append(input())
        except EOFError:
            break

    return data


def test():
    msg = """def foo 3
calc foo + bar =
def bar 7
def programming 10
calc foo + bar =
def is 4
def fun 8
calc programming - is + fun =
def fun 1
calc programming - is + fun =
clear
"""
    buf = io.StringIO(msg)
    list_msg = buf.readlines()

    return problem_d(list_msg)


def calc(data: list, variables: dict):
    """
    returns the calculated input
    """
    query = ""
    res = 0
    sign = '+'
    for item in data[1:]: # offset command
        query += item + ' '
        if item in ['+', '-', '=']:
            sign = item
        else:
            try:
                if type(res) is not int:
                    continue
                if sign == '+':
                    res += int(variables[item])
                if sign == '-':
                    res -= int(variables[item])
            except KeyError:
                    res = 'unknown'

    if type(res) is int:
        try:
            res = [k for k, v in variables.items() if v == str(res)]
            if len(res) == 0:
                res = 'unknown'
            else:
                res = res[0]
        except KeyError:
            res = 'unknown'

    return query + str(res)  


def problem_d(data: list):
    """
    returns solution for problem d in list format
    """
    output = []
    variables = {}

    for line in data:
        line = line.split()
        command = line[0]
        if command == 'def':
            variables[line[1]] = line[2]
        if command == 'calc':
            output.append(calc(line, variables))
        if command == 'clear':
            variables.clear()
    return output 

        
if __name__ == "__main__":
    # print(test())
    print(list_as_new_line_stings(problem_d(read_input())))
