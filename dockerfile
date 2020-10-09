# A partir da imagem abaixo
FROM python:3

# Diretório dentro do container que quero trabalhar
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y python3-tk \
    && apt-get clean
RUN pip install jupyter
RUN pip install ipython
RUN pip install pandas
RUN pip install numpy
RUN pip install matplotlib

EXPOSE 8080

CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--port=8080", "--allow-root"]


