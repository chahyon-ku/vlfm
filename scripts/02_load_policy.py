import os

from habitat_baselines.config.default_structured_configs import HierarchicalPolicyConfig
import hydra
from hydra.utils import instantiate
import torch
import vlfm.measurements.traveled_stairs  # noqa: F401
import vlfm.obs_transformers.resize  # noqa: F401
import vlfm.policy.action_replay_policy  # noqa: F401
import vlfm.policy.habitat_policies  # noqa: F401
import vlfm.utils.vlfm_trainer  # noqa: F401
from habitat_baselines.run import execute_exp
from omegaconf import DictConfig
import omegaconf
import typing

from habitat.config import read_write
from habitat.config.default import patch_config


@hydra.main(
    version_base=None,
    config_path="../config",
    config_name="experiments/vlfm_objectnav_hm3d.yaml",
)
def main(config: DictConfig) -> None:
    dummy_checkpoint_path = "data/checkpoints/dummy_policy.pth"
    if not os.path.isfile(dummy_checkpoint_path):
        dummy_dict = {
            "config": config,
            "extra_state": {"step": 0},
            "state_dict": {},
        }
        os.makedirs(os.path.dirname(dummy_checkpoint_path), exist_ok=True)
        torch.save(dummy_dict, dummy_checkpoint_path)

    config = patch_config(config)
    with read_write(config):
        try:
            config.habitat_baselines.rl.policy.hierarchical_policy = HierarchicalPolicyConfig(high_level_policy={})
            config.habitat.simulator.agents.main_agent.sim_sensors.pop("semantic_sensor")
        except KeyError:
            pass
    config: vlfm.policy.habitat_policies.VLFMPolicyConfig = instantiate(config.habitat_baselines.rl.policy)
    policy = vlfm.policy.habitat_policies.HabitatITMPolicyV2.load_from_checkpoint(dummy_checkpoint_path)
    print(policy)
    print(policy._itm)
    print(policy._frontier_map)
    
    # execute_exp(config, "eval" if config.habitat_baselines.evaluate else "train")


if __name__ == "__main__":
    main()