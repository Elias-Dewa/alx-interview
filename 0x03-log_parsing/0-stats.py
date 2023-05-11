#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics
"""

from sys import stdin


if __name__ == '__main__':

    def parse_log(status_code, file_size):
        status_code = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
        file_size = 0
        count_lines = 0

        print("File size: {:d}".format(file_size))
        for key in sorted(status_code.keys()):
            if status_code[key]:
                print("{}: {:d}".format(key, status_code[key]))

        try:
            for line in stdin:
                if count_lines % 10 == 0 and count_lines != 0:
                    parse_log(status_code, file_size)
                data = line.split()
                if len(data) >= 2:
                    arg = data[-2]
                    if arg in status_code.keys():
                        status_code[arg] += 1
                    file_size += int(data[-1])
            parse_log(status_code, file_size)
        except KeyboardInterrupt as error:
            parse_log(status_code, file_size)
            raise
