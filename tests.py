import unittest
from fastapi.testclient import TestClient
from main import app

# class TestGetForm(unittest.TestCase):
#     def setUp(self):
#         self.client = TestClient(app)
#
#     def test_get_form_valid(self):
#         response = self.client.post("/get_form", data={"user_email": "test@example.com", "user_phone": "+7 123 456 78 90"})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"form_name": "Order Form"})
#
#     def test_get_form_invalid(self):
#         response = self.client.post("/get_form", data={"user_email": "invalid_email", "user_phone": "+7 123 456 78 90"})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"user_phone": "phone"})

class TestGetForm(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_order_form_valid(self):
        test_data = {
            "customer_email": "example@example.com",
            "customer_phone": "+7 123 456 78 90",
            "order_date": "06.12.2024",
            "customer_comments": "Some text for test"
        }
        expected_data = {
            "form_name": "Order Form"
        }
        response = self.client.post(
            url="/get_form", data=test_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def not_found_template_all_fields_correct(self):
        """
        Шаблон не найден, данные в полях корректны
        """
        test_data = {
            "customer_email": "example@example.com",
            "order_date": "06.12.2024",
            "customer_comments": "Some text for test"
        }
        expected_data = {
            "customer_email": "email",
            "order_date": "date",
            "customer_comments": "text"
        }
        response = self.client.post(
            url="/get_form", data=test_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def not_found_template_any_fields_not_correct(self):
        """
        Шаблон не найден, данные в некоторых полях некорректны
        """
        test_data = {
            "user_email": "example@@",
            "message_date": "06.12.224",
            "user_message": "Some text for test"
        }
        expected_data = {
            "user_email": "email",
            "message_date": "date",
            "user_message": "text"
        }
        response = self.client.post(
            url="/get_form", data=test_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def not_found_template_unexpected_fields(self):
        """
        Шаблон не найден, данные в некоторых полях некорректны
        """
        test_data = {
            "unexpected_field_1": "example@@",
            "unexpected_field_2": "06.12.224",
            "unexpected_field_3": "Some text for test"
        }
        expected_data = {
        }
        response = self.client.post(
            url="/get_form", data=test_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

if __name__ == "__main__":
    unittest.main()