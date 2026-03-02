def login(user:str):
    return f"{user} logged in"

def logout(user:str):
    return f"{user} logged out"

def open(user:str, file_name:str):
    return f"{user} opened {file_name}"

def callback_fun(funcion,*args):
    return funcion(*args)

# print(callback_fun(open,"Manuel","archivo.xlsx"))