from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from markdown import markdown
from taggit.managers import TaggableManager

from helpers import pl_to_en

class Entry(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    markdown_content = models.TextField()
    language = models.CharField(max_length=2)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=512)
    tags = TaggableManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Entries'

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={
            'day': self.pub_date.strftime('%e'), 
            'month': self.pub_date.strftime('%m'), 
            'year': self.pub_date.strftime('%Y'), 
            'slug': self.slug})
    
    def save(self):
        self.content = markdown(self.markdown_content, ['codehilite'])
        print(self.content)
        if self.language == 'pl':
            self.slug = slugify(self.title.translate(pl_to_en))
        else:
            self.slug = slugify(self.title)
        super(Entry, self).save()

    def __unicode__(self):
        return unicode(self.title)
