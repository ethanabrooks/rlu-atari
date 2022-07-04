#! /usr/bin/env python
import tensorflow as tf
import tensorflow_datasets as tfds
import apache_beam as beam

SPLIT_WEIGHTS = (6, 2, 2)
# splits = tfds.Split.TRAIN.subsplit(weighted=SPLIT_WEIGHTS)
downConfig = tfds.download.DownloadConfig(
    beam_options=beam.options.pipeline_options.PipelineOptions(),
    register_checksums=False,
)
ds = tfds.load(
    "rlu_atari",
    data_dir="/shared/home/ethanbro/tensorflow_datasets/",
    # split=list(splits),
    download_and_prepare_kwargs={"download_config": downConfig},
)
