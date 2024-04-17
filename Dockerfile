FROM mageai/mageai:latest

ARG PIP=pip3
ARG PROJECT_NAME=retail_sales_etl
ARG MAGE_CODE_PATH=/home/mage
ARG USER_CODE_PATH=${MAGE_CODE_PATH}/${PROJECT_NAME}

WORKDIR ${MAGE_CODE_PATH}

COPY mage/${PROJECT_NAME} ${USER_CODE_PATH}

RUN mkdir ${USER_CODE_PATH}/spark-lib
RUN mkdir ${USER_CODE_PATH}/secrets

# Download gcs-connector-hadoop3-2.2.5.jar
RUN curl -L https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-2.2.5.jar -o ${USER_CODE_PATH}/spark-lib/gcs-connector-hadoop3-2.2.5.jar

# Download spark-3.5-bigquery-0.37.0.jar
RUN curl -L https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases/download/0.37.0/spark-3.5-bigquery-0.37.0.jar -o ${USER_CODE_PATH}/spark-lib/spark-3.5-bigquery-0.37.0.jar

RUN touch ${USER_CODE_PATH}/secrets/google.json

ENV USER_CODE_PATH=${USER_CODE_PATH}

# Install custom Python libraries
RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt

# Add Debian Bullseye repository
RUN echo 'deb http://deb.debian.org/debian bullseye main' > /etc/apt/sources.list.d/bullseye.list

# Install OpenJDK 11
RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk

# Remove Debian Bullseye repository
RUN rm /etc/apt/sources.list.d/bullseye.list

RUN ${PIP} install pyspark

ENV PYTHONPATH="${PYTHONPATH}:/home/mage"

CMD ["/bin/sh", "-c", "/app/run_app.sh"]