import statistics


def count_street_lights(road_lenght: int) -> int:

    return road_lenght//20 + 1


def calculate_illumination(distance: int) -> float:

    return 3**(-(distance/100)**2)


def find_longest_streak_in_list(list_of_numbers: list) -> list:
    list_of_numbers.sort()
    longest_streak = []
    current_streak = [list_of_numbers[0]]

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] == list_of_numbers[i - 1] + 1:
            current_streak.append(list_of_numbers[i])
        else:
            if len(current_streak) > len(longest_streak):
                longest_streak = current_streak
            current_streak = [list_of_numbers[i]]

    if len(current_streak) > len(longest_streak):
        longest_streak = current_streak

    return longest_streak


def calculate_list_median(list_of_numbers: list) -> float:

    return statistics.median(list_of_numbers)


def find_index_of_darkest_street_light(not_working_street_lights: list) -> int:
    darkest_light = calculate_list_median(
        find_longest_streak_in_list(not_working_street_lights))

    return int(darkest_light)


def calculate_illumination_of_darkest_light(not_working_street_lights: list) -> float:
    steps_to_working_light = (len(
        find_longest_streak_in_list(not_working_street_lights))/2)
    if steps_to_working_light % 1 == 0.5:
        steps_to_working_light += 0.5

    return calculate_illumination(steps_to_working_light*20)


def find_minimal_number_of_light_bulbs_to_replace(not_working_street_lights: list) -> int:
    # Use function to find the minimal number of light bulbs, which is needed
    # to be replaced to make illumination intencity at every street light non less than 1.

    return len(not_working_street_lights)


if __name__ == "__main__":
    print(find_index_of_darkest_street_light(
        not_working_street_lights=[6, 7, 5, 3, 12, 11, 10, 22, 23, 24, 25]))
    print(calculate_illumination_of_darkest_light(
        not_working_street_lights=[6, 7, 5, 3, 12, 11, 10, 22, 23, 24, 26, 25]))
    print(calculate_illumination(60))
    print(find_minimal_number_of_light_bulbs_to_replace(
        not_working_street_lights=[6, 7, 5, 3, 12, 11, 10, 22, 23, 24, 26, 25]))
