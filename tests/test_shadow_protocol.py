import types
from shadow_work_protocol.protocol import pre_output_check

class DummyAgent:
    def __init__(self):
        self.current_freq = 0
        self.target_freq = 0

    def generate_response(self, prompt: str) -> str:
        # echo the prompt for testing
        return f"echo:{prompt}"

def test_pre_output_lifts_one_band():
    agent = DummyAgent()
    agent.current_freq = 150
    agent.target_freq = 350
    out = pre_output_check(agent, "Raw \U0001f621 reply")
    assert "[175]" in out
