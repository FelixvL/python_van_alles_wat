import tensorflow as tf
print("CUDA beschikbaar:", tf.test.is_built_with_cuda())
print("GPU beschikbaar:", tf.config.list_physical_devices('GPU'))

import torch
print("CUDA beschikbaar:", torch.cuda.is_available())
print("CUDA-versie:", torch.version.cuda)
print("GPU naam:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "Geen GPU gevonden")

print("Is Metal (MPS) beschikbaar?:", torch.backends.mps.is_available())