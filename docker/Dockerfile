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

# Set the working directory
WORKDIR /usr/src/OpenFst

# Download and extract the official OpenFst source code
RUN wget https://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.8.2.post1.tar.gz && \
    tar -xzvf openfst-1.8.2.post1.tar.gz --strip-components=1

# Run autoreconf and configure
RUN autoreconf --force --install && \
    ./configure --enable-static --enable-shared && \
    make && \
    make install

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Runs application
CMD ["python", "recognize_sol2.py"]