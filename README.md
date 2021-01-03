![Explosion!!](https://imgur.com/download/FPZPLK9)

## Features
- Lots of integrated SMS APIs, and support for custom API configuration!
- Unlimited number of SMSs (with proxy support for huge bombs!).
- Faster and lighter than most SMS Bomber apps/scripts.
- International bombing available.

## Requirements
- Python 3.6+ on MacOS, Android ([Termux](https://termux.com)), Linux, or iOS ([iSH](https://testflight.apple.com/join/97i7KM8O0))

NOTE: Windows not supported as some of `httpx`'s `http2` libraries can't be installed on it.

## Instructions for MacOS
```bash
# Install brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install Dependencies
brew install git
brew install python3
sudo easy_install pip
sudo pip install --upgrade pip

# Clone this repo
git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber.git

# Move into working directory.
cd YetAnotherSMSBomber

# Install the requirements.
pip3 install -r requirements.txt
```

## Instructions for Android

Download Termux from the [Play Store](https://play.google.com/store/apps/details?id=com.termux)

Open Termux and enter the following commands:

```bash
# Install Dependencies:
pkg install git python -y

# Clone this repo
git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber.git

# Move into working directory.
cd YetAnotherSMSBomber

# Install the requirements.
pip3 install -r requirements.txt
```

## Instructions for iOS/iPadOS(due to the way Apple devices handle ram usage it's gonna be slow but it works :P)

Download iSH from [here](https://testflight.apple.com/join/97i7KM8O0)

Open iSH and enter the following commands:

```bash
# Install Dependencies:
apk add git
apk add python3
apk add py3-pip

# Clone this repo
git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber.git

# Move into working directory.
cd YetAnotherSMSBomber

# Install the requirements.
pip3 install -r requirements.txt
```

## Instructions for Debian-based GNU/Linux distributions:

```bash
# Install Dependencies:
sudo apt install git python3 python3-pip

# Clone this repo
git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber.git

# Move into working directory.
cd YetAnotherSMSBomber

# Install the requirements.
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
python3 bomber.py -c "./config.json" -P <TARGET>

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
