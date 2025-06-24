FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install ffmpeg
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy code
COPY . /app/
WORKDIR /app/

# Make sure start script is executable
RUN chmod +x start

# Install Python dependencies (if required)
RUN pip3 install --no-cache-dir -U -r requirements.txt || true

# Start the bot
CMD ["bash", "start"]
