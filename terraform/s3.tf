resource "aws_s3_bucket" "input_bucket" {
  bucket = "event-driven-pipeline-input-shaik-12345"
}

resource "aws_s3_bucket" "output_bucket" {
  bucket = "event-driven-pipeline-output-shaik-12345"
}
