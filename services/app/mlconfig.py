# Copyright 2023 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
from diffusers import StableDiffusionPipeline
#from transformers import pipeline

class Model:
    def __init__(self):
        self.model_id="CompVis/stable-diffusion-v1-4"
        self.device="cuda"
        self.cache_dir="/app/"
    
    def load(self):
        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16, cache_dir=self.cache_dir)
        pipe = pipe.to(self.device)
        return pipe
