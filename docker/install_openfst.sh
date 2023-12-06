#!/bin/bash

# Install OpenFst dependencies
apt-get update && apt-get install -y --no-install-recommends \
    libfst-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone and build OpenFst
git clone --branch master --single-branch https://github.com/unicode-org/OpenFst.git
cd OpenFst
autoreconf --force --install
./configure --enable-static --enable-shared
make
make install
