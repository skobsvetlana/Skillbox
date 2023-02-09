def is_spec_symbols(name):
    spec_symbols = '@№$%^&*()'

    for symbol in spec_symbols:
        if file_name.startswith(symbol):
            return True

    return False
