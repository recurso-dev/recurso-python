from enum import Enum


class OauthCallbackProvider(str, Enum):
    GITHUB = "github"
    GOOGLE = "google"

    def __str__(self) -> str:
        return str(self.value)
