import pywhatkit
import time


def creat_list_from_txt(file_path):
    """
    creates a lst of numbers of a given text file
    :param file_path: path to file with all the numbers
    :return: lst containing all the numbers
    """
    with open(file_path) as all_nums:
        final_list = []
        for cur_num in all_nums:
            final_list.append(cur_num.strip())

        return final_list


def add_area_code(simple_num):
    """
    adds the area code to a given number
    :param simple_num: number without area code
    :return: the number with it
    """
    no_zero = simple_num[1:]
    area_code = "+972"
    final = area_code + no_zero
    return final


if __name__ == '__main__':
    # put the text string you want to send in here, as "the_text"
    the_text = "Some text to send"

    start = time.time()
    num_lst = creat_list_from_txt("nums_lst.txt")
    total_amount = len(num_lst)
    counter = 1
    for num in num_lst:
        fixed_num = add_area_code(num)
        pywhatkit.sendwhatmsg_instantly(fixed_num, the_text, tab_close=True, wait_time=8)
        print("we finished with contact", counter, "out of", total_amount)
        counter += 1
    end = time.time()
    print("finished")
    total_time = end - start
    print("it only took", round(total_time, 2), "seconds. which is",
          round((total_time / total_amount), 2), "seconds per contact")
