# Base image with both Python and Node.js
FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install ffmpeg for audio streaming
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy all files from your local project to the container
COPY . /app/
WORKDIR /app/

# Make sure the start script is executable
RUN chmod +x start

# Optional: Install Python dependencies if requirements.txt exists
RUN [ -f requirements.txt ] && pip3 install --no-cache-dir -U -r requirements.txt || true

# Start the bot using start script
CMD ["bash", "start"]
