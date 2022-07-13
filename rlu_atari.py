#! /usr/bin/env python
import tensorflow as tf
import tensorflow_datasets as tfds
import apache_beam as beam
import os

# If you are running on Dataflow, Spark,..., you may have to set-up runtime
# flags. Otherwise, you can leave flags empty [].
# flags = ['--runner=DataflowRunner', '--project=rlu-atari',]

# `beam_options` (and `beam_runner`) will be forwarded to `beam.Pipeline`
dl_config = tfds.download.DownloadConfig(
    beam_options=beam.options.pipeline_options.PipelineOptions(
        job_name=f"{os.getenv('GCP_PROJECT')}-gen",
        project=os.getenv("GCP_PROJECT"),
        region="us-east5",
        requirements_file="beam_requirements.txt",
        runner="DataflowRunner",
        staging_location=f"{os.getenv('GCS_BUCKET')}/binaries",
        temp_location=f"{os.getenv('GCS_BUCKET')}/temp",
    )
)
data_dir = f"{os.getenv('GCS_BUCKET')}/tensorflow_datasets"
builder = tfds.builder(os.getenv("DATASET_NAME"), data_dir=data_dir)
builder.download_and_prepare(download_config=dl_config)
ds = builder.as_dataset()
for data in ds["train"]:
    breakpoint()
