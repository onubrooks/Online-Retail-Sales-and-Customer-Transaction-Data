# Project Deep-Dive and Detailed Sections

This section dives deeper into each of the project's core aspects:

## **1. Data Acquisition and Ingestion**

This section dives into how we gather and integrate retail sales and customer transaction data from Kaggle.

1.1. Kaggle Datasets and Relevance
The project utilizes data from four carefully chosen Kaggle datasets, each contributing valuable insights to our analysis:

Dataset 1 ([UK Online Retail Sales and Customer Transaction Data](https://www.kaggle.com/datasets/thedevastator/online-retail-transaction-data/data)): This data set provides an in-depth look at transactions, product details, and customer information documented by an online retail company based in the UK. The scope of the data spans vastly, from granular details about each product sold to extensive customer data sets from different countries.

Dataset 2 ([Customer Shopping Dataset - Retail Sales Data](https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset)): Contains shopping information from 10 different shopping malls between 2021 and 2023. This data is gathered from various age groups and genders to provide a comprehensive view of shopping habits in Istanbul.

Dataset 3 ([Online Retail Dataset](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)): Transactions of a UK-based non-store online retail

Dataset 4 ([Online Retail Dataset](https://www.kaggle.com/datasets/divanshu22/online-retail-dataset)): The Online Retail Dataset consists of records about retail transactions conducted online. It contains information about customer purchases, including the invoice number, stock code, description of the items purchased, quantity, unit price, invoice date, customer ID, and country.

By combining data from these diverse sources, we gain a richer understanding of customer behavior, sales trends, and overall retail operations across different regions (UK and Turkey).

1.2. Download Process
The data download process leverages the Python requests library, a versatile tool for making HTTP requests. Within our Mage workflow, a dedicated stage is responsible for fetching the data from the following dataset URLs:

[URL 1](https://storage.googleapis.com/public-project-dataset/1_UK%20Online%20Retail%20Sales%20and%20Customer%20Transaction%20Data.zip)
[URL 2](https://storage.googleapis.com/public-project-dataset/2_Market%20Basket%20Analysis%20in%20Istanbul%20Retail%20Data.zip)
[URL 3](https://storage.googleapis.com/public-project-dataset/3_Transactions%20of%20a%20UK-based%20non-store%20online%20retail.zip)
[URL 4](https://storage.googleapis.com/public-project-dataset/4_Online%20Retail%20Dataset%20Exploring%20E-commerce%20Transactions%20and%20Customer%20Behavior.zip)

Note: In order to avoid the complexity of using the Kaggle API and authentication, these datasets were downloaded manually from Kaggle and uploaded to a publicly accessible GCP bucket.

This Mage stage interacts with the Kaggle API to securely retrieve the data files. Downloaded files are then staged within the pipeline for further processing.

## **2. Cloud Infrastructure with Terraform**

This section delves into the infrastructure layer of our project, built and managed using Terraform, an Infrastructure as Code (IaC) tool.

<img width="577" alt="Screenshot 2024-04-17 at 15 47 00" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/c8d02b9a-ba61-48b1-8e41-fc6ccb07c663">


### 2.1. Terraform Configuration and Provisioned Resources

Terraform configuration files (.tf files) define the cloud resources required for the data pipeline. These files are version-controlled and reusable, ensuring a consistent and manageable infrastructure setup. Here's an overview of the resources typically provisioned by Terraform in this project:

* **Cloud Storage Buckets:** Terraform creates one or more Cloud Storage buckets to store the raw and processed data files used throughout the pipeline.
* **BigQuery Datasets and Tables:** BigQuery datasets and tables are defined within Terraform configurations, specifying the schema and structure for the data to be stored in BigQuery.
* **Cloud Run Service for Mage Server:** Terraform provisions a Cloud Run service to deploy and manage the Mage server container image. This service allows us to run the Mage workflow orchestration engine in a scalable and serverless manner.

<img width="776" alt="Screenshot 2024-04-17 at 15 40 25" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/b4782e17-308a-4955-99c7-39620d8cc7fb">


### 2.2. Benefits of Infrastructure as Code (IaC)

Utilizing IaC with Terraform offers several advantages:

* **Repeatable Infrastructure:** Terraform configurations ensure consistent infrastructure provisioning across different environments (development, staging, production).
* **Version Control and Collaboration:**  Configuration files are version-controlled, allowing for easy tracking of changes and collaboration among team members.
* **Reduced Errors:** Defining infrastructure in code minimizes manual configuration errors and promotes a more reliable deployment process.
* **Scalability and Automation:** Terraform enables infrastructure scaling and management through code, simplifying infrastructure adjustments as needed.

By leveraging IaC with Terraform, we establish a robust and manageable foundation for our data analysis pipeline within Google Cloud Platform.

## **3. Workflow Orchestration with Mage**

This section explores the heart of our data pipeline – the workflow orchestration powered by Mage. Mage is a user-friendly tool that streamlines the execution of complex data processing tasks in a defined sequence.

### 3.1. Mage Workflow Structure

The Mage workflow is structured as a series of interconnected stages, each encapsulating a specific data processing step. Here's a breakdown of the typical stages involved:

<img width="1373" alt="Screenshot 2024-04-17 at 15 49 02" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/6fce56cd-44d0-491b-9ac3-382d86ea46f4">


1. **Data Acquisition:** This stage utilizes the `requests` library (or similar tool) to download the Kaggle datasets from their respective URLs. Downloaded files are staged within a designated location.
2. **Data Preprocessing:** This stage includes tasks like cleaning the raw data, handling missing values, or formatting the data to adhere to a specific schema.
3. **Data Transformation:** The PySpark engine takes center stage here. Complex transformations, aggregations, and feature engineering are applied to the preprocessed data using PySpark functionalities.
4. **Data Validation:** This stage can involve data quality checks to ensure the transformed data meets defined criteria before loading it into GCS and BigQuery.
5. **Data Loading to GCS:** The processed data is uploaded to a Cloud Storage bucket for persistence and potential future use.
6. **Data Loading to BigQuery:** The transformed data is loaded into BigQuery datasets and tables defined within the Terraform configuration.

### 3.2. Managing Dependencies and Ensuring Execution Flow

Mage excels at handling dependencies between workflow stages. Each stage can explicitly declare its dependencies on other stages it requires to run successfully. This ensures a logical execution order, where a stage only starts after all its preceding dependencies have completed without errors.

<img width="713" alt="Screenshot 2024-04-17 at 15 50 50" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/4b5f5473-1c5c-4b62-a0b2-cb6a1948144e">


Mage also offers features for error handling and retry logic. If a stage encounters an issue, Mage can be configured to attempt retries or notify designated personnel for intervention. This ensures the overall pipeline's robustness and minimizes disruptions.

By leveraging Mage's orchestration capabilities, we establish a well-defined, automated, and reliable data processing pipeline for our retail sales and customer transaction data analysis project.

## **4. Data Transformation with PySpark**

PySpark, a powerful distributed processing engine, plays a pivotal role in transforming the raw data into a structured and analytical format. This section delves into the key PySpark transformations applied within our data pipeline.

**Data Loading and Configuration:**

The provided code snippet showcases the initial steps for setting up the PySpark environment and accessing BigQuery data. It leverages Spark's integration with Google Cloud Storage (GCS) to establish authentication and read data from BigQuery tables specified in the `bq_table_names` list.

**Data Merging and Deduplication:**

* The `union_and_drop_duplicates` function combines data from multiple BigQuery tables into a single DataFrame.
* This function also removes duplicate records within the merged DataFrame to ensure data integrity.

**Data Cleaning:**

* The `clean_data` function is responsible for cleaning and preparing the data for further analysis. This involves tasks like:
  * Handling missing values (e.g., filling with appropriate values or removing rows with too many missing entries).
  * Identifying and correcting data inconsistencies or errors.
  * Standardizing data formats (e.g., converting dates to a consistent format).
  * Deriving new features based on existing data columns.

**Data Validation:**

Data validation steps are integrated within a separate stage. These steps could involve:

* Checking for data type consistency.
* Ensuring data adheres to defined business rules.
* Identifying and addressing any data quality issues before loading the transformed data into BigQuery.

**Data Writing to BigQuery:**

The final step involves writing the cleaned and transformed data back to BigQuery using the `write_to_bigquery` function. This function specifies the target BigQuery table (`bq_output_table`) to store the processed data.

By leveraging PySpark's capabilities, we clean, transform, and enrich the raw data, preparing it for advanced analytics and insights generation.

## **5. Data Warehousing with BigQuery**

BigQuery serves as the central data warehouse for our project, storing the transformed and enriched data in a structured and optimized manner. This section explores the BigQuery schema design and optimization techniques employed.

### 5.1. BigQuery Schema Design

The data pipeline transforms the raw data into multiple BigQuery tables, each catering to specific analysis needs. Here's the final table schema design:

<img width="1007" alt="Screenshot 2024-04-17 at 15 44 16" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/1094cd45-46a3-42e8-8cb7-6d11adf083b8">


* **Sales Transaction Table:**
  * `customer_id`: Unique identifier for the customer (if available).
  * `invoice_no`: Unique identifier for the sales invoice.
  * `invoice_date`: Date of the sales transaction.
  * `stock_code`: Unique identifier for the product.
  * `description`: Description of the product.
  * `category`: Category of the product (e.g., clothing, electronics).
  * `customer_country`: Country of the customer (if available).
  * `gender`: Gender of the customer (if available).
  * `unit_price`: Unit price of the product.
  * `quantity`: Quantity of the product purchased.
  * `payment_method`: Payment method used for the transaction (e.g., credit card, cash).

* **Aggregated Sales Tables:**
  * This tables stores pre-aggregated sales data based on specific business requirements.
  * Four analytics tables were created as detailed in the Looker analytics dashboard section below.
 
<img width="980" alt="Screenshot 2024-04-17 at 15 43 11" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/818f2eab-ccca-48c5-90e6-3e732a459e3d">


**Data Definition Language (DDL):**

The PySpark script utilizes the `createOrReplaceTempView` function to create temporary views representing the transformed data. These views can then be used within SQL queries to write the data to permanent BigQuery tables defined using BigQuery's DDL statements.

### 5.2. Partitioning and Clustering

For improved query performance on frequently accessed data subsets, BigQuery offers partitioning and clustering techniques. Here's a breakdown of their potential application in this project:

* **Partitioning:**
  * The data has a natural time component, `invoice_date` in the sales transaction table, partitioning by date can significantly improve query performance when filtering or aggregating data for specific date ranges.
  * BigQuery supports partitioning by a single timestamp or date field.

* **Clustering:**
  * Clustering groups data together based on frequently used query filters or joins. This can be beneficial if your queries often involve specific combinations of columns. Here we cluster by the `category` column.
  * BigQuery allows clustering by up to four columns.

## **6. Data Visualization with Looker Studio**

The dashboard is live [here](https://lookerstudio.google.com/u/0/reporting/f0239093-6349-4806-83b1-20e81e8de904/page/zcIvD). We captured the following metrics:

### Shopping Trends by Demographics and Payment Methods

* Identify which customer segments (country, age, gender) contribute most to sales.
* Understand preferred payment methods for different demographics.
* Visualisation: A stacked bar chart with customer country on the x-axis, and total sales on the y-axis. Segments within each country can be further broken down by age category, gender, and payment method using color or stacking.

<img width="710" alt="Screenshot 2024-04-17 at 14 33 44" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/107e161a-6ea5-4f2e-a70f-7b1a74c62ca9">


### Analyze Product Category Performance

* Determine which product categories generate the most sales and revenue.
* Identify potential areas for product development or marketing focus.
* Visualisation: A pie(donought) chart with product category on the x-axis and total revenue on the y-axis. Represents the data proportionally to show the contribution of each category to overall sales.

<img width="536" alt="Screenshot 2024-04-17 at 14 33 58" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/a861adcb-cba6-48ed-ba48-e2d00d3dcba7">


### Explore Product Performance Across Shopping Malls

* Discover top-selling products in each shopping mall over time.
* Identify trends in product popularity across different malls.
* Visualisation: A line chart with invoice date on the x-axis and total sales on the y-axis. Uses different lines to represent each shopping mall. Overlays another line chart on the same graph (secondary y-axis) to show total quantity sold for comparison.

<img width="663" alt="Screenshot 2024-04-17 at 14 34 17" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/ccde611b-8d94-45df-bfc4-9a6ce4b0a6f7">


### Investigate Customer Purchase Behavior

* Segment customers based on purchase frequency and total spending.
* Identify potential high-value customers for targeted marketing efforts.
* Visualisation: A scatter plot with purchase frequency on the x-axis and total amount spent on the y-axis. Color-code data points based on customer country or another relevant category.

<img width="523" alt="Screenshot 2024-04-17 at 14 34 30" src="https://github.com/onubrooks/Online-Retail-Sales-and-Customer-Transaction-Data/assets/26160845/ceaaffed-8631-44d9-8fcf-9197fb5db909">

The dashboard is live [here](https://lookerstudio.google.com/u/0/reporting/f0239093-6349-4806-83b1-20e81e8de904/page/zcIvD).

## **7. Bonus: Building Docker Image and Pushing to the Artifact Registry**

At the root of the project is a Dockerfile containing all the Mage code. This file can be used to build a docker image locally or on cloud build and the resulting image will be added to the `variables.tf` file in the terraform folder as the docker image to be deployed on Google Cloud Run. Setting up is very straightforward:

### Building Locally

Because the mage user code is located in the `retail_sales_etl` folder, we'll use it as our project name.
Build the image: `docker build --tag <image>:<tag> .`

Run image: `docker run -it -p 6789:6789 <image>:<tag> /app/run_app.sh mage start retail_sales_etl`

Visit: localhost:6789 and make sure that it's working.

Note: GCP artifact redistry uses linux64 only so we need to use linux64 if running on a Mac computer:
`docker build --platform linux/amd64 --tag <image>:<tag> .`

Set up artifact registry on your Google cloud account using this link: https://docs.mage.ai/production/deploying-to-cloud/gcp/gcp-artifact-registry

### Building on Google Cloud Build

After setting up your artifact registry and region, run the following command:

`gcloud builds submit \
  --region=<region> \
  --tag=<region>-docker.pkg.dev/<project-id>/<repository>/<image:tag> \
    .`

After this is successful, replace the variable for container image in your `variables.tf` file with the new image.

```tf
variable "docker_image" {
  type        = string
  description = "The Docker image url in the Artifact Registry repository to be deployed to Cloud Run"
  default     = "<region>-docker.pkg.dev/<project-id>/<repository>/<image:tag>"
}
```

You can also deploy the image to your Docker account:

Login: `docker login`
Build: `docker tag <image:tag> <docker-username>/<image:tag>`
Push: `docker push <docker-username>/<image:tag>`
