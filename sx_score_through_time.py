import extract_info_in_file


if __name__ == "__main__":
    FILE ="test.txt"
    content = extract_info_in_file.read(FILE)
    split_new_line = extract_info_in_file.split_to_the_line(content)
    print(len(split_new_line))