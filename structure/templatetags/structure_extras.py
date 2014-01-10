from django import template

register = template.Library()


@register.filter
def columns(the_list, n):
    list_len = len(the_list)
    split = list_len / n
    if list_len % n != 0:
        split += 1
    return [the_list[0:split], the_list[split:list_len]]


def parse_arguments(arguments):
    arg_list = [int(arg.strip()) for arg in arguments.split(',')]
    return arg_list


@register.filter
def column_split(the_list, sizes):
    sizes = parse_arguments(sizes)
    list_len = len(the_list)
    num_lists = len(sizes)
    lists = []
    start_index = 0
    end_index = 0
    for i in range(0, num_lists):
        end_index = start_index + sizes[i]
        sub_list = the_list[start_index:end_index]
        start_index = end_index
        lists.append((sub_list, len(sub_list)))

    if end_index != list_len:
        extra_list = the_list[end_index:]
        lists.append((extra_list, len(extra_list)))

    return lists


@register.filter
def padded_column_split(the_list, sizes):
    sizes = parse_arguments(sizes)
    list_len = len(the_list)
    num_lists = len(sizes)
    max_length = max(sizes)
    lists = []
    start_index = 0
    end_index = 0
    for i in range(0, num_lists):
        end_index = start_index + sizes[i]
        sub_list = the_list[start_index:end_index]
        sub_list.extend([None] * (max_length-sizes[i]))
        start_index = end_index
        lists.append((sub_list, len(sub_list)))

    if end_index != list_len:
        extra_list = the_list[end_index:]
        extra_list.extend([None] * (max_length-len(extra_list)))
        lists.append((extra_list, len(extra_list)))

    return lists