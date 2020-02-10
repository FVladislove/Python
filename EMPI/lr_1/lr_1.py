import decimal as d


def selection_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
    return list


def sample_mean(list):
    sum = d.Decimal("0.00")
    for i in range(len(list)):
        sum += list[i]
    sum = sum / len(list)
    return sum


def dispersion(list):
    sample_mean_var = sample_mean(list)
    sum = d.Decimal("0.00")
    for i in range(len(list)):
        sum += (list[i] - sample_mean_var) ** 2
    sum /= (len(list) - 1)
    return sum


def root_mean_square_deviation(list):
    d.getcontext().prec = 8
    rms_deviation = dispersion(list) ** (d.Decimal("1") / d.Decimal("2"))
    return rms_deviation


def distribution_coefficient(list):
    sample_mean_var = sample_mean(list)
    upper_sum = d.Decimal("0.00000000")
    lower_sum = d.Decimal("0.00000000")

    for i in range(len(list)):
        temp = list[i] - sample_mean_var
        upper_sum += temp ** 3
        lower_sum += temp ** 2
    upper_sum /= len(list)
    lower_sum = (lower_sum / len(list)) ** (d.Decimal("3") / d.Decimal("2"))
    return (upper_sum / len(list)) / (lower_sum / len(list))


def excess_coefficient(list):
    sample_mean_var = sample_mean(list)
    d.getcontext().prec = 8
    upper_sum = d.Decimal("0")
    lower_sum = d.Decimal("0")
    for i in range(len(list)):
        temp = (list[i] - sample_mean_var)
        upper_sum += temp ** 4
        lower_sum += temp ** 2
    upper_sum /= len(list)
    lower_sum = (lower_sum / len(list)) ** 2
    return upper_sum / lower_sum - 3


def x_mod(list):
    n = len(list)
    if n % 2 == 0:
        x_mod = 1 / 2 * (list[n // 2] + list[(n + n) // 2])
    else:
        x_mod = list[(n + 1) // 2]
    return x_mod


list = [2, 2, 4, 3, 3, 5, 8, 8, 8, 6, 6, 6, 7, 7, 5, 5, 5, 4, 2, 4, 3, 4, 4, 5, 5]
list = selection_sort(list)
sample_mean_var = sample_mean(list)
print("Sample mean = " + str(sample_mean_var))

dispersion_var = dispersion(list)
print("Dispersion = " + str(dispersion_var))

rms_deviation = root_mean_square_deviation(list)
print("RMS deviation = " + str(rms_deviation))

distribution_coefficient_var = distribution_coefficient(list)
print("Distribution coefficient = " + str(distribution_coefficient_var))
excess_coefficient_var = excess_coefficient(list)
print("Excess coeficient = " + str(excess_coefficient_var))
print("X mod = " + str(x_mod(list)))
