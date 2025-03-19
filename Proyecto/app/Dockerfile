# syntax=docker/dockerfile:1

FROM python:3.12-alpine

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN apk add --no-cache gcc musl-dev linux-headers imagemagick
RUN pip install -r requirements.txt
RUN ln -s /usr/lib/libMagickCore-7.Q16HDRI.so.10.0.2 /usr/lib/libMagickCore-7.Q16HDRI.so
RUN ln -s /usr/lib/libMagickWand-7.Q16HDRI.so.10.0.2 /usr/lib/libMagickWand-7.Q16HDRI.so

EXPOSE 5000