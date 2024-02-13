# flake8: noqa
# There's no way to ignore "F401 '...' imported but unused" warnings in this
# module, but to preserve other warnings. So, don't check this module at all.

# Copyright 2020 The HuggingFace Team. All rights reserved.
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

from ...file_utils import is_sentencepiece_available, is_torch_available
from .configuration_xlm_prophetnet import XLM_PROPHETNET_PRETRAINED_CONFIG_ARCHIVE_MAP, XLMProphetNetConfig


if is_sentencepiece_available():
    from .tokenization_xlm_prophetnet import XLMProphetNetTokenizer

if is_torch_available():
    from .modeling_xlm_prophetnet import (
        XLM_PROPHETNET_PRETRAINED_MODEL_ARCHIVE_LIST,
        XLMProphetNetDecoder,
        XLMProphetNetEncoder,
        XLMProphetNetForCausalLM,
        XLMProphetNetForConditionalGeneration,
        XLMProphetNetModel,
    )
