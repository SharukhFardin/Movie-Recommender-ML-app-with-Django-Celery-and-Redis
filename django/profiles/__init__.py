from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from recommender import utils

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?", default=10, type=int)

    def handle(self, *args: Any, **options: Any) -> str | None:
        count = options.get("count")
