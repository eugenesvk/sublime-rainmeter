import sublime

from unittest import TestCase


class TestThemeSwitcher(TestCase):
    """Test class wrapper using unittest."""

    # pylint: disable=W0703; This is acceptable since we are testing it not failing

    def test_edit_theme_command_single_theme(self):
        """Should run through."""
        win = sublime.active_window()

        future_skin = "Lachgummi Joghurt"
        win.run_command(
            "edit_theme",
            {
                "theme": future_skin
            }
        )

        settings = sublime.load_settings("Rainmeter.sublime-settings")
        post_theme = settings.get("color_scheme", None)

        self.assertTrue(future_skin in post_theme)

    def test_edit_theme_command_multi_theme(self):
        win = sublime.active_window()

        settings = sublime.load_settings("Rainmeter.sublime-settings")
        prior_theme = settings.get("color_scheme", None)

        win.run_command(
            "edit_theme",
            {
                "theme": "Not existing skin"
            }
        )

        settings = sublime.load_settings("Rainmeter.sublime-settings")
        post_theme = settings.get("color_scheme", None)

        self.assertEqual(prior_theme, post_theme)