import statistics


def count_street_lights(road_lenght: int) -> int:

    return road_lenght//20 + 1


def calculate_illumination(distance: int) -> float:
    illumination = 3**(-(distance/100)**2)
    if illumination < 0.01:
        illumination = 0

    return illumination


def find_longest_streak_in_list(list_of_numbers: list) -> list:
    list_of_numbers.sort()
    longest_streak = []
    current_streak = [list_of_numbers[0]]

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] == list_of_numbers[i - 1] + 1:
            current_streak.append(list_of_numbers[i])
            if len(current_streak) > len(longest_streak):
                longest_streak = current_streak
        else:
            current_streak = [list_of_numbers[i]]

    return longest_streak


def calculate_list_median(list_of_numbers: list) -> float:

    return statistics.median(list_of_numbers)


def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list) -> int:
    if road_length < 0 or road_length > 2000000:
        return 'Wrong imput: road range can be from 0 to 2000000m'
    not_working_street_lights.sort()
    logest_streak_of_lights = find_longest_streak_in_list(
        not_working_street_lights)
    if logest_streak_of_lights[0] == 0:
        darkest_light = not_working_street_lights[0]
    elif logest_streak_of_lights[-1] + 1 == count_street_lights(road_length):
        darkest_light = not_working_street_lights[-1]
    elif len(logest_streak_of_lights) > 20:
        # from 10 illumination < 0.01
        darkest_light = not_working_street_lights[10]
    else:
        darkest_light = calculate_list_median(
            logest_streak_of_lights)

    return int(darkest_light)


def find_minimal_number_of_light_bulbs_to_replace(not_working_street_lights: list) -> int:
    # Use function to find the minimal number of light bulbs, which is needed
    # to be replaced to make illumination intencity at every street light non less than 1.

    return len(not_working_street_lights)


if __name__ == "__main__":
    assert find_index_of_darkest_street_light(road_length=460,
                                              not_working_street_lights=[6, 7, 5, 3, 12, 11, 10, 22, 23, 24, 25]) == 23
    assert find_minimal_number_of_light_bulbs_to_replace(
        not_working_street_lights=[6, 7, 5, 3, 12, 11, 10, 22, 23, 24, 26, 25]) == 12
    assert find_index_of_darkest_street_light(
        road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    print("ALL TESTS PASSED")
