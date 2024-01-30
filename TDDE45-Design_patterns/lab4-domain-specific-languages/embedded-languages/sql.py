#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('bible-sqlite.db')
# The table is t_bbe and it has columns b,c,v,t
# Make the requested queries to the database

cur = conn.cursor()

def books_verses(cur):
    books_verses = {}
    for row in cur.execute('SELECT b,v FROM t_bbe'):
        if row[0] in books_verses.keys():
            books_verses[row[0]] += 1
        else:
            books_verses[row[0]] = 1
    return books_verses

print(books_verses(cur))

def book_memories(cur):
    book_memory = []
    for row in cur.execute('SELECT b,v,t FROM t_bbe'):
        if 'memory' in row[2]:
            if not row[0] in book_memory:
                book_memory.append(row[0])
    return book_memory

print(book_memories(cur))

def avg_verses(cur):
    avg = {} # chapter:[verses]
    for row in cur.execute('SELECT c, avg(v) FROM t_bbe GROUP BY c') :
        if row[0] in avg.keys():
            avg[row[0]] += int(row[1])
        else:
            avg[row[0]] = int(row[1])
    return avg

print(avg_verses(cur))

