def calculate_moose_age(input_str: str):
    """
    Returns a mooses aproximate age
    """
    split_input = input_str.split(' ')
    l = int(split_input[0])
    r = int(split_input[1])
    if l < 0 or r < 0:
        return "Not a moose"
    if l == r:
        if l == 0:
            return "Not a moose"
        return "Even {}".format(l * 2)
    if l >= r:
        return "Odd {}".format(2 * l)
    return "Odd {}".format(2 * r)

def test_samples():
    sample_input = ['2 3', '3 3', '0 0']
    sample_output = ['Odd 6', 'Even 6', 'Not a moose']

    for i, sample in enumerate(sample_input):
        res = calculate_moose_age(sample)
        print(res)
        if res != sample_output[i]:
            print("failed {}".format(i))
            break
    print("tests finished successfully")


if __name__ == "__main__":
    print(calculate_moose_age(input()))
