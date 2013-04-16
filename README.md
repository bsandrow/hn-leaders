# hn-leaders

A script that pulls down a copy of the Hacker News karmic leaderboard. The
script inlines all external resources using data URIs.

## Purpose

I whipped this together to throw on cron because I noticed that some of the
entries in the middle of the list would disappear and reappear from the list.
The point was to scrape the site for a while and analyze the results.

## Usage

    usage: hn-leaders [-h] [-d DIR] [-v] [-f FORMAT]

    HN leaderboard archiver.

    optional arguments:
      -h, --help            show this help message and exit
      -d DIR, --dir DIR     Directory to store file in
      -v, --verbose         Verbose output
      -f FORMAT, --format FORMAT
                            Format for the filename. This is passed through
                            strftime, so the usual time format characters apply

## License

MIT License. See LICENSE.
