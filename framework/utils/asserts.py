def soft_assert_for_lists(expected_list, actual_list):
    messages = []
    if len(expected_list) == len(actual_list):
        for index in range(0, len(expected_list)):
            if expected_list[index] != actual_list[index]:
                messages.append(f"Different values. Expected: {expected_list[index]}, actual: {actual_list[index]}")
    else:
        messages.append("Different length of lists ")

    if messages:
        raise AssertionError("\n".join(messages))
    else:
        return True
