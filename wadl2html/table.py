
import copy


START_DELIMITER = "| "
END_DELIMITER = " |"
SEPERATOR = " | "


def create_table(columns, data):
    """ Given a set of columns, and some data rows, output a properly formatted
    rST table. :( """

    # assign each column space based on its size
    column_sizes = calculate_column_sizes(columns)

    rows = []

    # create the header
    rows.append(row_line(column_sizes))
    rows.extend(formatted_row(column_sizes, columns))
    rows.append(row_line(column_sizes, "="))

    # handle the rows
    for row in data:
         rows.extend(formatted_row(column_sizes, row))
         rows.append(row_line(column_sizes))

    return "\n" + "\n".join(rows) + "\n"


def calculate_column_sizes(columns):
    """ Based on the columns and their names, split the spaces reasonably evenly.
    TODO: this doesn't handle when the column space is smaller than the titles."""

    column_space = 80 - (
        (len(columns) - 1) * len(SEPERATOR) + len(START_DELIMITER) + len(END_DELIMITER))
    text_size = len(''.join(columns))
    column_sizes = []

    if text_size > column_space:
        raise Exception("Headers bigger than available space!")

    # fill out the base sizes
    for column in columns:
        column_sizes.append(len(column))

    for i in range(column_space - text_size):
        column = i % len(columns)
        column_sizes[column] += 1

    return column_sizes


def formatted_row(column_sizes, row):
    """ Given a row and specified column sizes, return a properly formatted row.
    TODO: this may eventually want to try to split on spaces instead of just
    wherever. """

    output = []
    row_state = copy.deepcopy(row)

    while characters_left_in_row(row_state):
        # the current row we're messing with
        current_row = []
        next_state = []

        for column_size, cell in zip(column_sizes, row_state):
            # pull at most column_size characters from the cell, stashing the
            # rest for later
            text, rest = split_sentence(column_size, cell.strip())
            next_state.append(rest)

            # append exactly column_size characters from cell, padding if necessary
            fmt = "{:<" + str(column_size) + "}"
            current_row.append(fmt.format(text))

        # return the current row in text
        output.append(START_DELIMITER + SEPERATOR.join(current_row) + END_DELIMITER)
        row_state = next_state

    return output


def split_sentence(column_size, cell):

    # if the cell is smaller than column size, just return it
    if len(cell) < column_size:
        return (cell, "")

    words = cell.split()
    output = []

    for word in words:
        if is_output_plus_word_ok(column_size, output, word):
            output.append(words.pop(0))
        else:
            break

    return (" ".join(output), " ".join(words))


def is_output_plus_word_ok(column_size, output, word):
    data = copy.deepcopy(output)
    data.append(word)
    new = " ".join(data)
    return len(new) < column_size


def row_line(column_sizes, character="-"):
    """Create a line, with the little pluses where they belong."""

    output = []
    for size in column_sizes:
        output.append(character * (size + 2))

    return "+" + "+".join(output) + "+"


def characters_left_in_row(row):
    """ Given a modified row, are there items left to print? """

    chars_left = "".join(row)
    return len(chars_left) > 0
