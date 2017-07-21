# I am aware that this isn't the pythonic way but I believe in writing small composable functions
# than importing them into the program

def isEmpty(str):
    if str == "":
        return True

def isError(func, name):
    if func == True and name == request.form['title']:
        return isEmpty("")



