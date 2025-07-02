from . import motors
from .base import BaseManipulator, BaseMobileRobot, BaseRobot
# Optional hardware back-ends – gracefully ignore if their heavy/extra
# dependencies are missing so that "simulation-only" environments work.
try:
    from .go2 import UnitreeGo2  # pragma: no cover
except ModuleNotFoundError:
    UnitreeGo2 = None  # type: ignore
# Repeat the same pattern for every hardware class that may rely on vendor
# libraries unavailable in CI or simulation-only contexts.
try:
    from .koch11 import KochHardware  # pragma: no cover
except ModuleNotFoundError:
    KochHardware = None  # type: ignore
try:
    from .lekiwi import LeKiwi  # pragma: no cover
except ModuleNotFoundError:
    LeKiwi = None  # type: ignore
try:
    from .piper import PiperHardware  # pragma: no cover
except ModuleNotFoundError:
    PiperHardware = None  # type: ignore
try:
    from .so100 import SO100Hardware  # pragma: no cover
except ModuleNotFoundError:
    SO100Hardware = None  # type: ignore
try:
    from .wx250s import WX250SHardware  # pragma: no cover
except ModuleNotFoundError:
    WX250SHardware = None  # type: ignore
from .phosphobot import RemotePhosphobot
