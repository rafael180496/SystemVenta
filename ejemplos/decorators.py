PASSWORD='12345678'

def password_requerid(func):
    def wrapper():
        password=input(('Cual es tu contrasena'))

        if password == PASSWORD:
            needs_password()
        else:
            print('Invalido')
    
    return wrapper()

@password_requerid
def needs_password():
    print('La contrasena es correcta')


def UPP(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper


@UPP
def say_my_name(name):
    return 'Hola, {}'.format(name)



if __name__ == "__main__":
    needs_password()
    say_my_name('raf')
