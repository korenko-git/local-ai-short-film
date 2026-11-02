"""Create a short, deterministic bell-like achievement sting as PCM WAV."""

import math
import random
import struct
import wave
from pathlib import Path


SAMPLE_RATE = 48_000
DURATION = 2.2
SEED = 11070330
OUTPUT = Path(__file__).resolve().parents[3] / "audio" / "sfx" / "scene07-curiosity-achievement.wav"


def main() -> None:
    count = round(SAMPLE_RATE * DURATION)
    dry = [0.0] * count
    notes = [
        (0.00, 659.25, 0.78),
        (0.18, 783.99, 0.70),
        (0.38, 987.77, 0.65),
        (0.62, 1318.51, 0.60),
    ]

    for start, frequency, velocity in notes:
        first = round(start * SAMPLE_RATE)
        for i in range(first, count):
            t = (i - first) / SAMPLE_RATE
            if t > 1.15:
                break
            attack = 1.0 - math.exp(-t / 0.006)
            fundamental = math.exp(-t / 0.38)
            overtone = math.exp(-t / 0.22)
            partials = (
                0.68 * math.sin(2 * math.pi * frequency * t)
                + 0.22 * overtone * math.sin(2 * math.pi * frequency * 2.01 * t + 0.12)
                + 0.08 * overtone * math.sin(2 * math.pi * frequency * 3.92 * t + 0.3)
                + 0.07 * fundamental * math.sin(2 * math.pi * frequency * 1.003 * t)
            )
            dry[i] += velocity * attack * fundamental * partials

    # Soft low note under the first chime, like a gentle achievement pulse.
    for i in range(count):
        t = i / SAMPLE_RATE
        if t < 0.42:
            dry[i] += 0.12 * math.exp(-t / 0.13) * math.sin(2 * math.pi * 130.81 * t)

    rng = random.Random(SEED)
    previous = 0.0
    for i in range(count):
        t = i / SAMPLE_RATE
        white = rng.uniform(-1.0, 1.0)
        high = white - previous
        previous = white
        envelope = min(1.0, t / 0.04) * math.exp(-max(0.0, t - 0.2) / 0.52)
        dry[i] += 0.012 * high * envelope

    # Three quiet early reflections give the chime a compact, polished tail.
    wet = dry[:]
    for delay_s, gain in ((0.083, 0.16), (0.151, 0.095), (0.227, 0.052)):
        delay = round(delay_s * SAMPLE_RATE)
        for i in range(delay, count):
            wet[i] += dry[i - delay] * gain

    peak = max(abs(value) for value in wet) or 1.0
    gain = 0.72 / peak
    frames = bytearray()
    for i, value in enumerate(wet):
        t = i / SAMPLE_RATE
        fade = min(1.0, max(0.0, (DURATION - t) / 0.32))
        sample = max(-1.0, min(1.0, value * gain * fade))
        pcm = round(sample * 32767)
        frames.extend(struct.pack("<hh", pcm, pcm))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUTPUT), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(frames)


if __name__ == "__main__":
    main()
