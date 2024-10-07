import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="some_prefix_",
    )

    hello: str | None = None


def hello() -> None:
    print(Settings())
