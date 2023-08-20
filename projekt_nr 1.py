from csv import DictReader
from typing import Dict

import click




class Entry:
    def __init__(self, desc: str, time: int, tags: list[str]):
        self.desc = desc
        self.time = time
        self.tags = tags
        
    def __repr__(self):
        return f'Entry(description={self.desc!r}, time={self.time!r}), tags={self.tags!r}'
    
    def __str__(self):
        tags = [f'#{t}' for t in self.tags]
        tags = ' '.join(tags)
        return f'{self.desc} ({self.time} min) {tags}'
    

def build_entry_from_dict(row: Dict[str, str]) -> Entry:
    tags = row['tags'].split(' ')
    entry = Entry(
        desc=row['desc'].strip(),
        time=int(row['time'].strip()),
        tags=tags,
    )
    return entry


def load_entries(csv_file: str) -> list[Entry]:
    with open(csv_file) as stream:
        reader = DictReader(stream)
        entries = [build_entry_from_dict(row) for row in reader]
    return entries


def compute_total_time_by_tags(entries: list[Entry]) -> Dict[str, int]:
    tags = {t for e in entries for t in e.tags}
    report={}
    for tag in tags:
        total = sum([e.time for e in entries if tag in e.tags])
        report[tag] = total
    return report


def display_report_by_tags(time_by_tags: Dict[str,int]) -> None:
    print('TOTAL-TIME  TAG')
    for tag, time in time_by_tags.items():
        print(f'{time:10}  #{tag}')


@click.command()
@click.argument('csv_file')
def main(csv_file: str):
    entries = load_entries(csv_file)
    report = compute_total_time_by_tags(entries)
    display_report_by_tags(report)


if __name__ == '__main__':
    main()




      
        
