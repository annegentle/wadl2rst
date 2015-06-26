
import copy
import re

SPLIT_DELIMITERS = re.compile(r"-|/| |_")
START_DELIMITER = "| "
END_DELIMITER = " |"
SEPERATOR = " | "


def create_table(columns, data):
    """ Given a set of columns, and some data rows, output a properly formatted
    rST table. :( """

    # split strings into arrays sanely
    data = split_all_values(data)

    # assign each column space based on its size
    column_sizes = calculate_column_sizes(columns, data)

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


def calculate_column_sizes(columns, rows):
    """ Based on the columns and their names, split the spaces reasonably evenly.
    TODO: this doesn't handle when the column space is smaller than the titles."""

    markup_length = (len(columns) - 1) * len(SEPERATOR) + len(START_DELIMITER) + len(END_DELIMITER)
    column_space = 80 - markup_length
    column_sizes = []

    # grab the base column sizes
    for idx, column in enumerate(columns):
        column_sizes.append(len(column))

    # bump out any columns as necessary
    for row in rows:
        for idx, words in enumerate(row):
            if len(words) > 0:
                max_word_size = len(max(words))
                if max_word_size > column_sizes[idx]:
                    column_sizes[idx] = max_word_size

    taken_space = sum(column_sizes)

    if sum(column_sizes) > column_space:
        raise Exception("can't fit without splitting.")

    for idx in range(column_space - taken_space):
        column_sizes[idx % len(columns)] += 1

    return column_sizes


def formatted_row(column_sizes, row):
    """ Given a row and specified column sizes, return a properly formatted row.
    TODO: this may eventually want to try to split on spaces instead of just
    wherever. """

    output = []
    row_state = copy.deepcopy(row)

    # if number of elements in the row are less than the number of columns,
    # then append the row with spaces
    if len(row_state) < len(column_sizes):
        for space in range(len(column_sizes) - len(row_state)):
            row_state.append('')

    while characters_left_in_row(row_state):
        # the current row we're messing with
        current_row = []
        next_state = []

        for column_size, cell in zip(column_sizes, row_state):
            # pull at most column_size characters from the cell, stashing the
            # rest for later
            text, rest = split_sentence(column_size, cell)
            next_state.append(rest)

            # append exactly column_size characters from cell, padding if necessary
            fmt = "{:<" + str(column_size) + "}"
            data = fmt.format("".join(text))
            current_row.append(data)

        # return the current row in text
        output.append(START_DELIMITER + SEPERATOR.join(current_row) + END_DELIMITER)
        row_state = next_state

    return output


def split_all_values(rows):
    """ Loop over all cells in the table, tokenizing the strings contained therein."""

    output = []

    for row in rows:
        new_row = []

        for cell in row:
            cell = split_cell_values(cell)
            new_row.append(cell)

        output.append(new_row)

    return output


def split_cell_values(cell):
    """ Split the cell into chunks, including the delimiters."""

    start = 0
    output = []

    cell = cell.strip()

    for match in SPLIT_DELIMITERS.finditer(cell):
        end = match.end()
        output.append(cell[start:end])
        start = end

    if start < len(cell):
        output.append(cell[start:])

    return output

def split_sentence(column_size, cell):
    """ Return enough words to fill the column."""

    # if the total cell sizes are smaller the the column size, just return it
    if len("".join(cell)) <= column_size:
        return (cell, [])

    output = []

    for word in cell:
        if is_output_plus_word_ok(column_size, output, word):
            output.append(cell.pop(0))
        else:
            break

    return (output, cell)


def is_output_plus_word_ok(column_size, output, word):
    data = copy.deepcopy(output)
    data.append(word)
    new = "".join(data)
    return len(new) < column_size


def row_line(column_sizes, character="-"):
    """Create a line, with the little pluses where they belong."""

    output = []
    for size in column_sizes:
        output.append(character * (size + 2))

    return "+" + "+".join(output) + "+"


def characters_left_in_row(row):
    """ Given a modified row, are there items left to print? """

    items = ["".join(item) for item in row]
    chars_left = "".join(items)
    return len(chars_left) > 0
