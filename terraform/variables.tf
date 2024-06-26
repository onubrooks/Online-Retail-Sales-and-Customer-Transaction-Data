variable "credentials" {
  description = "Path to the keyfile containing GCP credentials."
  type        = string
  default     = "../mage/retail_sales_etl/secrets/google.json"
}


variable "project" {
  description = "Project"
  default = "zoomcamp-de-411412"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default = "zoomcamp_de_411412_demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default = "zoomcamp-de-411412-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "app_name" {
  type        = string
  description = "Retail Sales Analytics"
  default     = "retailanalytics"
}

variable "project_name" {
  type        = string
  description = "Retail Sales Analytics"
  default     = "retail_sales_etl"
}

variable "container_cpu" {
  description = "Container cpu"
  default     = "2000m"
}

variable "container_memory" {
  description = "Container memory"
  default     = "4G"
}

variable "region" {
  type        = string
  description = "The default compute region"
  default     = "europe-west1"
}

variable "zone" {
  type        = string
  description = "The default compute zone"
  default     = "europe-west1-b"
}

variable "repository" {
  type        = string
  description = "The name of the Artifact Registry repository to be created"
  default     = "mageprod"
}

variable "docker_image" {
  type        = string
  description = "The Docker image url in the Artifact Registry repository to be deployed to Cloud Run"
  default     = "europe-west1-docker.pkg.dev/zoomcamp-de-411412/mageprod/mageprod:linux64"
  # default     = "docker.io/onubrooks/retail_sales_etl-mage"
}

variable "domain" {
  description = "Domain name to run the load balancer on. Used if `ssl` is `true`."
  type        = string
  default     = ""
}

variable "ssl" {
  description = "Run load balancer on HTTPS and provision managed certificate with provided `domain`."
  type        = bool
  default     = false
}
