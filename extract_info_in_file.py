from posixpath import split


def read(file):
    """ Read the content of a file

    Parameters
    ----------
    file : str
        The file location

    Returns
    -------
    content : str

    """
    my_file = open(file,"r")
    content = my_file.read()
    my_file.close()
    return content

def split_to_the_line(content):
    """Split txt file to the line

    Parameters
    ----------
    content : str 


    Returns
    -------
    content_list : lst
        Split return to line txt

    """
    content_list = content.split("\n")
    return content_list
     
if __name__ == '__main__':
    file_path="test.txt"
    content = read(file_path)
    split_to_the_line(content)
