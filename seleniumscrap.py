from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_courses_page(url):
    # Setup Chrome with headless options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        wait = WebDriverWait(driver, 10)  # wait max 10 seconds

        # Wait until at least one course item appears
        course_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".course-item")))

        data = []
        for item in course_items:
            title = item.find_element(By.CSS_SELECTOR, ".course-title").text
            description = item.find_element(By.CSS_SELECTOR, ".course-description").text
            data.append({
                "title": title,
                "description": description
            })

        return data

    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://courses.ethernet.edu.et/portal/courses"
    scraped_data = scrape_courses_page(url)
    for course in scraped_data:
        print(f"Title: {course['title']}")
        print(f"Description: {course['description']}\n")
