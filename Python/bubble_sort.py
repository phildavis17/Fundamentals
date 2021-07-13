import logging

def bubble_sort(in_list: list) -> list:
    """Bubble sort. A bad sorting algo."""
    if not in_list:
        return []
    end = len(in_list) - 1
    while end > 0:
        logging.info(f"Current: {in_list}")
        for i in range(end):
            if in_list[i] > in_list[i + 1]:
                in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
        end += -1
    return in_list

if __name__ == "__main__":
    print(bubble_sort([3, 2, 1, 4, 5]))