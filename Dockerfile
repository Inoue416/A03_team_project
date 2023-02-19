# NOTE:バージョンに特に理由なし、参考したもののバージョンを使っている
FROM python:3.9-alpine3.13

LABEL maintainer="team-Kyushu-danji"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
# HACK:ここの「./app」は仮置き
COPY ./app/ /app/

WORKDIR /app

EXPOSE 8000
    # venv 作成
RUN python -m venv /py && \
    # pipのアップグレード
    /py/bin/pip install --upgrade pip && \
    # パケージをインストール（alpine linuxなどapk（パッケージマネージャー）を使っている）
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    # pythonのパッケージをインストール
    /py/bin/pip install -r /tmp/requirements.txt && \
    # 要らないものを削除
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    # 開発用のユーザ作成
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user