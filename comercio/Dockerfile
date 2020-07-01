#FROM mcr.microsoft.com/mssql/server:2019-latest
#RUN mkdir /var/opt/mssql/backup
#ADD . /var/opt/mssql/backup
#ENV SA_PASSWORD Abcd1234!
#ENV ACCEPT_EULA Y
#RUN  /opt/mssql/bin/sqlservr & sleep 10
#RUN /opt/mssql-tools/bin/sqlcmd -U SA -P 'Abcd1234!' -Q"RESTORE DATABASE Comercio FROM DISK='/var/opt/mssql/backup/Comercio_Completo';"
FROM jose1522/comercio_sw_ulacit
CMD /opt/mssql/bin/sqlservr