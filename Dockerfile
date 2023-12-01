# Official Python runtime as a parent image
FROM python:3.11

# Enable non-interactive mode during image build
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    automake \
    autoconf \
    libtool \
    g++ \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Clone OpenFst from GitHub
WORKDIR /usr/src
RUN git clone --branch master --single-branch https://github.com/georgepar/openfst-docker.git

# Set the working directory to /usr/src/openfst-docker
WORKDIR /usr/src/openfst-docker

# Install OpenFst dependencies and build OpenFst
RUN ./install_openfst.sh

# Install pyfst
RUN pip install pyfst

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run transliteration script
CMD ["python", "recognize_sol2.py"]
