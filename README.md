# Flask + Vue App template

## Description

This a template to quickly set up a flask server with a Vue frontend app.

## Instructions

1. Clone this repository
2. Go into the client folder and install Vue dependencies with `npm install -d`
3. ...Profit

## Details

The idea behind this template is to simplify the creation of a Flask App with a graphical interface built with Vue. This is my preferred set-up as of late when creating dashboards, helper tools or data science applications.

The Flask app and the Vue UI live in the `server` and `client` folders, respectively. In development mode, they can be run independently in ports 5000 and 8080. Once the Vue UI is bundled with `npm run build`, it can be rendered from the Flask API.

## Credits

This template uses the default Vue app created with vue-cli. Thanks to the Vue team for their awesome work.
