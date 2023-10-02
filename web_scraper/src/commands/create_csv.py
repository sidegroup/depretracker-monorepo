import pandas as pd
from elasticsearch_dsl import Search
from ..factories.elastic_search_client import ElasticsearchClientFactory


class CreateCsv:

    OUTPUT_PATH = "output/"

    def __init__(self):
        self.es = ElasticsearchClientFactory.create()


    def search(self, index):
        return Search(using=self.es, index=index).query("match_all").scan()

    def for_submissions(self, index):
        result = list()
        for hit in self.search(index):
            result.append({
                'author_name': hit['author_name'],
                'author_flair': hit['author_flair'],
                'date': hit['date'],
                'post_id': hit['post_id'],
                'is_original_content': hit['is_original_content'],
                'is_text': hit['is_text'],
                'link_flair': hit['link_flair'],
                'is_locked': hit['is_locked'],
                'post_name': hit['post_name'],
                'number_of_comments': hit['number_of_comments'],
                'mature_content': hit['mature_content'],
                'permalink': hit['permalink'],
                'score': hit['score'],
                'text': hit['text'],
                'spoiler': hit['spoiler'],
                'fixed': hit['fixed'],
                'title': hit['title'],
                'upvote_ration': hit['upvote_ration'],
                'url': hit['url']
            })
        dataframe = pd.DataFrame.from_dict(result, orient='columns')
        dataframe.to_csv(self.OUTPUT_PATH + "{}.csv".format(index))


    def for_comments(self, index):
        result = list()
        count = 0
        for hit in self.search(index):
            count += 1
            print(count)
            result.append({
                'id': hit['id'],
                'author_name': hit['author_name'],
                'body': hit['body'],
                # 'body_html': hit['body_html'],
                'date': hit['date'],
                'is_author_comment': hit['is_author_comment'],
                'link_id': hit['link_id'],
                'parent_id': hit['parent_id'],
                'permalink': hit['permalink'],
                'score': hit['score'],
                'fixed': hit['fixed'],
                'post_id': hit['post_id'],
            })
        dataframe = pd.DataFrame.from_dict(result, orient='columns')
        dataframe.to_csv(self.OUTPUT_PATH + "{}.csv".format(index))
