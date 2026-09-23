def read_page_size(raw):
    if not isinstance(raw, str):
        raise TypeError('必须是字符串')
    try:
        temp = int(raw)
        if temp > 100 or temp < 1:
            raise ValueError("超出范围")
    except ValueError:
        print(ValueError)
    except TypeError:
        print(TypeError)
    else:
        return temp


print(read_page_size(True))

