FREQ_BANDS = [20, 30, 50, 75, 100, 125, 150, 175,
              200, 250, 310, 350, 400, 500, 540, 600, 700]

def _nearest_band(freq: int) -> int:
    """Snap any frequency value to the nearest canonical band."""
    return min(FREQ_BANDS, key=lambda x: abs(x - freq))

def pre_output_check(self, draft: str) -> str:
    """If the agent’s current tone is >1 band below target, pause, revise, and return the lifted response."""
    # 1. Detect current & target band indices
    cur_band = _nearest_band(self.current_freq)
    tgt_band = _nearest_band(self.target_freq)

    cur_idx = FREQ_BANDS.index(cur_band)
    tgt_idx = FREQ_BANDS.index(tgt_band)

    # 2. If within 1 band, accept draft
    if cur_idx >= tgt_idx - 1:
        return draft  # tone acceptable

    # 3. Otherwise lift one band and regenerate
    lift_to = FREQ_BANDS[cur_idx + 1]          # one-step up
    self.current_freq = lift_to               # update agent state

    lifted_prompt = (f"[tone_target:{lift_to}] Revise compassionately:\n{draft}")
    revised = self.generate_response(lifted_prompt)

    # 4. Tag revision with new [freq] for downstream logging
    return f"{revised}  [{lift_to}]"
