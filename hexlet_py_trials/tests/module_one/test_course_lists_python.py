from hexlet_py_trials.src.module_one.course_lists_python import compare_version
from hexlet_py_trials.src.module_one.course_lists_python import length_of_last_word
from hexlet_py_trials.src.module_one.course_lists_python import hamming_weight
from hexlet_py_trials.src.module_one.course_lists_python import is_continuous_sequence
from hexlet_py_trials.src.module_one.course_lists_python import transposed
from hexlet_py_trials.src.module_one.course_lists_python import chunked


def test_compare_version():
    assert compare_version("0.1", "0.2") == -1
    assert compare_version("0.2", "0.1") == 1
    assert compare_version("4.2", "4.2") == 0


def test_length_of_last_word():
    assert length_of_last_word('') == 0
    assert length_of_last_word('man in Black') == 5
    assert length_of_last_word('hello, world!     ') == 6
    assert length_of_last_word('hello\t\nworld') == 5


def test_hamming_weight():
    assert hamming_weight(0) == 0
    assert hamming_weight(4) == 1
    assert hamming_weight(101) == 4


def test_is_continuous_sequence():
    assert is_continuous_sequence([10, 11, 12, 13])
    assert is_continuous_sequence([-5, -4, -3])
    assert not is_continuous_sequence([10, 11, 12, 14, 15])
    assert not is_continuous_sequence([1, 2, 2, 3])
    assert not is_continuous_sequence([7])
    assert not is_continuous_sequence([])


def test_transosed():
    assert transposed([[1]]) == [[1]]
    assert transposed([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transposed([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert transposed(transposed([[1, 2]])) == [[1, 2]]


def test_chunked():
    assert chunked(2, ['a', 'b', 'c', 'd']) == [['a', 'b'], ['c', 'd']]
    assert chunked(3, ['a', 'b', 'c', 'd']) == [['a', 'b', 'c'], ['d']]
    assert chunked(3, 'foobar') == ['foo', 'bar']
    assert chunked(10, (42,)) == [(42,)]
