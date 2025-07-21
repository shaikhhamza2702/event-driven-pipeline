resource "aws_s3_bucket" "input_bucket" {
  bucket = "event-driven-pipeline-input"
}

resource "aws_s3_bucket" "output_bucket" {
  bucket = "event-driven-pipeline-output"
}
