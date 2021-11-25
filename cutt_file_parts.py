import concurrent.futures


def before_last_lenght_file_element(file_name: str):
    """  
    Remove the last 2 digits of the file length
    Args:
        file_name (str): name file  

    Returns:
        list : content file 
        int  : ast 2 digits of the file length 
    """
    elements = []
    try:
        with open(file_name, encoding="utf-8") as file_wordlists:
            elements = file_wordlists.readlines()
    except UnicodeDecodeError:
        with open(file_name, encoding="ISO-8859-1") as file_wordlists:
            elements = file_wordlists.readlines()

    try:
        return elements, int(str(len(elements))[:-2])
    except ValueError:
        return elements, len(elements)


def calcul(length_content: int, operator: int):
    """
    Calculate on how much to cut the contents of the file
    Args:
        length_content (int): lenght content file 
        operator (int): before_last_lenght_file_element function result

    Returns:
        int : result calcul cutt parts 
    """
    calcul = int
    if length_content > 1_000_000:
        calcul = length_content//operator//100
        print(calcul)

    elif length_content > 1_000_000:
        calcul = length_content//operator//1.8

    elif length_content > 10_000:
        calcul = length_content//operator//2

    elif length_content > 1_000:
        calcul = length_content//operator//3

    if calcul == 0:
        return operator
    return int(calcul)


def cutt(_list: list, result_calcul: int):
    """
    Generator function which returns the elements of the file
    Args:
        _list (list): list content file 
        result_calcul (int): result of calcul function

    Yields:
        str : line on file 
    """
    start = result_calcul
    while(result_calcul < len(_list)):
        if (result_calcul+start) > len(_list):
            yield _list[result_calcul: len(_list)]
        result_calcul += start
        yield _list[start:result_calcul]


def thread_executor(element: list, funct, number_thread: int = 50):
    """
    Function that executes the thread
    Args:
        element (list): line of file 
        funct ([type]): function for execute on thread
        number_thread (int, optional): number of thread . Defaults to 50.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_thread) as executor:
        for content in element:
            executor.submit(funct, content.strip())