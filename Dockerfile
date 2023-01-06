FROM mambaorg/micromamba

# Define variables
ARG PORT=3000
WORKDIR /code

# Expose port for the server
EXPOSE ${PORT}

#Spinup the environment
COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

COPY ./src /code/app
