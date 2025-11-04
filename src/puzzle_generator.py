import random
import operator

OPS = {
    'easy': [('+', operator.add), ('-', operator.sub)],
    'medium': [('*', operator.mul)],
    'hard': [('/', operator.floordiv)],
    'extreme': [('*', operator.mul), ('/', operator.floordiv)]
}

def generate_puzzle(level):
    op_symbol, op_func = random.choice(OPS[level])
    if level == 'easy':
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif level == 'medium':
        a, b = random.randint(10, 20), random.randint(2, 10)
    elif level == 'hard':
        a, b = random.randint(20, 50), random.randint(2, 10)
        a = a * b  # ensure division has integer result
    else:
        a,b = random.randint(50, 100), random.randint(2, 10)
    question = f"{a} {op_symbol} {b}"
    answer = op_func(a, b)
    return question, answer

