import time
from typing import Dict, Iterable, List
import requests


class Mail:
    BASE_URL = "https://tempmail.plus/api/mails"
    ALLOWED_DOMAINS = {
        "mailto.plus",
        "fexpost.com",
        "fexbox.org",
        "mailbox.in.ua",
        "rover.info",
        "chitthi.in",
        "fextemp.com",
        "any.pink",
        "merepost.com",
    }

    def __init__(self, Email: str, Loop: bool = False, interval_seconds: int = 5) -> None:
        self.loop = Loop
        self.interval_seconds = interval_seconds

        if "@" not in Email:
            raise ValueError(self._invalid_domain_message(""))

        _local, domain = Email.split("@", 1)
        if domain not in self.ALLOWED_DOMAINS:
            raise ValueError(self._invalid_domain_message(domain))

        self.email = Email
        self.session = requests.Session()
        self.session.headers.update({
            "accept": "application/json",
            "user-agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/141.0.0.0 Safari/537.36"
            ),
        })
        self.cookies = {"email": self._encode_email_cookie(self.email)}
        self._seen_ids = set()

    @staticmethod
    def _encode_email_cookie(email: str) -> str:
        return email.replace("@", "%40")

    def _fetch_mails(self, limit: int = 10) -> Dict:
        params = {"email": self.email, "limit": str(limit)}
        response = self.session.get(self.BASE_URL, params=params, cookies=self.cookies, timeout=20)
        response.raise_for_status()
        return response.json()

    def _list_mail_items(self, limit: int = 10) -> List[Dict]:
        payload = self._fetch_mails(limit=limit)
        mail_list = payload.get("mail_list") or []
        return mail_list if isinstance(mail_list, list) else []

    def get_inboxes(self, limit: int = 10) -> Iterable[Dict]:
        if not self.loop:
            items = self._list_mail_items(limit=limit)
            return [self._format_mail_item(item) for item in items]

        items = self._list_mail_items(limit=limit)
        for item in items:
            mail_id = item.get("mail_id")
            if isinstance(mail_id, int):
                self._seen_ids.add(mail_id)
            print(self._format_mail_item(item))

        while True:
            try:
                items = self._list_mail_items(limit=limit)
            except requests.RequestException:
                time.sleep(self.interval_seconds)
                continue

            for item in items:
                mail_id = item.get("mail_id")
                if isinstance(mail_id, int) and mail_id not in self._seen_ids:
                    self._seen_ids.add(mail_id)
                    print(self._format_mail_item(item))

            time.sleep(self.interval_seconds)

    @staticmethod
    def _format_mail_item(item: Dict) -> Dict:
        return {
            "from_mail": item.get("from_mail"),
            "from_name": item.get("from_name"),
            "subject": item.get("subject"),
            "is_new": item.get("is_new"),
            "time": item.get("time"),
            "mail_id": item.get("mail_id"),
        }

    def _invalid_domain_message(self, provided: str) -> str:
        suggestions = ", ".join(sorted(self.ALLOWED_DOMAINS))
        prefix = f"Provided domain '{provided}' does not exist. " if provided else "Invalid email format. "
        return f"{prefix}Valid domains are: {suggestions}"



