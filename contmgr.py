import contextlib
@contextlib.contextmanager
def context_manager(num):
    print('Enter')
    yield num + 1
    print('Exit')
with context_manager(2) as cm:
# the following instructions are run when the 'yield' point of the context
# manager is reached.
# 'cm' will have the value that was yielded
    print('Right in the middle with cm = {}'.format(cm))
