#! /usr/bin/env python
import tensorflow as tf
import tensorflow_datasets as tfds
import apache_beam as beam

# If you are running on Dataflow, Spark,..., you may have to set-up runtime
# flags. Otherwise, you can leave flags empty [].
# flags = ['--runner=DataflowRunner', '--project=rlu-atari',]

# `beam_options` (and `beam_runner`) will be forwarded to `beam.Pipeline`

name = "rlu_atari_checkpoints_ordered"
gcp_project = "rlu-atari"
gcs_bucket = "gs://rlu-atari"

dl_config = tfds.download.DownloadConfig(
    beam_options=beam.options.pipeline_options.PipelineOptions(
        job_name=f"{gcp_project}-gen",
        project=gcp_project,
        region="us-east5",
        requirements_file="beam_requirements.txt",
        runner="DataflowRunner",
        staging_location=f"{gcs_bucket}/binaries",
        temp_location=f"{gcs_bucket}/tmp",
    )
)
data_dir = f"{gcs_bucket}/tensorflow_datasets"
builder = tfds.builder(name, data_dir=data_dir)
builder.download_and_prepare(download_config=dl_config)
ds = builder.as_dataset()
for data in ds["train"].batch(8):
    print(
        "checkpoint_id",
        data["checkpoint_id"].numpy(),
        "episode_id",
        data["episode_id"].numpy(),
    )
    breakpoint()
