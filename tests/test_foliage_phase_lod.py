import pytest
import render.foliage_phase_lod as mod

CASES = [
    ("instance_phase", (1, 2)),
    ("lod_agnostic", (1, 2)),
    ("timebase_unify", (1, 2)),
    ("world_coord_phase", (1, 2)),
    ("wind_param", (0.3, 0.7)),
    ("switch_continuity", (1, 2)),
    ("phase_offset", (1, 2)),
    ("sway_amplitude", (0.5, 1.0)),
    ("buffer_layout", (1, 2)),
    ("vertex_shader", (1, 2)),
    ("lod_tier", (2, 3)),
    ("sync_group", (1, 2)),
    ("jitter_check", (1, 2)),
    ("restore_seed", (1, 2)),
    ("phase_metric", (1.0, 2.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
