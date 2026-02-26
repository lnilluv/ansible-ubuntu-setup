from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HardeningLayoutTest(unittest.TestCase):
    def test_inventory_is_parameterized(self) -> None:
        content = (ROOT / "hosts.yml").read_text(encoding="utf-8")
        self.assertIn("{{ target_vps_ip }}", content)
        self.assertNotRegex(content, r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

    def test_two_phase_playbooks_exist(self) -> None:
        self.assertTrue((ROOT / "bootstrap-playbook.yml").exists())
        self.assertTrue((ROOT / "lockdown-playbook.yml").exists())

    def test_secure_variable_template_exists(self) -> None:
        example = ROOT / "group_vars" / "all.example.yml"
        self.assertTrue(example.exists())
        content = example.read_text(encoding="utf-8")
        for key in (
            "target_vps_ip",
            "bootstrap_allowed_ip",
            "ssh_pubkey_path",
            "tailscale_authkey",
            "admin_user",
            "ssh_port",
        ):
            self.assertIn(f"{key}:", content)

    def test_firewall_role_mentions_tailscale_only_policy(self) -> None:
        content = (ROOT / "roles" / "firewall" / "tasks" / "main.yml").read_text(encoding="utf-8")
        self.assertIn("tailscale0", content)
        self.assertIn("bootstrap_allowed_ip", content)

    def test_validation_role_exists(self) -> None:
        validation_role = ROOT / "roles" / "validation" / "tasks" / "main.yml"
        self.assertTrue(validation_role.exists())

    def test_readme_describes_two_phase_tailscale_flow(self) -> None:
        content = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("ubuntu 22.04", content)
        self.assertIn("two-phase", content)
        self.assertIn("tailscale", content)
        self.assertIn("bootstrap", content)
        self.assertIn("lockdown", content)


if __name__ == "__main__":
    unittest.main()
