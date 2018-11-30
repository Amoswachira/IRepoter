import unittest
import json
from app import create_app

HEADERS = {'Content-Type': 'application/json'}
URL_REDFLAGS = "/api/v1/red-flags"
URL_REDFLAGS_ID = "/api/v1/red-flags/1"
# URL_REDFLAGS_IDS = "/api/v1/red-flags/111"
# URL_LOCATION = "/api/v1/red-flags/1/location"
# URL_COMMENT = "/api/v1/red-flags/1/comment"


class RedFlagTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {
            "id": 1,
            "createdOn": "Tue, 27 Nov 2018 19:11:10 GMT",
            "createdBy": "Jane",
            'type': 'red-flags',
            "location": "Meru",
            "status": "draft",
            "images": "",
            "videos": "",
            "title": "scandals",
            "comment": "This is atest commet."
        }

    def test_get_redflags(self):
        response = self.client.get(URL_REDFLAGS)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_post_redflag(self):
        response = self.client.post(
                URL_REDFLAGS, headers=HEADERS, data=json.dumps(self.data)
            )
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Created red-flag record', str(result))

    def test_get_one_redflag(self):
        response = self.client.post(
                URL_REDFLAGS, headers=HEADERS, data=json.dumps(self.data)
            )
        response2 = self.client.get(URL_REDFLAGS_ID)
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200)

    # def test_redflag_not_found(self):
    #     response = self.client.get(URL_REDFLAGS_IDS)
    #     result = json.loads(response.data)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertIn("Red-flag does not exist", str(result))

    def test_delete_one_redflag(self):
        response = self.client.post(
                URL_REDFLAGS, headers=HEADERS, data=json.dumps(self.data)
            )
        response2 = self.client.delete(URL_REDFLAGS_ID)
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200)
        self.assertIn('red-flag record has been deleted', str(result))

    # def test_update_location_of_one_redflag(self):
    #     response = self.client.post(
    #             URL_LOCATION, headers=HEADERS, data=json.dumps(self.data)
    #         )
    #     response2 = self.client.patch(
    #             URL_LOCATION, headers=HEADERS, data=json.dumps({
    #                     "location": "Kisumu"
    #                 })
    #         )
    #     result = json.loads(response2.data)
    #     self.assertEqual(response2.status_code, 201)
    #     self.assertIn("Updated red-flag record's location", str(result))

    # def test_update_comment_of_one_redflag(self):
    #     response = self.client.post(
    #             URL_COMMENT, headers=HEADERS, data=json.dumps(self.data)
    #         )
    #     response2 = self.client.patch(
    #             URL_COMMENT, headers=HEADERS, data=json.dumps({
    #                     "comment": "curruption"
    #                 })
    #         )
    #     result = json.loads(response2.data)
    #     self.assertEqual(response2.status_code, 201)
    #     self.assertIn("Updated red-flag record's comment", str(result))

if __name__ == "__main__":
    unittest.main()
