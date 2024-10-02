# using NotImplementedError function instead of pass keyword when you
# create a python function that you have not yet implement it
def connect():
    raise NotImplementedError('this method is not implemented')

def get_users() -> dict[int,str]:
    users: dict[int, str] = {1: 'John', 2: 'Doe', 3: 'Torm'}
    return users
print(get_users())