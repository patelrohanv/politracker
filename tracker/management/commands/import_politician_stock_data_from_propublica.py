import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from tracker.models import Politician, Stock, Trade


class Command(BaseCommand):
    help = "Imports data from the US Senate's Financial Disclosures website"

    def fetch_data(self):
        url = "https://efdsearch.senate.gov/search/report/data/"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
        }

        payload = {
            "report_types": '["PTR"]',
            "senator_state": "",
            "senator_party": "",
            "senator": "",
            "report_date_from": "01/01/2020",
            "report_date_to": "12/31/2020",
            "ptr_date_from": "",
            "ptr_date_to": "",
            "submit": "Search",
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            print("Fetched data successfully")
            return response.content
        else:
            print(
                f"Failed to fetch data from the website. Status code: {response.status_code}"
            )
            return None

    def parse_data(self, content):
        soup = BeautifulSoup(content, "html.parser")
        data_rows = soup.select("table#search-results tbody tr")
        return data_rows

    def process_data(self, data_rows):
        for row in data_rows:
            cells = row.find_all("td")

            politician, _ = Politician.objects.get_or_create(
                name=cells[0].text.strip(),
            )

            stock, _ = Stock.objects.get_or_create(
                symbol=cells[3].text.strip(),
                name=cells[2].text.strip(),
            )

            trade = Trade(
                politician=politician,
                stock=stock,
                trade_type=cells[4].text.strip(),
                trade_date=cells[1].text.strip(),
                amount=cells[5].text.strip(),
            )
            trade.save()

    def handle(self, *args, **options):
        content = self.fetch_data()

        if content:
            data_rows = self.parse_data(content)
            print(f"Number of rows parsed: {len(data_rows)}")
            self.process_data(data_rows)
            self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
        else:
            self.stdout.write(self.style.ERROR("Failed to fetch data from the website"))
