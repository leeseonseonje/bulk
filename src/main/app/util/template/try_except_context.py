def context(call, message):
    try:
        return call()
    except:
        print(message)


# def transactions():
