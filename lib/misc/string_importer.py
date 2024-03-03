def import_string_file(language):
    strings_path = f"lib.strings.strings_{language}"
    return __import__(strings_path, fromlist=[''])
