import praw
import time

# Autenticação na API do Reddit
reddit = praw.Reddit(client_id='DzLrEIjbuDKTEirqtk3uHw',
                     client_secret='5PK8_DzWN4RtuUlTVTxpONZWCtFXSw',
                     username='taw-balbino',
                     password='!!3uSKPvumU9Kst',
                     user_agent='webcrowler')



try:
    submissions = reddit.subreddit('desabafos').search('deprê OR ansiedade OR chorar OR morrer OR matar OR medo OR crises OR chorando OR Só OR sozinho OR solidão OR desolado OR morto OR vazio OR suicídio OR surto OR surtei OR surtar OR depressivo ORansioso OR ansiosa OR desespero OR desesperado OR desesperada OR solitário OR melancólico OR desânimo OR tristeza OR depresso OR infeliz OR neura OR neurótico OR psiquiatra OR psicólogo OR psicóloga OR noia OR noiada OR noiado OR ajuda OR problema OR problemas', limit=None, sort= "hot")
    contador = 0
    for submission in submissions:
        for comment in submission.comments:
            print(comment.body)

        print(submission.selftext)
        print(submission.author.name)
        contador += 1
        print(contador)

except Exception:
    print(Exception.__str__)


