from qamplus.base import QamPlusClient

import unittest


class TestModels(unittest.TestCase):
    execution_logic= {
        "initial": "answer",
		"steps":
		[
			{"name":"play", "data":"2_en" },
			{"name":"play", "data":"2_en" }
        ]
    }

    customer_id = ''
    password = ''

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass

    def test_create_new_call_inbound(self):
        client = QamPlusClient(customer_id=self.customer_id, password=self.password)
        response = client.voice.create(direction="outbound",
           to='18188509066',
           caller_id="12123456789",
           execution_logic=self.execution_logic,
           reference_logic=self.execution_logic,
           country_iso2="us",
           technology="pstn" )

        assert response is not None
        assert response.status_code == 200
