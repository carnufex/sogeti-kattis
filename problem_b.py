def sort_people(names: list):
    """
    Returns list sorted by surnames, firstnames
    """
    res = []
    for surname in sorted(names, key=lambda x: (x.split()[-1], x.split()[0])):
        res.append(surname)

    return res

def clean_output(names: list):
    """
    remove surname of unique firstnames
    """
    firstnames = [x.split()[0] for x in names]
    
    # list of all names occuring two or more times
    unambiguous_names = list(set(i for i in firstnames if firstnames.count(i) > 1))
    res = []
    for name in names:
        split_name = name.split()
        firstname = split_name[0]
        surname = split_name[-1]

        if not firstname in unambiguous_names:
            # firstname is unique, disregard surname
            res.append(firstname)
        else:
            res.append(name)

    return res

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
    names = """Will Smith
Agent Smith
Peter Pan
Micky Mouse
Minnie Mouse
Peter Gunn"""

    sorted_surnames = sort_people(names)
    result = clean_output(sorted_surnames)
    return list_as_new_line_stings(result)



if __name__ == "__main__":
    # print(test())
    print(list_as_new_line_stings(clean_output(sort_people(read_input()))))
