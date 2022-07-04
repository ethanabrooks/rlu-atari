#! /usr/bin/env python
import tensorflow as tf
import tensorflow_datasets as tfds
import apache_beam as beam

# If you are running on Dataflow, Spark,..., you may have to set-up runtime
# flags. Otherwise, you can leave flags empty [].
# flags = ['--runner=DataflowRunner', '--project=rlu-atari',]

# `beam_options` (and `beam_runner`) will be forwarded to `beam.Pipeline`
dl_config = tfds.download.DownloadConfig(
    beam_options=beam.options.pipeline_options.PipelineOptions(
        runner="DataflowRunner",
        project="rlu-atari",
        job_name="download-rlu-atari",
        temp_location="gs://rlu-atari/temp",
        region="us-east5",
    )
)
data_dir = "gs://rlu-atari/tensorflow_datasets"
builder = tfds.builder("rlu_atari", data_dir=data_dir)
builder.download_and_prepare(download_config=dl_config)
