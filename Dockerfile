# Official Python image as the base image
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
    && rm -rf /var/lib/apt/lists/*

# Copy OpenFst source code into the container
COPY ./openfst-1.8.2.post1 /usr/src/OpenFst

# Build and install OpenFst
WORKDIR /usr/src/OpenFst
RUN autoreconf --force --install && \
    ./configure --enable-static --enable-shared && \
    make && \
    make install

# Install pyfst
RUN pip install pyfst

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run your Python script
CMD ["python", "recognize_sol2.py"]
