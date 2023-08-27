import os

ELEVENLABS_ENDPOINT = os.getenv(
    "ELEVENLABS_ENDPOINT", "https://api.elevenlabs.io/v1/text-to-speech"
)