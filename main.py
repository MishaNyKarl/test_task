from functools import reduce

NUMBERS = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
TARGET_NUMBER = 200


def pad_binary_string(base, num):
    """Дополняет бинарное представление числа нулями слева до нужной длины."""
    return (base - len(str(num))) * '0' + str(num)


def format_expressions(list_of_num_and_signs, target_num):
    """Форматирует найденные выражения в читабельный вид."""
    signs_lib = ['-', '+']
    result = []
    for nums, signs in list_of_num_and_signs:
        inter_res = nums[0]
        for i in range(len(signs)):
            inter_res += signs_lib[int(signs[i])]
            inter_res += nums[i+1]
        result.append(inter_res + f'={target_num}')
    return result


def find_valid_expressions(numbers, target):
    """Генерирует все возможные математические выражения, которые дают целевое значение."""
    result = []
    for i in range(2**(len(numbers)-1)):
        spaces = pad_binary_string(len(numbers)-1, int(bin(i)[2:]))
        intermediate_numbers = []
        new_number = numbers[0]
        for j in range(len(spaces)):
            if spaces[j] == '1':
                new_number += numbers[j+1]
            else:
                intermediate_numbers.append(new_number)
                new_number = numbers[j+1]
        intermediate_numbers.append(new_number)

        number_of_signs = len(intermediate_numbers) - 1
        if number_of_signs < 1:
            continue

        if sum(map(int, intermediate_numbers)) < target or \
                reduce(lambda x, y: x - y, map(int, intermediate_numbers)) > target:
            continue

        for j in range(2**number_of_signs):
            string = intermediate_numbers[0]
            signs = pad_binary_string(number_of_signs, int(bin(j)[2:]))
            intermediate_res = int(intermediate_numbers[0])
            for k in range(len(signs)):
                if signs[k] == '0':
                    intermediate_res -= int(intermediate_numbers[k+1])
                    string += '-'
                    string += intermediate_numbers[k+1]
                else:
                    intermediate_res += int(intermediate_numbers[k+1])
                    string += '+'
                    string += intermediate_numbers[k + 1]
            if intermediate_res == target:
                result.append([intermediate_numbers, signs])
    return result


print(format_expressions(find_valid_expressions(NUMBERS, TARGET_NUMBER), TARGET_NUMBER))
