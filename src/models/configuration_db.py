# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
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
""" RoBERTa configuration """


import logging

### dont remove BERT
from .configuration_bert import BertConfig


logger = logging.getLogger(__name__)

DISTILBERT_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "distilbert-base-uncased": "https://huggingface.co/distilbert-base-uncased/resolve/main/config.json",
    "distilbert-base-uncased-distilled-squad": (
        "https://huggingface.co/distilbert-base-uncased-distilled-squad/resolve/main/config.json"
    ),
    "distilbert-base-cased": "https://huggingface.co/distilbert-base-cased/resolve/main/config.json",
    "distilbert-base-cased-distilled-squad": (
        "https://huggingface.co/distilbert-base-cased-distilled-squad/resolve/main/config.json"
    ),
    "distilbert-base-german-cased": "https://huggingface.co/distilbert-base-german-cased/resolve/main/config.json",
    "distilbert-base-multilingual-cased": (
        "https://huggingface.co/distilbert-base-multilingual-cased/resolve/main/config.json"
    ),
    "distilbert-base-uncased-finetuned-sst-2-english": (
        "https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english/resolve/main/config.json"
    ),
}


class DistilBertConfig(BertConfig):
	r"""
		This is the configuration class to store the configuration of an :class:`~transformers.RobertaModel`.
		It is used to instantiate an RoBERTa model according to the specified arguments, defining the model
		architecture. Instantiating a configuration with the defaults will yield a similar configuration to that of
		the BERT `bert-base-uncased <https://huggingface.co/bert-base-uncased>`__ architecture.

		Configuration objects inherit from  :class:`~transformers.PretrainedConfig` and can be used
		to control the model outputs. Read the documentation from  :class:`~transformers.PretrainedConfig`
		for more information.

		The :class:`~transformers.RobertaConfig` class directly inherits :class:`~transformers.BertConfig`.
		It reuses the same defaults. Please check the parent class for more information.

		Example::

			from transformers import RobertaConfig, RobertaModel

			# Initializing a RoBERTa configuration
			configuration = RobertaConfig()

			# Initializing a model from the configuration
			model = RobertaModel(configuration)

			# Accessing the model configuration
			configuration = model.config

		Attributes:
			pretrained_config_archive_map (Dict[str, str]):
				A dictionary containing all the available pre-trained checkpoints.
	"""
	pretrained_config_archive_map = DISTILLBERT_PRETRAINED_CONFIG_ARCHIVE_MAP
	model_type = "distilbert"

	def __init__(self, pad_token_id=1, bos_token_id=0, eos_token_id=2, **kwargs):
		"""Constructs FlaubertConfig.
		"""
		super().__init__(pad_token_id=pad_token_id, bos_token_id=bos_token_id, eos_token_id=eos_token_id, **kwargs)




