FROM python:3.11-alpine
WORKDIR /apps
COPY . .

RUN  pip install -r req.text

RUN sed -i 's/\r$//g' /apps/entrypoint.sh
RUN chmod +x /apps/entrypoint.sh
ENTRYPOINT ["/apps/entrypoint.sh"]
