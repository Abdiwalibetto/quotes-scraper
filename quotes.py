import csv

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")

with open("quotes.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Text", "Author", "Tags"])

    while True:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            tags = quote.find_elements(By.CLASS_NAME, "tag")
            writer.writerow([text, author, ",".join(tag.text for tag in tags)])
            print(f"{text} - {author} Tags: {[tag.text for tag in tags]}")

        try:
            driver.find_element(By.CSS_SELECTOR, "li.next a").click()
        except NoSuchElementException:
            break

driver.quit()