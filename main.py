import module_strings

def get_number():
    import random
    return random.randint(1, 100)

def get_hello():
    return 'Hello'

if __name__ == '__maine__':
    print(module_strings.func())