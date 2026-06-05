from playwright.sync_api import sync_playwright 

def scrape_linkedin_jobs(keyword="AI Engineer", location=""):
    jobs = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}"
        if location:
            url += f"&location={location}"
        page.goto(url)
        page.wait_for_timeout(5000)  # Wait for the page to load
        job_cards = page.query_selector_all(".base-card")
        for card in job_cards[:2]:
            title_elem = card.query_selector(".base-search-card__title")
            company_elem = card.query_selector(".base-search-card__subtitle")
            location_elem = card.query_selector(".base-search-card__location")
            link_elem = card.query_selector("a")
            
            if not all([title_elem, company_elem, link_elem]):
                continue
            
            title = title_elem.inner_text().strip()
            company = company_elem.inner_text().strip()
            location = location_elem.inner_text().strip() if location_elem else "N/A"
            link = link_elem.get_attribute("href")
            
            if link:
                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": link
                })
        
        browser.close()
    return jobs

