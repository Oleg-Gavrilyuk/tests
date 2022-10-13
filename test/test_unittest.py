import unittest
from main import get_doc_owner_name, get_all_doc_owners_names, documents, delete_doc
from main import get_doc_shelf, add_new_doc


class TestFunctions(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('start to test')

    def test_get_all_doc_owners_name(self):
        self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')
        
    def test_get_all_doc_owners_names(self):
        name_list = []
        for i in documents:
            name_list.append(i['name'])
        a = set(name_list)
        self.assertEqual(get_all_doc_owners_names(), a)

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('11-2'), '1')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('11-3', 'pass', 'Иванов Иван', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(delete_doc('11-3'))

    @classmethod
    def tearDown(self):
        print('End of the test')



if __name__ == '__main__':
    unittest.main()
