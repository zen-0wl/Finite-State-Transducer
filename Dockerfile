# Use the official Python runtime as a parent image
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

# Clone OpenFst from GitHub and build it
WORKDIR /usr/src
RUN git clone --branch master --single-branch https://zen-0wl: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@github.com/unicode-org/OpenFst.git

WORKDIR /usr/src/OpenFst
RUN autoreconf --force --install && ./configure --enable-static --enable-shared && make && make install

# Install pyfst
RUN pip install pyfst

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run transliteration script
CMD ["python", "recognize_sol2.py"]
