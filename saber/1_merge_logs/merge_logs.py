#!/usr/bin/env python3

import json


def get_timestamp(line):
    try:
        json_line = json.loads(line)
        ts = json_line['timestamp']
    except json.decoder.JSONDecodeError:
        print(f"Can't decode JSON line: {line}")
        return None
    except KeyError:
        print(f"JSON line {line} doesn't have a timestamp")
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
    print(line_a, file=merged_log_file)
    line, ts = get_next_line(log_file)
    return line, ts


if __name__ == '__main__':
    log_a_path = 'logs/log_a.jsonl'
    log_b_path = 'logs/log_b.jsonl'
    merged_log_path = 'logs/merged_log.jsonl'

    try:
        log_a_file = open(log_a_path, 'r')
        log_b_file = open(log_b_path, 'r')
        merged_log_file = open(merged_log_path, 'w')
    except (FileNotFoundError, PermissionError) as ex:
        print(ex)
        exit()

    line_a, ts_a = get_next_line(log_a_file)
    line_b, ts_b = get_next_line(log_b_file)
    while line_a and line_b:
        if ts_a < ts_b:
            line_a, ts_a = print_next_line(line_a, log_a_file)
        elif ts_a > ts_b:
            line_b, ts_b = print_next_line(line_b, log_b_file)
        else:
            line_a, ts_a = print_next_line(line_a, log_a_file)
            line_b, ts_b = print_next_line(line_b, log_b_file)

    while line_a:
        line_a, ts_a = print_next_line(line_a, log_a_file)

    while line_b:
        line_b, ts_b = print_next_line(line_b, log_b_file)

    log_a_file.close()
    log_b_file.close()
    merged_log_file.close()
