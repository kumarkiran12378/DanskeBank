
from django.db.models.signals import pre_delete
from book.models import Book, Author
from django.dispatch import receiver


@receiver(pre_delete, sender=Book)
def delete_author(sender, instance, **kwargs):
    author_ids = list(instance.authors.values_list('author_id', flat=True))
    for id in author_ids:
        if sender.objects.filter(authors=id).count()<2:
            Author.objects.filter(author_id=id).delete()

@receiver(pre_delete, sender=Author)
def delete_author(sender, instance, **kwargs):
    if Book.objects.filter(authors=instance.author_id).count()>0:
        raise Exception("Author is associated with one or more Book.")
