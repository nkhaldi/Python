import json

import time
import argparse
import dataclasses
import random
import shutil

from datetime import datetime, timedelta
from pathlib import Path

_MAX_LOG_SIZE_BYTES = 2 ** 30  # 1GB

_LOG_FILENAMES = 'log_a.jsonl', 'log_b.jsonl'
_LOG_LEVELS = b'DEBUG', b'INFO', b'WARNING', b'ERROR'

_PERSON_NAME = 'Bender', 'Fry', 'Leela', 'Amy', 'Farnsworth', 'Dr. Zoidberg'
_ACTION = 'said', 'took', 'played', 'ate', 'saw', 'built', 'killed', 'created', 'brought', 'robbed'
_OBJECT = 'an apple', 'a car', 'a boat', 'a rocket', 'a mall', 'a fish', 'a bottle of bear', 'a man'
_PLACE = 'at park', 'on the Mars', 'near the Square Garden', 'in L.A.'
_WHEN = 'day before yesterday', 'yesterday', 'today', 'tomorrow', 'day after tomorrow'


@dataclasses.dataclass
class LogRecord:
    log_level: str
    timestamp: str
    message: str


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Tool to generate test logs.')

    parser.add_argument(
        'output_dir',
        metavar='<OUTPUT DIR>',
        type=str,
        help='path to dir with generated logs',
    )

    parser.add_argument(
        '-f', '--force',
        action='store_const',
        const=True,
        default=False,
        help='force write logs',
        dest='force_write',
    )

    return parser.parse_args()


def _create_dir(dir_path: Path, *, force_write: bool = False) -> None:
    if dir_path.exists():
        if not force_write:
            raise FileExistsError(
                f'Dir "{dir_path}" already exists. Remove it first or choose another one.')
        shutil.rmtree(dir_path)

    dir_path.mkdir(parents=True)


_RECORD_TEMPLATE = LogRecord(
    log_level='<LOG_LEVEL>',
    timestamp='<TIMESTAMP>',
    message='<MESSAGE>',
)

_MESSAGE_TEMPLATE = json.dumps(dataclasses.asdict(_RECORD_TEMPLATE)).encode('utf-8')
_MESSAGE_TEMPLATE += b'\n'


def _generate_logfile(log_filepath: Path, start_time: datetime) -> None:
    print(f"generating {log_filepath.name}...")
    person_name, action = _PERSON_NAME, _ACTION
    object, place, when = _OBJECT, _PLACE, _WHEN
    log_levels, message_template = _LOG_LEVELS, _MESSAGE_TEMPLATE
    rand, td, ln = random.random, timedelta, len

    with log_filepath.open('wb') as fh:
        current_time = start_time
        total_size, max_size = 0, _MAX_LOG_SIZE_BYTES
        write = fh.write
        while total_size < max_size:
            timestamp = f"{current_time.year}-{current_time.month:02}-{current_time.day:02} " \
                        f"{current_time.hour}:{current_time.minute:02}:{current_time.second:02}".encode('utf-8')

            message = f"{person_name[int(6 * rand())]} " \
                      f"{action[int(10 * rand())]} " \
                      f"{object[int(8 * rand())]} " \
                      f"{place[int(4 * rand())]} " \
                      f"{when[int(5 * rand())]}".encode('utf-8')

            data = message_template \
                .replace(b'<LOG_LEVEL>', log_levels[int(4 * rand())]) \
                .replace(b'<TIMESTAMP>', timestamp) \
                .replace(b'<MESSAGE>', message)

            write(data)
            total_size += ln(data)
            current_time += td(seconds=int(10 * rand()))


def _generate_logs(output_dir: Path) -> None:
    start_time = datetime.now()

    for log_filename in _LOG_FILENAMES:
        log_path = output_dir.joinpath(log_filename)
        _generate_logfile(log_path, start_time)


def main() -> None:
    args = _parse_args()

    t0 = time.time()
    output_dir = Path(args.output_dir)
    _create_dir(output_dir, force_write=args.force_write)
    _generate_logs(output_dir)
    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == '__main__':
    main()
