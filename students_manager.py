"""
students_manager.py

A small utility to help Roy (class monitor) manage per-student records.
Features:
- Add or overwrite a brief introduction for a student (name, class, fav_subject, short intro)
- Write per-student text files in a `students_records/` directory
- Maintain a `students.json` index file
- Read/list existing records

Usage examples included in the `__main__` block.
"""

import os
import json
from dataclasses import dataclass
from typing import Optional

STUDENTS_DIR = os.path.join(os.path.dirname(__file__), "students_records")
JSON_INDEX = os.path.join(STUDENTS_DIR, "students.json")

@dataclass
class Student:
    name: str
    student_class: int = 8
    favourite_subject: Optional[str] = None
    intro: Optional[str] = None


def ensure_dir():
    os.makedirs(STUDENTS_DIR, exist_ok=True)


def sanitize_filename(name: str) -> str:
    # Replace spaces with underscores and remove unsafe chars
    safe = "".join(c for c in name if c.isalnum() or c in " _-").rstrip()
    return safe.replace(" ", "_")


def student_file_path(name: str) -> str:
    fname = sanitize_filename(name) + ".txt"
    return os.path.join(STUDENTS_DIR, fname)


def save_student_file(student: Student, overwrite: bool = True) -> str:
    """Write a per-student text file. Returns path."""
    ensure_dir()
    path = student_file_path(student.name)
    if os.path.exists(path) and not overwrite:
        raise FileExistsError(f"File {path} exists and overwrite is False")

    content_lines = [
        f"Name: {student.name}",
        f"Class: {student.student_class}",
        f"Favourite subject: {student.favourite_subject or 'N/A'}",
        "",
        "Brief intro:",
        student.intro or "",
    ]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(content_lines))

    # update index json
    update_index(student)
    return path


