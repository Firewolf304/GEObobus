### List
- [Config](#config-)

# Config 
## Example config
Brief information about the config: 
```text
{
  "SERVER" : {                              # server config
    "IP" : "127.0.0.1",                     # service ip
    "PORT" : 8080,                          # service port
    "STATIC_FOLDER" : "/front",             # frontend folder (static files)
    "STATIC_URL_PATH" : "/newmodule",       # service home url
    "ROUTES" : "flaskapp/routes"            # api path folder 
  },
  "DATABASE" : {                                                # sql config
    "HOST" : "127.0.0.1",                                       # db ip
    "PORT" : "5432",                                            # db port
    "USER" : "postgres",                                        # db user
    "PASSWORD" : "postgres",                                    # db password
    "DBNAME" : "postgres",                                      # db name
    "PROTOCOL" : "postgresql",                                  # using db protocol
    "CREATE" : false,                                           # create tables in db
    "REFLECT" : true                                            # reflect tables in db
  },
  "LOGGER" : {                                                  # logging config
    "LOGLEVEL" : "DEBUG",                                       # logging level for logging (from python)
    "FLASK_DEBUG" : false,                                      # run flask debug
    "FILENAME" : "logger.log",                                  # filename log output
    "FORMAT" : "[%(asctime)s] [%(levelname)s] => %(message)s",  # log format
  }
}
```


