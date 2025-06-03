
from ..repositories.reddit_submission_repository import RedditSubmissionRepository
from ..repositories.reddit_comment_repository import RedditCommentRepository

import csv
from io import StringIO
from typing import List, Dict, Union

class DataService:
    def __init__(self, submission_repo: RedditSubmissionRepository, comment_repo: RedditCommentRepository):
        self.submission_repo = submission_repo
        self.comment_repo = comment_repo

    def get_submissions_paginated(self, page, page_size):

        result = self.submission_repo.list(page, page_size)
        return {
            "data": result["data"],
            "total": result["total"]
        }

    def get_comments_paginated(self, page, page_size):

        result = self.comment_repo.list(page, page_size)
        return {
            "data": result["data"],
            "total": result["total"]
        }

    def get_submissions(self):
        posts = self.submission_repo.listAll()
        return [post["_source"] for post in posts]

    def get_comments(self):
        comments = self.comment_repo.listAll()
        return [comment["_source"] for comment in comments]

    def get_counts(self):
        return {
            "submissions": self.submission_repo.count(),
            "comments": self.comment_repo.count()
        }

    def export_submissions(self, format: str = 'csv') -> Union[str, List[Dict]]:
        submissions = self.get_submissions()
        return self._convert_format(data=submissions, format=format, filename="submissions")

    def export_comments(self, format: str = 'csv') -> Union[str, List[Dict]]:
        comments = self.get_comments()
        return self._convert_format(data=comments, format=format, filename="comments")

    def _convert_format(self, data: List[Dict], format: str, filename: str) -> Union[str, List[Dict]]:
        if not data:
            raise ValueError("Nenhum dado encontrado para exportação")

        if format == 'csv':
            return self._generate_csv(data, filename)
        elif format == 'json':
            return data
        else:
            raise ValueError(f"Formato não suportado: {format}")

    def _generate_csv(self, data: List[Dict], filename: str) -> str:
        if not data:
            return ""

        # Cria buffer de memória
        output = StringIO()
        writer = csv.writer(output)

        # Escreve cabeçalho
        headers = data[0].keys()
        writer.writerow(headers)

        # Escreve linhas
        for item in data:
            writer.writerow(item.values())

        return output.getvalue()