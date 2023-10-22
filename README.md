# Simple program that will check for any updates on a news article every 2 minutes
![image](https://github.com/ZeraAI/news-alert-checker/assets/43397999/5c292057-59a2-4f5c-b344-37b2c33f7023)


If there is update: Makes a *ding* sound.

If there is no update: Just keeps running quietly.


## How to run
### 1. Install requirements
```bash
pip install requests beautifulsoup4 pygame
```

### 2. Prepare Sound File
You can use the provided mp3 file to use as your alert. You can use any other sound without restriction.

### 3. Modify the news websites that you want updated

### 4. Run
```bash
python3 news_monitor.py
```

## How is this useful?
If you want to keep up with certain news or are particularly interested in a specific article, then this script will get the job done.

Especially during these trying times with uncertainty and war (ex: Ukraine vs Russia, Hamas Israel and Palestine). 

Suggestion: You could run this on a Raspberry Pi with a little speaker to stay up to date.
