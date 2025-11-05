import requests
from urllib.parse import quote


class SendMail:
    """
    Simple mail sender against tempmail.plus API.

    Usage:
        from ByMail.send import SendMail
        mail = SendMail(
            from_="utpys@merepost.com",
            to="utpys@fexpost.com",
            subject="WEwetse",
            text="zsgzsdgzse",
            content_type="text/html",  # default
        )
        sent = mail.status()
    """

    def __init__(
        self,
        *,
        from_: str,
        to: str,
        subject: str,
        text: str,
        content_type: str = "text/html",
        api_url: str = "https://tempmail.plus/api/mails/",
        headers_override: dict | None = None,
    ) -> None:
        self.from_ = from_
        self.to = to
        self.subject = subject
        self.text = text
        self.content_type = content_type or "text/html"
        self.api_url = api_url
        self._response = None

        cookies = {"email": quote(self.from_)}


        headers = {
            "accept": "*/*",
            "origin": "https://tempmail.plus",
            "referer": "https://tempmail.plus/en/",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "ByMail/1.0 (+requests)",
        }
        if headers_override:
            headers.update(headers_override)

        files = {
            "email": (None, self.from_),
            "to": (None, self.to),
            "subject": (None, self.subject),
            "content_type": (None, self.content_type),
            "text": (None, self.text if self.content_type != "text/html" else f"{self.text}"),
        }

        try:
            self._response = requests.post(
                self.api_url,
                cookies=cookies,
                headers=headers,
                files=files,
                timeout=20,
            )
        except Exception as exc:
            class _ErrorResponse:
                def __init__(self, error: Exception) -> None:
                    self.status_code = 0
                    self.ok = False
                    self.text = str(error)

            self._response = _ErrorResponse(exc)

    def status(self) -> bool:
        """Return True if the message appears to be sent successfully."""
        if self._response is None:
            return False
        try:
            return 200 <= int(getattr(self._response, "status_code", 0)) < 300
        except Exception:
            return False

    def response(self):
        """Return the underlying response object (or error-like object)."""
        return self._response


