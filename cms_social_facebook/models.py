from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

COLOR_CHOICES = [
    ('light', _('light')),
    ('dark', _('dark')),
]

class FacebookComments(CMSPlugin):
    pageurl = models.URLField(_("URL to comment on"))
    num_posts = models.PositiveSmallIntegerField(_("Number of posts"),
        default=2)
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)

    def __unicode__(self):
        return "Comments (%s)" % (self.pageurl)

class FacebookFacepile(CMSPlugin):
    pageurl = models.URLField(_("URL"))
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)

    max_rows = models.PositiveSmallIntegerField(_("Max rows"),
        default=1)

    action = models.CharField(_("Actions separate by commas"),
        default=None, null=True, blank=True)

    def __unicode__(self):
        return "Facepile (%s)" % (self.pageurl)

class FacebookLikebox(CMSPlugin):
    pageurl = models.URLField(_("URL that you like it"))
    num_posts = models.PositiveSmallIntegerField(_("Number of posts"),
        default=2)
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    height = models.PositiveSmallIntegerField(_("Height"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))

    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)

    border_color = models.CharField(_("Color Scheme"), default=None,
            null=True, blank=True, max_length=50)

    show_faces = models.BooleanField(_("Show faces"),
            default=True)

    stream = models.BooleanField(_("Stream"),
            default=True)

    header = models.BooleanField(_("Header"),
            default=True)



    def __unicode__(self):
        return "Comments (%s)" % (self.pageurl)


