#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics
"""

from sys import stdin


if __name__ == '__main__':

    def parse_log(status_code, file_size):
        status_code = {
            "200": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0,
        }
        file_size = 0
        count_lines = 0

        print("File size: {:d}".format(file_size))
        for key, value in status_code.items():
            if value:
                print("{}:{:d}".format(key, value))

        try:
            for line in stdin:
                if count_lines % 10 == 0 and count_lines != 0:
                    parse_log(status_code, file_size)
                count_lines += 1
                data = line.split(" ")
                if len(data) >= 2:
                    arg = data[-2]
                    if arg in status_code:
                        status_code[arg] += 1
                    file_size += int(data[-1])
                parse_log(status_code, file_size)
        except KeyboardInterrupt as error:
            print(status_code, file_size)
            raise
