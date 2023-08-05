import unittest
from app import count_street_lights, calculate_illumination, find_longest_streak_in_list, calculate_list_median, find_index_of_darkest_street_light, find_minimal_number_of_light_bulbs_to_replace


class TestApp(unittest.TestCase):
    def test_count_street_lights(self):
        self.assertEqual(11, count_street_lights(200))
        self.assertEqual(3, count_street_lights(40))

    def test_calculate_illumination(self):
        self.assertEqual(0.012345679012345678, calculate_illumination(200))
        self.assertEqual(0, calculate_illumination(220))

    def test_find_longest_streak_in_list(self):
        self.assertEqual([10, 11, 12, 13, 14, 15, 16, 17], find_longest_streak_in_list(
            [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 23, 24]))
        self.assertEqual(
            [2, 3, 4, 5, 6], find_longest_streak_in_list([6, 4, 5, 3, 2]))

    def test_find_index_of_darkest_street_light(self):
        self.assertEqual(23, find_index_of_darkest_street_light(road_length=460,
                                                                not_working_street_lights=[6, 7, 5, 3, 12, 11, 10, 22, 23, 24, 25]))
        self.assertEqual(0, find_index_of_darkest_street_light(road_length=460,
                                                               not_working_street_lights=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertEqual(5, find_index_of_darkest_street_light(road_length=100,
                                                               not_working_street_lights=[3, 4, 5]))
        self.assertEqual(11, find_index_of_darkest_street_light(road_length=9000,
                                                                not_working_street_lights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]))
        self.assertEqual('Wrong imput: road range can be from 0 to 2000000m', find_index_of_darkest_street_light(road_length=-1,
                                                                                                                 not_working_street_lights=[3, 4, 5]))

    def test_calculate_list_median(self):
        self.assertEqual(12, calculate_list_median(
            [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 23, 24]))
        self.assertEqual(
            3.5, calculate_list_median([4, 5, 3, 2]))

    def test_find_minimal_number_of_light_bulbs_to_replace(self):
        self.assertEqual(15, find_minimal_number_of_light_bulbs_to_replace(
            [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 23, 24]))
        self.assertEqual(
            4, find_minimal_number_of_light_bulbs_to_replace([4, 5, 3, 2]))


if __name__ == "__main__":
    unittest.main()