def read_student_file(name: str) -> str:
    path = student_file_path(name)
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def update_index(student: Student):
    ensure_dir()
    index = {}
    if os.path.exists(JSON_INDEX):
        with open(JSON_INDEX, "r", encoding="utf-8") as fh:
            try:
                index = json.load(fh)
            except json.JSONDecodeError:
                index = {}
    index[student.name] = {
        "class": student.student_class,
        "favourite_subject": student.favourite_subject,
        "intro_preview": (student.intro or "").strip()[:120],
    }
    with open(JSON_INDEX, "w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=2, ensure_ascii=False)


def list_students() -> dict:
    ensure_dir()
    if not os.path.exists(JSON_INDEX):
        return {}
    with open(JSON_INDEX, "r", encoding="utf-8") as fh:
        return json.load(fh)


def rebuild_index_from_files() -> int:
    """Rebuilds `students.json` from existing per-student .txt files.
    Scans `students_records/` for `.txt` files, parses basic fields and writes a fresh index.
    Returns the number of records written to the index."""
    ensure_dir()
    entries = {}
    count = 0
    for fname in os.listdir(STUDENTS_DIR):
        if not fname.lower().endswith('.txt'):
            continue
        path = os.path.join(STUDENTS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except OSError:
            continue
        lines = content.splitlines()
        name = None
        class_num = 8
        fav = None
        intro_lines = []
        in_intro = False
        for line in lines:
            if line.startswith('Name:'):
                name = line.split(':', 1)[1].strip()
            elif line.startswith('Class:'):
                try:
                    class_num = int(line.split(':', 1)[1].strip())
                except Exception:
                    class_num = 8
            elif line.startswith('Favourite subject:') or line.startswith('Favorite subject:'):
                fav = line.split(':', 1)[1].strip()
            elif line.strip() == 'Brief intro:':
                in_intro = True
            elif in_intro:
                intro_lines.append(line)
        if name:
            intro = '\n'.join(intro_lines).strip()
            entries[name] = {
                'class': class_num,
                'favourite_subject': fav or None,
                'intro_preview': (intro or '')[:120]
            }
            count += 1
    with open(JSON_INDEX, 'w', encoding='utf-8') as fh:
        json.dump(entries, fh, indent=2, ensure_ascii=False)
    return count


def import_from_csv(csv_path: str, overwrite: bool = True, encoding: str = 'utf-8') -> int:
    """Import students from a CSV file with headers: name,class,favourite_subject,intro
    Returns the number of records imported."""
    import csv
    count = 0
    with open(csv_path, newline='', encoding=encoding) as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            # Accept multiple header name variants for robustness
            name = (row.get('name') or row.get('Name') or '').strip()
            if not name:
                continue
            class_val = (row.get('class') or row.get('student_class') or row.get('Class') or '').strip()
            try:
                sc = int(class_val) if class_val != '' else 8
            except ValueError:
                sc = 8
            fav = (row.get('favourite_subject') or row.get('favourite') or row.get('Favourite subject') or '').strip() or None
            intro = (row.get('intro') or row.get('introduction') or '').strip() or None
            s = Student(name=name, student_class=sc, favourite_subject=fav, intro=intro)
            save_student_file(s, overwrite=overwrite)
            count += 1
    return count


if __name__ == "__main__":
    # CLI for simple operations: list, import CSV, or create sample data
    import argparse
    import csv

    parser = argparse.ArgumentParser(description='Manage student records (add/list/import)')
    parser.add_argument('--import-csv', dest='import_csv', help='Path to CSV file to import')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing per-student files when importing')
    parser.add_argument('--list', action='store_true', help='Print the students index (students.json)')
    parser.add_argument('--create-sample-csv', action='store_true', help='Write a sample CSV file (students_import_sample.csv)')
    parser.add_argument('--rebuild-index', action='store_true', help='Rebuild students.json from per-student .txt files')
    args = parser.parse_args()

    if args.create_sample_csv:
        sample_csv = os.path.join(os.path.dirname(__file__), 'students_import_sample.csv')
        with open(sample_csv, 'w', encoding='utf-8', newline='') as fh:
            w = csv.writer(fh)
            w.writerow(['name', 'class', 'favourite_subject', 'intro'])
            w.writerow(['Sam', '8', 'Art', 'Enjoys drawing and painting.'])
            w.writerow(['Mina', '8', 'Mathematics', 'Adept at mental arithmetic.'])
        print('Wrote sample CSV:', sample_csv)
        raise SystemExit(0)

    if args.import_csv:
        if not os.path.exists(args.import_csv):
            print('CSV file not found:', args.import_csv)
            raise SystemExit(1)
        added = import_from_csv(args.import_csv, overwrite=args.overwrite)
        print(f'Imported {added} students from', args.import_csv)
        print('\nUpdated students index:')
        print(json.dumps(list_students(), indent=2, ensure_ascii=False))
        raise SystemExit(0)

    if args.rebuild_index:
        written = rebuild_index_from_files()
        print(f'Rebuilt index from .txt files. {written} records written to', JSON_INDEX)
        print('\nUpdated students index:')
        print(json.dumps(list_students(), indent=2, ensure_ascii=False))
        raise SystemExit(0)

    if args.list:
        print(json.dumps(list_students(), indent=2, ensure_ascii=False))
        raise SystemExit(0)

    # Default behavior: create a few sample students if run without arguments
    sample_students = [
        Student(name="Roy", student_class=8, favourite_subject="Mathematics", intro="Class monitor. Likes helping classmates and organizing notes."),
        Student(name="Aisha", student_class=8, favourite_subject="Science", intro="Enthusiastic about experiments."),
        Student(name="Daniel", student_class=8, favourite_subject="History", intro="Loves reading historical stories."),
        Student(name="Priya", student_class=8, favourite_subject="English", intro="Enjoys writing short poems.")
    ]

    print("Creating sample student records in:", STUDENTS_DIR)
    for s in sample_students:
        path = save_student_file(s, overwrite=True)
        print("- ", s.name, "->", path)

    print("\nCurrent students index:")
    print(json.dumps(list_students(), indent=2, ensure_ascii=False))
