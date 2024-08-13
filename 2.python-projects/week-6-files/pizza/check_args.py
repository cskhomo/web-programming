def check_args(argv, n, ext):

    types = {".py": "Python",
            ".csv": "CSV",}

    if len(argv) < n:
        return "!Too few command-line arguments"

    if len(argv) > n:
        return "!Too many command-line arguments"

    file = argv[1]

    if not file.endswith(ext):
        return f"!Not a {types[ext]} file"
    
    return file