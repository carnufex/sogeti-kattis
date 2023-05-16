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
    msg = """12
# 8 2 4 4 3
. 1 2 4 2 2 2 6 1 1
. 1 2 5 2 1 2 6 1 1
. 1 2 5 1 2 2 6 1 1
. 1 2 4 2 2 2 6 1 1
. 1 7 3 2 6 1 1
. 1 2 4 2 2 2 6 1 1
. 1 2 5 2 1 2 6 1 1
. 1 2 5 2 2 2 5 1 1
. 1 2 5 2 2 2 4 2 1
. 1 2 4 2 4 2 3 1 2
# 7 8 2 4
35
. 11 7 12
. 10 10 10
. 10 10 10
. 9 12 9
. 9 12 9
. 9 12 9
. 9 12 9
. 9 12 9
. 9 4 1 7 9
. 9 2 5 5 9
. 10 12 8
. 10 12 8
. 9 7 2 5 7
. 8 3 1 3 3 6 6
. 7 3 9 5 7
. 7 3 9 6 5
. 6 4 9 7 4
. 6 4 10 6 4
. 5 4 11 7 3
. 5 4 12 6 3
. 4 4 13 6 3
. 4 4 13 6 3
. 4 4 13 6 3
. 4 4 13 6 3
. 4 4 12 7 3
. 3 1 2 3 11 8 2
# 4 3 4 9 8 2
# 4 4 4 8 1 5 2 2
# 2 6 4 7 2 6 3
# 2 7 3 6 3 7 2
# 2 8 3 3 5 7 2
# 1 9 11 5 4
# 4 6 11 3 4 2
. 1 25 4
. 5 6 8 6 5
0"""
    buf = io.StringIO(msg)
    list_msg = buf.readlines()
    # return decode_image(list_msg)
    return decode_image(parse_input(list_msg))


def toggle(x):
    """
    Toggles the "bit"
    """
    return '#' if x == '.' else '.'


def parse_input(input_list:list):
    """
    Returns a parsed list of tuples (image: list, size: int)
    """
    images = []
    image_sizes = []
    partial_image = []
    for row in input_list:
        split_row = row.split()
        sign = split_row[0]
        if sign in ['#', '.']:
            partial_image.append(split_row)
        else:
            if len(partial_image) > 0:
                images.append((partial_image, image_sizes[-1]))
                partial_image = []
            if sign != '0':
                image_sizes.append(sign)

    return images 


def decode_image(images: list):
    """
    Decodes a parsed list of tuples to output images
    """
    output = []
    symbol = None

    for tup in images:
        # for each image
        has_error = False
        image_rows = tup[0]
        image_height = tup[1]
        previous_width = None

        if len(image_rows) != int(image_height):
            has_error = True
  
        for i, y in enumerate(image_rows):
            # for each image row
            col = []
            symbol = y[0]
            for x in y[1:]:
                # for each image col
                try:
                    x = int(x)
                    col.append(symbol * x)
                    symbol = toggle(symbol)
                    new_row = "".join([i for i in col])
                except ValueError:
                    has_error = True

            if previous_width is not None and previous_width != len(new_row):
                has_error = True
            elif previous_width is None:
                previous_width = len(new_row)
            if i == int(image_height)-1:
                if has_error:
                    new_row += "\nError decoding image"
                new_row += "\n"
            output.append(new_row)

    res = list_as_new_line_stings(output)
    
    return res[:-1] # removing empty line to satisfy test criteria
        
if __name__ == "__main__":
    # print(test())
    print(decode_image(parse_input(read_input())))
