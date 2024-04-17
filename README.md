# Online Retail Sales and Customer Transaction Data Ingestion and Analysis

This project tackles the challenge of integrating and analyzing retail data from various sources (Kaggle datasets focusing on malls in the UK and Turkey) to glean valuable insights into customer behavior, sales trends, and potential areas for improvement in retail operations.

This is an end to end data pipeline for ingesting, processing, transforming and modelling Online Retail Sales and Customer Transaction Data for analytics and reporting dashboards.

This README document is devided into 4 sections, feel free to skip ahead to any section:
Problem Description
Project Highlights
Project Deep Dive
Reproducing the Project.

## Problem Description

Retailers hold a treasure trove of data within customer transactions and sales figures. But this data often resides in silos, making it difficult to extract valuable insights for strategic decision-making. This project tackles this challenge by building a robust, end-to-end data pipeline.

We leverage data from Kaggle, focusing on retail transactions in malls across the UK and Turkey. By integrating and analyzing this data, we aim to:

* Unify Customer Behavior: Gain a comprehensive understanding of customer buying patterns and preferences across different regions.
* Identify Sales Trends: Uncover hidden trends and seasonality patterns within sales data to optimize inventory management and promotions.
* Drive Operational Efficiency: Pinpoint areas for improvement in retail operations based on data-driven insights.

This project delivers a powerful tool for retailers, transforming scattered data into actionable intelligence that empowers informed decision-making and ultimately, business growth.

## Project Highlights

This project leverages modern cloud technologies and best practices to deliver a robust and scalable data analysis pipeline. Here's a breakdown of the key aspects:

* **Cloud-Native Infrastructure:**
  * Google Cloud Platform (GCP) serves as the foundation for all project components.
    * Infrastructure as Code (IaC) with Terraform manages and provisions cloud resources efficiently and consistently.
* **End-to-End Orchestration:**
  * Mage, a workflow orchestration tool, coordinates the entire data pipeline, ensuring a seamless execution of dependent stages.
    * The pipeline automates data ingestion, transformation, and loading into the data lake and warehouse.
* **Structured Data Storage:**
  * Google Cloud Storage (GCS) acts as the centralized data lake, storing the raw and processed data in a readily accessible format.
    * BigQuery, a columnar data warehouse, houses the transformed data in a structured and optimized manner, enabling fast and efficient queries.
    * Partitioning and clustering techniques are potentially applied to BigQuery tables to optimize query performance based on typical use cases.
* **Advanced Data Transformations:**
  * PySpark, a powerful distributed processing engine, is utilized for data cleaning, feature engineering, and complex transformations on the ingested data.

* **Interactive Data Visualization:**
  * A comprehensive dashboard built with Google Looker Studio, a business intelligence (BI) and data visualization tool, provides interactive insights.
    * The Looker Studio dashboard connects directly to BigQuery, enabling real-time visualizations of key metrics and trends.
* **Reproducible Environment:**
  * Clear instructions within the project's README outline the steps required to set up the cloud environment (using Terraform), deploy the Mage server, and run the data pipeline.
* **Continous Integration/Deployment:**
  * A CI/CD pipeline using Github Actions builds the docker image of the changed mage files, pushes to the Artifact Registry and deploys to Google Cloud Run.

## Project Deep-Dive and Detailed Sections

This section dives deeper into each of the project's core aspects:

See [the details section](https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/blob/main/DETAILS.md) for a technical indepth review of the various project aspects, including screenshot, architecture diagrams, pipelines and more.

## Reproducing the Project

### Install Gcloud and Terraform

* Install `gcloud` SDK and Terraform: This project assumes you already have `gcloud` CLI installed as well as Terraform. If not, you can find installation instructions [here](https://cloud.google.com/sdk) and [here](https://developer.hashicorp.com/terraform/install).
* You will also need to configure Google Cloud Project and Credentials. See [here](https://developers.google.com/workspace/guides/create-project) for more information.
* You will need to configure gcloud Authentication: `gcloud auth activate-service-account --key-file=<PATH_TO_CREDENTIALS_FILE>`

### Create Infrastructure using Terraform

* Clone the project using Github CLI: `gh repo clone onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data`
* cd into the project directory: `cd Online-Retail-Sales-and-Customer-Transaction-Data`
* cd into the terraform directory: `cd terraform`
* Run `terraform init` to setup terraform and `terraform plan` to see the plan and whether your Google account is well set up and everything is in order.
* Run `terraform apply` to create infrastructure on Google cloud.
* If all goes well, your infrastructure is ready to go! Follow the steps for running the mage server and when you are done, run `terraform destroy` to destroy all the cloud resources.

### Run Mage server on Google Cloud

* Go to Google Cloud console at <https://console.cloud.google.com> and search for Cloud Run. Navigate to the Cloud Run page and select the Cloud Run service created by terraform.
* You will find the Cloud Run service URL, visit the site to access the mage server. Here you will find the pipelines contained on this Mage docker image.
* Navigate to 'Pipelines'.
* Select 'retail_sales_etl' pipeline.
* **One important thing**: The Dockerfile creates a file in `/retail_sales_etl/secrets/google.json`. This file is blank and you should copy your credentials JSON file contents into this file. This will enable the server to communicate with Google Cloud services.
* You can choose to run the pipeline manually or trigger the run via API. See example CURL command in [trigger.sh](https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/blob/main/mage/trigger.sh)

### **8. Continous Integration/Deployment**

* A CI/CD pipeline using Github Actions builds the docker image of the changed mage files, pushes to the Artifact Registry and deploys to Google Cloud Run.
* The Github Action script can be found here:  <https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/blob/main/.github/workflows/main.yml>
