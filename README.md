# youtube-transcript-scraper

**Fork**

Fork replacing the `txt` output by a `json` file for each video.

```json
[
    {
        "offset": "00:06", 
        "text": "HE'S ALRIGHT. HE'S FINE. JUST GET HIM DRESSED."
    }, 
    {
        "offset": "00:09", 
        "text": "I THINK HE LOOKS GREAT."
    },
    ...
]
```

Steps:
- adding the id of the video in `videoIds.csv`
- running `python captions.py`

**Origin**

## description
Since YouTube does not provide automatically generated transcripts via its API and normal scraping does not work with YT's ajaxy interface, this script uses browser automation to click through the YouTube web interface and download the transcript file.

## requirements
* a functioning webdriver environment (tested with [https://github.com/mozilla/geckodriver/releases][1]);
* the selenium package for Python;
* a CSV file with a column for video ids as input;

## use
* download script;
* create a directory called "subtitles" and make sure the script can write to it;
* modify captions.py with your CSV filename;
* make sure that webdriver and selenium are installed;
* run the script;

[1]:	https://github.com/mozilla/geckodriver/releases