#!/bin/bash
pip3 install -r requirements.txt

echo "python3 main.py \$@" | tee cryptohttp
chmod +x cryptohttp
