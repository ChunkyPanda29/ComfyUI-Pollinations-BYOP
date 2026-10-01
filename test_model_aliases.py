import unittest
from unittest.mock import Mock, patch

from pollinations_auto_updater import display_names, fetch_api_models


class ModelAliasTests(unittest.TestCase):
    def test_saved_workflow_values_remain_in_all_four_node_enums(self):
        responses = [
            [{"name": "openai/gpt-5.4-nano", "aliases": ["openai"]}],
            [
                {"name": "black-forest-labs/flux.1-schnell", "aliases": ["flux"], "output_modalities": ["image"]},
                {"name": "wan/wan-2.2", "aliases": ["wan"], "paid_only": True, "output_modalities": ["video"]},
            ],
            [{"name": "elevenlabs/eleven-v3", "aliases": ["elevenlabs"], "paid_only": True}],
        ]
        with patch("pollinations_auto_updater.requests.get", side_effect=[Mock(json=Mock(return_value=data)) for data in responses]):
            models = fetch_api_models()
        for modality, saved in {"text": "openai", "image": "flux", "video": "wan 💎", "audio": "elevenlabs 💎"}.items():
            self.assertIn(saved, models[modality])
            self.assertEqual(len(models[modality]), 2)

    def test_catalogs_without_aliases_keep_their_original_labels(self):
        self.assertEqual(display_names({"name": "flux"}), ["flux"])
        self.assertEqual(display_names({"name": "wan", "aliases": None, "paid_only": True}), ["wan 💎"])
