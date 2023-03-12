#!/usr/bin/env python3

import json
import sys


def eprint(err_msg, usage=False):
    print(err_msg, file=sys.stderr)
    if usage:
        usage_msg = "Usage: merge_logs.py <path/to/log1> <path/to/log2> [-o <path/to/merged/log>]"
        print(usage_msg, file=sys.stderr)


def get_log_files():
    try:
        log_a_path = sys.argv[1]
    except (IndexError, ValueError):
        eprint("Log files are not given.", usage=True)
        exit()

    if log_a_path == '-h' or log_a_path == '--help':
        eprint("Merge log files.", usage=True)
        exit()

    try:
        log_b_path = sys.argv[2]
    except (IndexError, ValueError):
        eprint("Not all log files are given.", usage=True)

    try:
        opt = sys.argv[3]
    except (IndexError, ValueError):
        opt = '-d'

    merged_log_path = 'logs/merged_log_path.jsonl'
    if opt == '-o':
        try:
            merged_log_path = sys.argv[4]
        except (IndexError, ValueError):
            eprint("Path to merged log is not given.", usage=True)
    elif opt == '-d' or opt == '--default':
        print(f"Printing merged log into default file {merged_log_path}")
    else:
        eprint(f"Unknown option {opt}.", usage=True)

    return log_a_path, log_b_path, merged_log_path


def get_timestamp(line):
    try:
        json_line = json.loads(line)
        ts = json_line['timestamp']
    except json.decoder.JSONDecodeError:
        eprint(f"Can't decode JSON line: {line}")
        return None
    except KeyError:
        eprint(f"JSON line {line} doesn't have a timestamp")
        return None
    return ts


def get_next_line(log_file):
    line = log_file.readline()
    if not line:
        return None, None

    line = line.strip()
    ts = get_timestamp(line)
    if not ts:
        return None, None

    return line, ts


def print_next_line(line, log_file):
    print(line_a, file=merged_log)
    line, ts = get_next_line(log_file)
    return line, ts


if __name__ == '__main__':
    log_a_path, log_b_path, merged_log_path = get_log_files()

    try:
        log_a = open(log_a_path, 'r')
        log_b = open(log_b_path, 'r')
        merged_log = open(merged_log_path, 'w')
    except (FileNotFoundError, PermissionError) as ex:
        eprint(ex)
        exit()

    line_a, ts_a = get_next_line(log_a)
    line_b, ts_b = get_next_line(log_b)
    while line_a and line_b:
        if ts_a < ts_b:
            line_a, ts_a = print_next_line(line_a, log_a)
        elif ts_a > ts_b:
            line_b, ts_b = print_next_line(line_b, log_b)
        else:
            line_a, ts_a = print_next_line(line_a, log_a)
            line_b, ts_b = print_next_line(line_b, log_b)

    while line_a:
        line_a, ts_a = print_next_line(line_a, log_a)

    while line_b:
        line_b, ts_b = print_next_line(line_b, log_b)

    log_a.close()
    log_b.close()
    merged_log.close()
