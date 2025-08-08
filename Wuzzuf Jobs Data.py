import requests
from bs4 import BeautifulSoup
import csv

csvfile = open('Wuzzuf Jobs Data.csv','w', newline='', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(['Job Title', 'Company', 'Location', 'Job Type','Work Location','Level','Years of Experience','Time Posted'])

for i in range(594):
    print(f"Scraping page {i}...")
    url = f'https://wuzzuf.net/search/jobs/?start={i}'
    response = requests.get(url).text
    soup = BeautifulSoup(response,'lxml')
    jobs = soup.find_all('div', class_='css-1gatmva e1v1l3u10')

    for job in jobs:
        title_tag = job.find('a', class_='css-o171kl')
        title = title_tag.text.strip() if title_tag else 'NAN'

        company_tag = job.find('a', class_='css-17s97q8')
        company = company_tag.text.strip() if company_tag else 'NAN'

        location_tag = job.find('span', class_='css-5wys0k')
        location = location_tag.text.strip() if location_tag else 'NAN'

        jobtype_tag = job.find('span', class_='css-1ve4b75 eoyjyou0')
        jobtype = jobtype_tag.text.strip() if jobtype_tag else 'NAN'

        worklocation_tag = job.find('span', class_='css-o1vzmt eoyjyou0')
        worklocation = worklocation_tag.text.strip() if worklocation_tag else 'NAN'

        level_tag = job.find('a', class_='css-o171kl')
        level = level_tag.text.strip() if level_tag else 'NAN'

        time_tag = job.find('div', class_='css-4c4ojb')
        time = time_tag.text.strip() if time_tag else 'NAN'

        # Extract years of experience
        spans = job.find_all('span')
        experience = 'NAN'
        for span in spans:
            if 'Yrs of Exp.' in span.text:
                experience = span.text.strip()
                break

        writer.writerow([title, company, location, jobtype, worklocation, level, experience, time])

csvfile.close()
print("✅ Scraping completed and saved to 'Wuzzuf Jobs Data.csv'")
