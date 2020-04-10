![Explosion!!](https://imgur.com/download/FPZPLK9)

## Features
- Lots of integrated SMS APIs.
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
usage: bomber.py [-h] [--sms SMS] [--threads THREADS] TARGET

positional arguments:
  TARGET                    Target mobile number without country code (default:+91)

optional arguments:
  -h, --help                show this help message and exit
  --sms SMS, -S SMS         Number of sms to target (default: 5000)
  --country COUNTRY, -c COUNTRY
                        Country code without (+) sign (default: 91)
  --threads THREADS, -T THREADS
                            Number of threads (default: 25)
  --proxy, -p           Use proxy for bombing (It is advisable to use this
                          option if you are bombing more than 5000 sms)
  --verbose, -v         Verbose
  --verify, -V          To verify all providers are working or not
```

## Examples
```bash
# The Classic - 25 threads, 50 SMSs, Country Code: +91
python3 bomber.py <TARGET>

# Classic + Proxy
python3 bomber.py --proxy <TARGET>
python3 bomber.py -p <TARGET>

# Here's how you use all possible parameters to your taste.
python3 bomber.py --proxy --sms 500 --country 91 <TARGET>
python3 bomber.py -p -S 500 -c 91 -T 30 <TARGET>
```

## Credits and Thanks
- Huge kudos to [iMro0t](https://github.com/iMro0t) for the original source code. Find it [here](https://github.com/iMro0t/bomb3r/).
- Thanks [botallen](https://github.com/botallen) for the recent fixes which have been merged from the original repo.
- [SpeedX](https://github.com/TheSpeedX)'s [TBomb](https://github.com/TheSpeedX/TBomb) for some API's used here.

## License
This project is licensed under the [GNU General Public License v3.0](https://github.com/AvinashReddy3108/YetAnotherSMSBomber/blob/master/LICENSE)
