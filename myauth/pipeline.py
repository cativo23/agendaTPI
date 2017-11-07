from urllib.request import urlopen
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile


def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large"%response['id']

    if url and user.avatar == None:
        avatar = urlopen(url)
        user.avatar.save(slugify(user.username + " social") + '.jpg', ContentFile(avatar.read()))
        user.save()
