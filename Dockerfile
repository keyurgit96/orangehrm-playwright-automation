FROM jenkins/jenkins:lts
USER root

# Install Docker CLI and Git
RUN apt-get update && \
    apt-get install -y docker.io git && \
    rm -rf /var/lib/apt/lists/*

# Configure global Git settings to allow root operations and prevent directory errors
RUN git config --global --add safe.directory '*' && \
    git config --global user.email "jenkins@example.com" && \
    git config --global user.name "Jenkins CI"

USER jenkins