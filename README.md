# tc_mongodb
MongoDB storage adapter for thumbor.

# Versions

This projects uses the following versioning scheme:

`<thumbor major>.<mongodb plugin major>.<mongodb plugin minor>`


# Configuration
```
# MONGO STORAGE OPTIONS
Config.define('MONGO_STORAGE_SERVER_HOST', 'localhost', 'MongoDB storage server host', 'MongoDB Storage')
Config.define('MONGO_STORAGE_SERVER_PORT', 27017, 'MongoDB storage server port', 'MongoDB Storage')
Config.define('MONGO_STORAGE_SERVER_DB', 'thumbor', 'MongoDB storage server database name', 'MongoDB Storage')
Config.define('MONGO_STORAGE_SERVER_COLLECTION', 'images', 'MongoDB storage image collection', 'MongoDB Storage')
```
