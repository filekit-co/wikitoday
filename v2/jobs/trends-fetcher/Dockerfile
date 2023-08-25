FROM python:3.11-slim

ENV PYTHONUNBUFFERED True

# Set ENV
ENV IN_LIBS_PATH=./cp_libs
ENV OUT_LIBS_PATH=/libs
ENV PYTHONPATH=/libs/python:/libs/protobuf

# Create a new user and switch to it
RUN useradd -m wikitoday
USER wikitoday

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Copy lib python code to the container.
# Copy compiled protobuf codes to the container.
COPY $IN_LIBS_PATH /libs/


# Upgrade pip and install production dependencies.
# Since we're now running as a non-root user, we might encounter permission issues. 
# If that's the case, need `--user` flag with pip.
RUN pip install --no-cache-dir --upgrade pip --user
RUN pip install --no-cache-dir -r requirements.txt --user

# @TODO command line
CMD ["/usr/local/bin/python3", "main.py"]