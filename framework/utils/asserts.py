def soft_assert_for_lists(expected_list, actual_list):
    """
    Utility for comparing all values from lists
    :param expected_list: expected list
    :param actual_list: actual list
    :return: True if not errors
    """
    messages = []
    if len(expected_list) == len(actual_list):
        for index in range(0, len(expected_list)):
            if expected_list[index] != actual_list[index]:
                messages.append(f"\nDifferent values. Expected: {expected_list[index]}. Actual: {actual_list[index]}")
    else:
        messages.append("\nDifferent length of lists ")

    if messages:
        raise AssertionError(''.join(messages))
    else:
        return True
