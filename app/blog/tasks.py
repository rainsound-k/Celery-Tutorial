from celery import shared_task

from .models import Post
from config.celery import app


@app.task(bind=True)
def blog_debug_task(self):
    return 'blog'


@shared_task
def blog_shared_task():
    return 'shared'


@shared_task
def blog_post_task():
    for i in range(100000):
        Post.objects.create(
            title=f'{i} 번째 글입니다.',
            content=f'{i} 글의 내용입니다!!!!!!!!!!'
        )
    return
