from hexlet_py_trials.src.module_one.course_base_python import invert_case
from hexlet_py_trials.src.module_one.course_base_python import rotate_left
from hexlet_py_trials.src.module_one.course_base_python import rotate_right
from hexlet_py_trials.src.module_one.course_base_python import is_perfect
from hexlet_py_trials.src.module_one.course_base_python import is_power_of_three
from hexlet_py_trials.src.module_one.course_base_python import fizz_buzz
from hexlet_py_trials.src.module_one.course_base_python import is_degenerated
from hexlet_py_trials.src.module_one.course_base_python import is_vertical
from hexlet_py_trials.src.module_one.course_base_python import is_horizontal
from hexlet_py_trials.src.module_one.course_base_python import is_inclined
from hexlet_py_trials.src.module_one.course_base_python import is_happy_ticket
from hexlet_py_trials.src.module_one.course_base_python import binary_sum
from hexlet_py_trials.src.module_one.course_base_python import is_happy_number
from hexlet_py_trials.src.module_one.course_base_python import encrypt
from hexlet_py_trials.src.module_one.course_base_python import fib


def test_invert_case():
    assert invert_case('HeXleT') == 'hExLEt'
    assert invert_case('') == ''


def test_rotate_left():
    assert rotate_left(('A', 'B', 'C')) == ('B', 'C', 'A')
    assert rotate_left(()) == ()


def test_rotate_right():
    assert rotate_right(('A', 'B', 'C')) == ('C', 'A', 'B')
    assert rotate_right(()) == ()
  

def test_is_perfect():
    assert is_perfect(6)
    assert not is_perfect(27)


def test_is_power_of_three():
    assert is_power_of_three(9)
    assert not is_power_of_three(10)


def test_fizz_buzz():
    assert fizz_buzz(1, 5) == '1 2 Fizz 4 Buzz'
    assert fizz_buzz(5, 1) == ''


def test_point_functions():
    assert is_degenerated((1, 1), (1, 1))
    assert not is_degenerated((1, 2), (2, 4))
    
    assert is_vertical((1, 1), (1, 4))
    assert not is_vertical((1, 1), (2, 4))

    assert is_horizontal((1, 1), (3, 1))
    assert not is_horizontal((1, 1), (1, 1))

    assert is_inclined((1, 1,), (2, 2))
    assert not is_inclined((1, 1), (2, 1))


def test_is_happy_ticket():
    assert is_happy_ticket('123123')
    assert is_happy_ticket('341800')
    assert not is_happy_ticket('42')
    assert not is_happy_ticket('12345678')


def test_binary_sum():
    assert binary_sum('10', '1') == '11'
    assert binary_sum('1101', '101') == '10010'


def test_is_happy_number():
    assert is_happy_number(7)
    assert not is_happy_number(6)


def test_encrypt():
    assert encrypt("move") == 'omev'
    assert encrypt("attack") == 'taatkc'
    assert encrypt("go!") == 'og!'


def test_fib_num():
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(10) == 55
