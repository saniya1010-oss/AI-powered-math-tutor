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
        a, b = random.randint(10, 15), random.randint(2, 10)
    elif level == 'hard':
        a, b = random.randint(15, 30), random.randint(2, 10)
        a = a * b  # ensure division has integer result
    else:
        a,b = random.randint(30, 80), random.randint(2, 10)
    question = f"{a} {op_symbol} {b}"
    answer = op_func(a, b)
    return question, answer


