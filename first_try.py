import pywhatkit
import time


def creat_list_from_txt(file_path):
    with open(file_path) as all_nums:
        final_list = []
        for cur_num in all_nums:
            final_list.append(cur_num.strip())

        return final_list


def add_area_code(simple_num):
    no_zero = simple_num[1:]
    pre = "+972"
    final = pre + no_zero
    return final


if __name__ == '__main__':
    start = time.time()
    num_lst = creat_list_from_txt("nums_lst.txt")
    total_amount = len(num_lst)
    counter = 1
    for num in num_lst:
        fixed_num = add_area_code(num)
        pywhatkit.sendwhatmsg_instantly(fixed_num, "מתנצל על השיגוע",
                                        tab_close=True, wait_time=10)
        print("we finished with contact", counter, "out of", total_amount)
        counter += 1
    end = time.time()
    print("finished")
    total_time = end - start
    print("it only took", round(total_time, 2), "seconds. which is",
          round((total_time / total_amount), 2), "seconds per contact")
