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
        path_a = sys.argv[1]
    except (IndexError, ValueError):
        eprint("Log files are not given.", usage=True)
        exit()

    if path_a == '-h' or path_a == '--help':
        eprint("Merge log files.", usage=True)
        exit()

    try:
        path_b = sys.argv[2]
    except (IndexError, ValueError):
        eprint("Not all log files are given.", usage=True)

    try:
        opt = sys.argv[3]
    except (IndexError, ValueError):
        opt = '-d'

    path_merged = 'logs/path_merged.jsonl'
    if opt == '-o':
        try:
            path_merged = sys.argv[4]
        except (IndexError, ValueError):
            eprint("Path to merged log is not given.", usage=True)
    elif opt == '-d' or opt == '--default':
        print(f"Printing merged log into default file {path_merged}")
    else:
        eprint(f"Unknown option {opt}.", usage=True)

    return path_a, path_b, path_merged


def open_log_files(path_a, path_b, path_merged):
    try:
        log_a = open(path_a, 'r')
        log_b = open(path_b, 'r')
        merged_log = open(path_merged, 'w')
    except (FileNotFoundError, PermissionError) as ex:
        eprint(ex)
        exit()

    return log_a, log_b, merged_log


def close_log_files(log_a, log_b, merged_log):
    log_a.close()
    log_b.close()
    merged_log.close()


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


def print_next_line(line, log_file, merge_file):
    print(line, file=merge_file)
    line, ts = get_next_line(log_file)
    return line, ts


def merge_logs(log_a, log_b, merge_file):
    line_a, ts_a = get_next_line(log_a)
    line_b, ts_b = get_next_line(log_b)

    while line_a and line_b:
        # Используем 2 отдельных if подряд, чтобы в случае,
        # когда у логов одинаковое время (ts_a == ts_b),
        # записать оба лога по очереди
        if ts_a <= ts_b:
            line_a, ts_a = print_next_line(line_a, log_a, merge_file)
        if ts_a >= ts_b:
            line_b, ts_b = print_next_line(line_b, log_b, merge_file)

    while line_a:
        line_a, ts_a = print_next_line(line_a, log_a, merge_file)

    while line_b:
        line_b, ts_b = print_next_line(line_b, log_b, merge_file)


if __name__ == '__main__':
    path_a, path_b, path_merged = get_log_files()
    log_a, log_b, merged_log = open_log_files(path_a, path_b, path_merged)
    merge_logs(log_a, log_b, merged_log)
    close_log_files(log_a, log_b, merged_log)
