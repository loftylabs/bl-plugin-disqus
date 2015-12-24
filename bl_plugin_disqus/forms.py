from baselinecore.plugin.forms import BasePluginSettingsForm
from django import forms


class DisqusSettingsForm(BasePluginSettingsForm):

    plugin = 'bl_plugin_disqus'

    channel_name = forms.CharField(
        help_text="This is the unique Disqus ID that identifies your website or property, "
                  "not your username.")
