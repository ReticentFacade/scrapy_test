# Testing Srapy Framework

## Setup

1. Clone & cd into the dir

```sh
git clone git@github.com/ReticentFacade/scrapy_test.git
cd scrapy_test/linkedin_ppl_spider
```

2. Create venv

```sh
python3 -m venv venv
```

3. Start venv

```sh
source venv/bin/activate
```

4. Install packages

```sh
pip install Scrapy scrapingbee
```

5. Check whether scrapy is working [It should list `linkedin_ppl_spider` in the output]

```sh
scrapy list
```

6. Run

```sh
scrapy crawl linkedin_ppl_spider
```
