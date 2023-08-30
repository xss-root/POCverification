import argparse
from utils.task_manager import TaskManager

def title():
    title = r"""
  ____                __    __
 |  _ \ ___   ___     \ \  / /
 | |_) / _ \ / __|     \ \/ /
 |  __/ (_) | (__       \ \/
 |_|   \___/ \___|      /\ \
                       /_/\_\                       
@Author: xss-root       @From:  https://github.com/xss-root 
    """
    print(title)

def main():
    title()
    parser = argparse.ArgumentParser(description="QuickPocSuite v0.0.1-beta By:W01fh4cker")
    parser.add_argument("-y", "--yaml", help="the YAML file containing the PoC")
    parser.add_argument("-l", "--list", help="the file containing target URLs")
    parser.add_argument("-t", "--thread", type=int, help="the maximum time in seconds for each request,default: 20", required=False, default=20)
    parser.add_argument("-o", "--output", help="the file to output the results, default: output.txt", required=False, default="output.txt")

    args = parser.parse_args()
    TaskManager(args.yaml, args.list, args.thread, args.output).task_apply()

if __name__ == "__main__":
    main()