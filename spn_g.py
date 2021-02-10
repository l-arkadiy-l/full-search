def get_spn(left, right):
    return ','.join([str((float(right[0]) - float(left[0])) / 2),
                     str((float(right[1]) - float(left[1])) / 2)])
