from pathlib import Path
import json, math
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly
import torch
import torchaudio

root = Path(__file__).resolve().parents[5]
scene = root / 'scenes/09-speed'
work = scene / 'work'
torch.set_num_threads(2)
torch.set_num_interop_threads(1)
torch.hub.set_dir(str(work / 'audio-model-cache'))
bundle = torchaudio.pipelines.HDEMUCS_HIGH_MUSDB_PLUS
print('Loading audio separator on CPU, two threads', flush=True)
model = bundle.get_model().eval().cpu()
sr, pcm = wavfile.read(work / 'speed-source.wav')
x = pcm.astype(np.float32) / 32768.0
x = resample_poly(x, 44100, sr, axis=0).astype(np.float32)
wave = torch.from_numpy(x.T.copy())
ref = wave.mean(0)
mean, std = ref.mean(), ref.std().clamp_min(1e-6)
wave = (wave - mean) / std
print('Separating 6.6 seconds of audio; no GPU', flush=True)
with torch.inference_mode():
    stems = model(wave[None])[0] * std
names = model.sources
vocal_idx = names.index('vocals')
background = sum(stems[i] for i in range(len(names)) if i != vocal_idx)
vocals = stems[vocal_idx]
for name, data in [('scene09-speed-instrumental-v1.wav', background), ('scene09-speed-vocals-removed-v1.wav', vocals)]:
    a = data.T.numpy()
    wavfile.write(scene / 'audio/sfx' / name, 44100, np.clip(a, -1, 1).astype(np.float32))
record = {'method':'torchaudio HDEMUCS_HIGH_MUSDB_PLUS','device':'cpu','threads':2,'sample_rate':44100,'sources':names,'removed':'vocals','kept':['drums','bass','other'],'source':'work/speed-source.wav','output':'audio/sfx/scene09-speed-instrumental-v1.wav','status':'separated_pending_review'}
Path(__file__).with_name('parameters.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print('Done', flush=True)

