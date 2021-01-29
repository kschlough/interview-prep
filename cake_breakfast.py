import unittest


def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    delivery_ids = sorted(delivery_ids)
    print(delivery_ids)
    
    # if len(delivery_ids) % 2 == 0:
    #     return []
    

    while delivery_ids != []:

        if len(delivery_ids) < 2:
            return delivery_ids[0]
       
        
        compare_num = delivery_ids.pop()

        # compare if popped last element is equal to next last element
        # if not, last element is the one
            
            
        if compare_num == delivery_ids[(len(delivery_ids)-1)]:
            delivery_ids.pop()
            
            
        elif compare_num != delivery_ids[(len(delivery_ids)-1)]:
            return compare_num
            
        
    



#pseudocode
#sort the list
#go through the list in sets of 2
#compare the 2 numbers
#if they're equal move on
#else the first one is the unreturned drone













# Tests

class Test(unittest.TestCase):

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)