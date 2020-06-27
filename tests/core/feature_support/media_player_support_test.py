from core.feature_support import FeatureSupport
from core.feature_support.media_player import MediaPlayerSupport
import pytest


@pytest.mark.parametrize(
    "number, expected_supported_features",
    [
        (1, {MediaPlayerSupport.PAUSE,},),
        (4, {MediaPlayerSupport.VOLUME_SET,},),
        (
            57,
            {
                MediaPlayerSupport.NEXT_TRACK,
                MediaPlayerSupport.PREVIOUS_TRACK,
                MediaPlayerSupport.VOLUME_MUTE,
                MediaPlayerSupport.PAUSE,
            },
        ),
        (
            149,
            {
                MediaPlayerSupport.TURN_ON,
                MediaPlayerSupport.PREVIOUS_TRACK,
                MediaPlayerSupport.VOLUME_SET,
                MediaPlayerSupport.PAUSE,
            },
        ),
        (0, set()),
    ],
)
def test_init(number, expected_supported_features):
    media_player_support = MediaPlayerSupport(None, None)
    media_player_support._supported_features = FeatureSupport.decode(
        number, media_player_support.features
    )
    assert media_player_support._supported_features == expected_supported_features