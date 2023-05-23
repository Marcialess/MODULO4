try:
    raise Exception("telefono","987738316","invalidate Phone Format")
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

    key, value, message = e.args

    print(f'key -->{key}')
    print(f'value -->{value}')
    print(f'message -->{message}')