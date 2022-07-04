#! /usr/bin/env python
import tensorflow_datasets as tfds
dl_config = tfds.download.DownloadConfig(
beam_options=beam.options.pipeline_options.PipelineOptions(flags=[]),
compute_stats=tfds.download.ComputeStatsMode.SKIP)
builder = tfds.builder("tedlium/release3", data_dir="./datasets")
logger.info(f"info: {builder.info}")
builder.download_and_prepare(
download_dir="./downloads",
download_config=dl_config)
