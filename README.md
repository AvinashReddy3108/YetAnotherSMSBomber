![Explosion!!](https://imgur.com/download/FPZPLK9)

## Features
- Lots of integrated SMS APIs, and support for custom API configuration!
- Unlimited number of SMSs (with proxy support for huge bombs!).
- Faster and lighter than most SMS Bomber apps/scripts.
- International bombing available.

## Requirements
- Anything which can run Windows, macOS or Linux and has a keyboard on it.
- Python 3 and PIP installed on it.

## Installation and Setup
It's as easy as typing the below commands into your terminal.
```bash
# Clone my repo
git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber.git

# Move into the work directory.
cd YetAnotherSMSBomber

# Install the requirements via PIP.
pip3 install -r requirements.txt
```

## Options
You can also read this via `python3 bomber.py -h` or `python3 bomber.py --help`

```
YetAnotherSMSBomber - A clean, small and powerful SMS bomber script.

Usage: bomber.py [--config-path/-c] [--num/-N] [--country/-C] [--threads/-T]
                 [--timeout/-t] [--proxy/-P] [--verbose/-v] [--verify/-V]
                 [-h/--help] TARGET

Positional arguments:
  TARGET             Target mobile number without country code.

Optional arguments:
  --config-path, -c  Path to API config file. (NOTE: the file must be in JSON format!) (default: 'api_config.json')
  --num, -N          Number of SMSs to send to TARGET. (default: 30)
  --country, -C      Country code without (+) sign. (default: 91)
  --threads, -T      Max number of concurrent HTTP(s) requests. (default: 15)
  --timeout, -t      Time (in seconds) to wait for an API request to complete. (default: 10)
  --proxy, -P        Use proxy for bombing. (Recommended for large number of SMSs)
  --verbose, -v      Enables verbose output, for debugging.
  --verify, -V       To verify all providers are working or not.
  -h, --help         Display this message.

Use this for fun, not for revenge or bullying!
```

## Examples
```bash
# The default - 25 threads, 50 SMSs, Country Code: +91
python3 bomber.py <TARGET>

# Custom SMS count and proxy.
python3 bomber.py --num 1000 --proxy <TARGET>
python3 bomber.py -N 1000 -P <TARGET>

# Custom API config file and proxy.
python3 bomber.py --config-path "./config.json" --proxy <TARGET>
python3 bomber.py -C "./config.json" -P <TARGET>

# Here's how you use all possible parameters to your taste.
python3 bomber.py --proxy --num 500 --country 91 --timeout 20 <TARGET>
python3 bomber.py -p -N 500 -c 91 -T 30 -t 20 <TARGET>
```

## Credits and Thanks
- Huge kudos to [iMro0t](https://github.com/iMro0t) for the original source code. Find it [here](https://github.com/iMro0t/bomb3r/).
- Thanks [botallen](https://github.com/botallen) for the recent fixes which have been merged from the original repo.
- [SpeedX](https://github.com/TheSpeedX)'s [TBomb](https://github.com/TheSpeedX/TBomb) for some API's used here.
- [fonic](https://github.com/fonic) for his awesome formatter for `argparse`. Check it out in this [gist](https://gist.github.com/fonic/fe6cade2e1b9eaf3401cc732f48aeebd)!

## License
This project is licensed under the [GNU General Public License v3.0](https://github.com/AvinashReddy3108/YetAnotherSMSBomber/blob/master/LICENSE)
