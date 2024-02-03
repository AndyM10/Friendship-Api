FROM postgres:latest
ENV POSTGRES_PASSWORD=myfriends
ENV POSTGRES_USER=Andrew
ENV POSTGRES_DB=friends
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
