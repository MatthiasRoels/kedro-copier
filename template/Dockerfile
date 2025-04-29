FROM python:3.12-slim

# install packages dependencies
RUN apt-get update \
    && apt-get install -y \
        git \
        make \
        locales
    # clean up
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# https://wiki.debian.org/Locale#Manually
RUN sed -i "s/# en_US.UTF-8/en_US.UTF-8/" /etc/locale.gen \
  && locale-gen
ENV LANG=en_US.UTF-8

# Setup user
ARG user=kedro
ARG group=kedro
ARG uid=1000
ARG gid=1000
ARG HOMEDIR=/home/${user}

ENV HOME ${HOMEDIR}

RUN groupadd -g ${gid} ${group} && \
    useradd -d "${HOMEDIR}" -u "${uid}" -g "${gid}" -m -s /bin/bash "${user}"

# Install uv by copying the binary from the official distroless Docker image
COPY --from=ghcr.io/astral-sh/uv:0.6.17 /uv /uvx /bin/

# set user to kedro
USER ${user}

WORKDIR ${HOMEDIR}/app

# copy requirements file to install
COPY --link --chown=${user}:${user} pyproject.toml uv.lock ./

# Install packages from PyPi using uv
RUN uv sync --no-cache --frozen --no-install-project --no-dev

COPY --link --chown=${user}:${user} . .

CMD ["uv"]

ENTRYPOINT ["run", "--no-sync"]
