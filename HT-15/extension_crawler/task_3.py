import subprocess

if __name__ == "__main__":
    subprocess.run(["scrapy", "crawl", "google", "-O", "data.csv"])