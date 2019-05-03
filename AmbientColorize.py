import sublime
import sublime_plugin


class AmbientColorize(object):
  def initialize(self):
    self.global_settings_file = "Preferences.sublime-settings"
    self.global_settings = sublime.load_settings(self.global_settings_file)
    self.plugin_settings_file = "AmbientColorize.sublime-settings"
    self.plugin_settings = sublime.load_settings(self.plugin_settings_file)

    self.light_scheme = self.plugin_settings.get("light_color_scheme")
    self.light_theme = self.plugin_settings.get("light_theme")
    self.dark_scheme = self.plugin_settings.get("dark_color_scheme")
    self.dark_theme = self.plugin_settings.get("dark_theme")

    self.current_settings = {}
    self.current_settings["scheme"] = self.global_settings.get("color_scheme")
    self.current_settings["theme"] = self.global_settings.get("theme")

    if (self.current_theme() == self.light_theme) & (self.current_scheme() == self.light_scheme):
      self.current_mode = "light"
    elif (self.current_theme() == self.dark_theme) & (self.current_scheme() == self.dark_scheme):
      self.current_mode = "dark"
    else:
      self.current_mode = None

  def current_theme(self):
    return self.current_settings["theme"]

  def current_scheme(self):
    return self.current_settings["scheme"]

  def apply_mode(self):
    scheme = self.light_scheme if self.current_mode == "light" else self.dark_scheme
    theme = self.light_theme if self.current_mode == "light" else self.dark_theme

    self.global_settings.set("theme", theme)
    self.global_settings.set("color_scheme", scheme)
    sublime.save_settings(self.global_settings_file)

  def toggle_mode(self):
    if self.current_mode == "dark":
      self.current_mode = "light"
    else:
      self.current_mode = "dark"

class AmbientColorizeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    _plugin.toggle_mode()
    _plugin.apply_mode()

def plugin_loaded():
  _plugin.initialize()

_plugin = AmbientColorize()

if int(sublime.version()) > 3000:
  plugin_loaded()
