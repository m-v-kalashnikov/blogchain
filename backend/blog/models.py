import datetime
import itertools
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from auth_custom.models import User


def user_directory_path(filename):
    return 'posts/{filename}/'.format(filename=filename)


class Post(models.Model):
    author = models.ForeignKey(User,
                               verbose_name='Автор',
                               related_name='blog_post_author',
                               on_delete=models.CASCADE,
                               )
    title = models.CharField(verbose_name='Название',
                             max_length=256,
                             null=True
                             )
    picture = models.ImageField(verbose_name='Изображение',
                                upload_to='posts/',
                                null=True,
                                blank=True
                                )
    text = models.TextField(verbose_name='Текст',
                            null=True
                            )
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True,
                                      null=True
                                      )
    slug = models.SlugField(verbose_name='Слаг',
                            default='',
                            editable=False,
                            max_length=512,
                            )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def _generate_slug(self):
        slug_candidate = slug_original = slugify(self.title, allow_unicode=True)
        for i in itertools.count(1):
            if not Post.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

    def comments(self):
        return Comment.objects.filter(post=self)

    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Было ли создано недавно?'


class Comment(models.Model):
    author = models.ForeignKey(User,
                               verbose_name='Автор',
                               related_name='blog_comment_author',
                               on_delete=models.CASCADE,
                               )
    post = models.ForeignKey(Post,
                             verbose_name='Пост',
                             related_name='blog_comment_post',
                             on_delete=models.CASCADE,
                             )
    text = models.TextField(verbose_name='Текст',
                            null=True
                            )
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True,
                                      null=True
                                      )

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-created_at']

    def __str__(self):
        return 'Коментарий "{}" от {}'.format(self.text[:20], self.author)

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

    def positive(self):
        return RateOfComment.objects.filter(comment=self, opinion='P').count()

    def negative(self):
        return RateOfComment.objects.filter(comment=self, opinion='N').count()

    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Было ли создано недавно?'


class RateOfComment(models.Model):
    author = models.ForeignKey(User,
                               verbose_name='Автор',
                               related_name='blog_rate_of_comment_author',
                               on_delete=models.CASCADE,
                               )
    comment = models.ForeignKey(Comment,
                                verbose_name='Коментарий',
                                related_name='blog_rate_of_comment_comment',
                                on_delete=models.CASCADE,
                                )
    POSITIVE = 'P'
    NEGATIVE = 'N'
    OPINION = [
        (POSITIVE, 'Позитивное'),
        (NEGATIVE, 'Негативное'),
    ]
    opinion = models.CharField(verbose_name='Мнение',
                               max_length=2,
                               choices=OPINION,
                               )
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True,
                                      null=True
                                      )

    class Meta:
        verbose_name = 'Мнение о коментарии'
        verbose_name_plural = 'Мнение о коментариях'
        ordering = ['-created_at']

    def __str__(self):
        return 'Мнение о коментании "{}" от {}'.format(self.comment.text[:20], self.author.username)
