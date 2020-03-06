const path = require("path");
const argv = require("optimist").argv;

let config = {};
let command = argv["_"][0];
switch (command) {
  case "build":
    config = {
      outputDir: "../dist",
      filenameHashing: true
    };
    break;
  case "serve":
    config = {
      devServer: {
        proxy: "http://localhost:5000"
      }
    };
}

module.exports = config;
