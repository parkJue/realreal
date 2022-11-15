from typing import List
from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand
 
 
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("receiver", nargs="+", type=str, help="이메일 수신 주소")
 
    def handle(self, *args, **options):
        subject = "장고를 활용한 이메일 발송"
        content = "메시지 내용입니다."
        sender_email = settings.DEFAULT_FROM_EMAIL
        receiver_email_list: List[str] = options["receiver"]
        send_mail(subject, content, sender_email, receiver_email_list)