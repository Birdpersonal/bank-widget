from isort.sorting import sort


def filter_by_state(list_dick: list, state = 'EXECUTED') -> list:
    new_list = []
    for i in list_dick:
        if i['state'] == state:
            new_list.append(i)
        else:
            continue
    return new_list

# filter_by_state_fon = filter_by_state()
# print(filter_by_state_fon)


def sort_by_date(list_dicktionary: list, reverse= True) -> list:
    new_sort = sorted(list_dicktionary, key=lambda x: x['date'], reverse= True)
    return new_sort

# sort_by_date_fon = sort_by_date()
# print(sort_by_date_fon)