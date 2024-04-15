"""
    Project: Pana (https://github.com/battleoverflow/pana)
    Author: battleoverflow (https://github.com/battleoverflow)
    License: BSD 2-Clause
"""

import requests
import argparse
from colorama import Fore, Style

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pkg', help="Name of the package", default=None, required=False)
parser.add_argument('-u', '--user', help="Name of the username", default=None, required=False)
args = parser.parse_args()

version = "0.2.1"

banner = \
f"""
 ____  _____ ____  _____ 
|  _ \(____ |  _ \(____ |
| |_| / ___ | | | / ___ |
|  __/\_____|_| |_\_____|
|_|

   battleoverflow | v{version}
"""

class Pana:

    def check_pkg(pkg_name: str) -> list:

        pkg_config = {
            "pypi": f"https://pypi.org/project/{pkg_name}",
            "npm": f"https://www.npmjs.com/package/{pkg_name}",
            "nuget": f"https://www.nuget.org/packages/{pkg_name}",
            "crates/docs": f"https://docs.rs/crate/{pkg_name}",
        }

        pkg_arr = []

        if args.pkg is not None:
            print(f"\n{Fore.BLUE}Checking package:{Style.RESET_ALL} {args.pkg}")

        for p in pkg_config:
            response = requests.get(pkg_config[p])

            if response.status_code == 200:
                if args.pkg is not None:
                    print(f"[{Fore.RED}{p}{Style.RESET_ALL}] Package name taken")
                
                pkg_arr.append([p, False])

            if response.status_code == 404:
                if args.pkg is not None:
                    print(f"[{Fore.GREEN}{p}{Style.RESET_ALL}] Package name available")
                
                pkg_arr.append([p, True])
        
        return pkg_arr

    def check_user(user: str) -> list:

        user_config = {
            "pypi": f"https://pypi.org/user/{user}",
            "npm": f"https://www.npmjs.com/~{user}",
            "nuget": f"https://www.nuget.org/profiles/{user}",
            "crates/docs": f"https://github.com/{user}"
        }

        pkg_arr = []

        if args.user is not None:
            print(f"\n{Fore.BLUE}Checking username:{Style.RESET_ALL} {args.user}")

        for p in user_config:
            response = requests.get(user_config[p])

            if response.status_code == 200:
                if args.user is not None:
                    print(f"[{Fore.RED}{p}{Style.RESET_ALL}] Username taken")
                
                pkg_arr.append([p, False])

            if response.status_code == 404:
                if args.user is not None:
                    print(f"[{Fore.GREEN}{p}{Style.RESET_ALL}] Username available")
                
                pkg_arr.append([p, True])
            
        return pkg_arr

    def main():
        print(banner)

        if args.pkg is not None:
            Pana.check_pkg(args.pkg)

        if args.user is not None:
            Pana.check_user(args.user)


if __name__ == "__main__":
    Pana.main()
