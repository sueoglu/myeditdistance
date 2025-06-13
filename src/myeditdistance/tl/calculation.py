def edit_distance(string1: str, string2: str) -> int:
    """Run the Levenshtein algorithm on string1 and string2.

    Parameters
    ----------
    string1
        first string
    string2
        second string

    Returns
    -------
    Some integer value.
    """
    if len(string1) == 0:
        ed = len(string2)
        return ed
    if len(string2) == 0:
        ed = len(string1)
        return ed
    elif string1[0] == string2[0]:
        return edit_distance(string1[1:], string2[1:])
    else:
        ed = 1 + min(
            edit_distance(string1[1:], string2),
            edit_distance(string1, string2[1:]),
            edit_distance(string1[1:], string2[1:]),
        )
        return ed
