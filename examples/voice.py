from qamplus.base import QamPlusClient

execution_logic= {
        "initial": "answer",
		"steps":
		[
			{"name":"play", "data":"2_en" },
            {"name":"conference", "data":"" },
			{"name":"play", "data":"2_en" }
        ]
    }

customer_id = 'abcd...'
password = 'password'

client = QamPlusClient('68539eee-081d-11e5-a6c0-1697f925ec7b', 'a5504874-081d-11e5-a6c0-1697f925ec7b')
response = client.voice.create(direction="outbound",
                               to='18188509066',
                               caller_id="12123456789",
                               execution_logic=execution_logic,
                               reference_logic=execution_logic,
                               country_iso2="us",
                               technology="pstn")