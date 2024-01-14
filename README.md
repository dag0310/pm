# Particulate Matter Sensor SDS011 Logger

Measure PM2.5 and PM10 values and log them to an API.

## Setup
- `sudo pip3 install -r requirements.txt`
- `./pm.py`
- Set values in `config.ini` according to `config.template.ini`

## System dependencies

- `sudo apt install python3-dev python3-serial`

## Libraries
- Library used: [simple-sds011](https://github.com/krumphauchicken/simple-sds011)
- Alternative library: [sds011lib](https://github.com/TimOrme/sds011lib)