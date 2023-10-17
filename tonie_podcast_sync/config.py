"""The configuration module for the tonie_podcast_sync."""
from dynaconf import Dynaconf

APP_NAME = "tonie-podcast-sync-cli"

settings = Dynaconf(
    envvar_prefix="TPS",
    settings_files=["settings.toml", ".secrets.toml"],
)

# `envvar_prefix` = export envvars with `export TPS_FOO=bar`.
# `settings_files` = Load these files in the order.
