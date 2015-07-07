
from unittest import TestCase

from nose.tools import raises

from wadl2rst import table


class TestCharactersLeftInRow(TestCase):
    """ tests for table.characters_left_in_row """

    def test_with_characters(self):
        row = ["foo", "bar", "baz"]
        output = table.characters_left_in_row(row)
        self.assertTrue(output)

    def test_with_no_characters(self):
        row = []
        output = table.characters_left_in_row(row)
        self.assertTrue(not output)

    def test_with_blank_string(self):
        row = [""]
        output = table.characters_left_in_row(row)
        self.assertTrue(not output)


class TestRowLine(TestCase):
    """ tests for table.row_line """

    def setUp(self):
        self.column_sizes = [1, 1, 1]

    def test_with_dashes(self):
        output = table.row_line(self.column_sizes)
        self.assertEquals("+-+-+-+", output)

    def test_with_equals(self):
        output = table.row_line(self.column_sizes, character="=")
        self.assertEquals("+=+=+=+", output)


class TestIsOutputPlusWordOk(TestCase):
    """ tests for table.is_output_plus_word_ok """

    def test_smaller_than_column_size(self):
        output = table.is_output_plus_word_ok(5, [""], "-" * 4)
        self.assertTrue(output)

    def test_equal_to_column_size(self):
        output = table.is_output_plus_word_ok(5, [""], "-" * 5)
        self.assertTrue(output)

    def test_greater_than_column_size(self):
        output = table.is_output_plus_word_ok(5, [""], "-" * 6)
        self.assertTrue(not output)


class TestSplitSentence(TestCase):
    """ tests for table.split_sentence """

    def setUp(self):
        self.cell = ["1", "2", "3", "4", "5", "6"]

    def test_split_sentence_smaller_than_column_size(self):
        text, rest = table.split_sentence(7, self.cell)
        self.assertEquals(text, self.cell)
        self.assertEquals(len(rest), 0)

    def test_split_sentence_in_half(self):
        text, rest = table.split_sentence(3, self.cell)
        self.assertEquals(text, ["1", "2", "3"])
        self.assertEquals(rest, ["4", "5", "6"])

    @raises(ValueError)
    def test_pathological_case(self):
        table.split_sentence(3, ["1234"])


class TestSplitTableValues(TestCase):
    """ tests for table.split_cell_values """

    def test_split_values(self):
        output = table.split_cell_values("test cell")
        self.assertIn("test ", output)
        self.assertIn("cell", output)

    def test_remove_newlines(self):
        output = table.split_cell_values("test\ncell")
        self.assertIn("test ", output)
        self.assertIn("cell", output)

    def test_strip_value(self):
        output = table.split_cell_values("test cell ")
        self.assertIn("test ", output)
        self.assertIn("cell", output)

    def test_remove_multiple_spaces(self):
        output = table.split_cell_values("test   cell ")
        self.assertIn("test ", output)
        self.assertIn("cell", output)


class TestFormattedRow(TestCase):
    """ tests for table.formatted_row """

    def setUp(self):
        self.column_sizes = [5, 5, 5]
        self.rows = [["foo"], ["bar"], ["baz"]]

    def test_handle_columns(self):
        output = table.formatted_row(self.column_sizes, self.rows)
        self.assertEquals(len(output), 1)
        self.assertEquals("|foo  |bar  |baz  |", output[0])

    def test_handle_word_wrap(self):
        self.rows[0].append("new")
        output = table.formatted_row(self.column_sizes, self.rows)
        self.assertEquals(len(output), 2)
        self.assertEquals("|foo  |bar  |baz  |", output[0])
        self.assertEquals("|new  |     |     |", output[1])

    def test_handle_wrong_column_size(self):
        self.rows.pop()
        output = table.formatted_row(self.column_sizes, self.rows)
        self.assertEquals("|foo  |bar  |     |", output[0])


class TestCalculateColumnSizes(TestCase):

    def setUp(self):
        self.columns = ["123", "123", "123"]
        self.rows = [[["abc"], ["abc"], ["abc"]]]

    def test_should_equal_at_least_80_characters(self):
        output = table.calculate_column_sizes(self.columns, self.rows)
        self.assertEquals(sum(output), 76) # 80 - 4 for the delimiters

    def test_should_respect_large_cell_items(self):
        self.rows[0][0][0] = "a" * 30
        output = table.calculate_column_sizes(self.columns, self.rows)
        self.assertEquals(output[0], 31) # adds an extran item to the length

    def test_should_handle_large_tables(self):
        self.rows[0][0][0] = "a" * 90
        output = table.calculate_column_sizes(self.columns, self.rows)
        self.assertEquals(sum(output), 99)


class TestCreateTable(TestCase):

    def setUp(self):
        self.columns = ["123", "123", "123"]
        self.rows = [["abc", "abc", "abc"]]

    def test_create_formatted_table(self):
        output = table.create_table(self.columns, self.rows)
        self.assertIn("+--------------------------+-------------------------+-------------------------+", output)
        self.assertIn("|123                       |123                      |123                      |", output)
        self.assertIn("+==========================+=========================+=========================+", output)
        self.assertIn("|abc                       |abc                      |abc                      |", output)
        self.assertIn("+--------------------------+-------------------------+-------------------------+", output)
