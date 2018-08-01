#!/usr/bin/env python
import argparse
import os
import sys

DEFAULT_DOCS = 50000
DEFAULT_QUERIES = 10000
DEFAULT_CORPUS = 10000

def make_output_pair(prefix, docs_name="_docs.txt", queries_name="_queries.txt"):
    f1 = open(prefix + docs_name, "w");
    f2 = open(prefix + queries_name, "w");

    return f1, f2

def make_data(prefix, docs, queries, ndocs = DEFAULT_DOCS, nqueries = DEFAULT_QUERIES):
    d_stream, q_stream = make_output_pair(prefix)

    while (ndocs):
        d_stream.write(docs[ndocs % len(docs)] + '\n')
        ndocs-=1;

    while (nqueries):
        q_stream.write(queries[nqueries % len(queries)] + '\n')
        nqueries-=1

def make_capitals(args):
    docs = [
      "london is the capital of great britain",
      "paris is the capital of france",
      "berlin is the capital of germany",
      "rome is the capital of italy",
      "madrid is the capital of spain",
      "lisboa is the capital of portugal",
      "bern is the capital of switzerland",
      "moscow is the capital of russia",
      "kiev is the capital of ukraine",
      "minsk is the capital of belarus",
      "astana is the capital of kazakhstan",
      "beijing is the capital of china",
      "tokyo is the capital of japan",
      "bangkok is the capital of thailand",
      "welcome to moscow the capital of russia the third rome",
      "amsterdam is the capital of netherlands",
      "helsinki is the capital of finland",
      "oslo is the capital of norway",
      "stockgolm is the capital of sweden",
      "riga is the capital of latvia",
      "tallin is the capital of estonia",
      "warsaw is the capital of poland",
    ];
    queries = [
        "moscow is the capital of russia",
        "lisboa or helsinki is capital of latvia",
        "another query about riga",
        "what is the capital of london"
    ];

    prefix = args.prefix or "capital"
    make_data(prefix, docs, queries, args.docs, args.queries)

def make_heavy(args):
    from random import choice, randint
    from string import ascii_lowercase as low

    # worst case
    word_len = 100
    words_in_doc = 1000

    prefix = args.prefix or "heavy"
    words = []

    print "Generating heavy set, it takes some time."
    print "Generating words.."
    for i in range(args.corpus):
        words.append(''.join(choice(low) for x in range(word_len)))

    d_stream, q_stream = make_output_pair(prefix)
    print "Generating docs.."
    for i in range(args.docs):
        d_stream.write(' '.join(choice(words) for x in range(words_in_doc)) + '\n')
    print "Generating queries.."
    for i in range(args.queries):
        query_size = randint(1,10)
        q_stream.write(' '.join(choice(words) for x in range(query_size)) + '\n')
    print "Done"

def make_same(args):
    docs = [
        "london is the capital of great britain",
    ]

    queries = [
        "london is the capital of great britain",
    ]

    prefix = args.prefix or "same"
    make_data(prefix, docs, queries, args.docs, args.queries)

def make_only(args):
    docs = [
        "one one one one one one one one one one one"
    ]

    queries = [
        "one one one"
    ]

    prefix = args.prefix or "only"
    make_data(prefix, docs, queries, args.docs, args.queries)


def main(args):
    call_me = globals().get("make_" + args.command)
    call_me(args)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('command', choices=('capitals', 'heavy', 'same', 'only'))
    argparser.add_argument('-d', '--docs', default=DEFAULT_DOCS, type=int, help="Number of docs")
    argparser.add_argument('-q', '--queries', default=DEFAULT_QUERIES, type=int, help="Number of queries")
    argparser.add_argument('-c', '--corpus', default=DEFAULT_CORPUS, type=int, help="Alphabet size")
    argparser.add_argument('-p', '--prefix', default="", type=str, help="Prefix to name otuput files")
    argparser.add_argument('files', nargs="*")
    args = argparser.parse_args()

    main(args)
