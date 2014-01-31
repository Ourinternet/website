from django import template

register = template.Library()


@register.filter
def columns(the_list, num_lists):
    list_len = len(the_list)
    split_list_size = list_len / num_lists

    if list_len % num_lists != 0:
        split_list_size += 1

    lists = []
    start_index = 0
    end_index = 0
    for i in range(0, num_lists):
        end_index = start_index + split_list_size
        sub_list = the_list[start_index:end_index]
        start_index = end_index
        lists.append(sub_list)

    if end_index != list_len:
        extra_list = the_list[end_index:]
        lists[0].extend(extra_list)

    max_length = split_list_size
    return lists, max_length


@register.filter
def padded_column(the_list, size):
    list_len = len(the_list)
    the_list.extend([None] * (size-list_len))

    return the_list
