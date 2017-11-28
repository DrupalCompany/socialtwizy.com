import facebook
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from facebookparser.models import Group
from facebookparser.models import Posts

# # #

# # #
class Command(BaseCommand):

    help = 'Provides an way to extract user groups based upon the token provided'

    #add the arguments
    def add_arguments(self, parser):

        parser.add_argument('--token', nargs='+', type=str)


    # Handels the Comands
    def handle(self, *args, **options):

        token = options['token'][0]

        graph = facebook.GraphAPI(token, version='2.1')

        groups = Group.objects.all()

        for group in groups:

            data = graph.get_connections(group.facebook_id, 'feed', limit=100)

            for post in data['data']:

                # return print(data)

                default_message = ''
                default_story = ''
                default_type = ''

                savePost = Posts()

                savePost.group = group
                savePost.facebook_id = post['id']
                savePost.body = post.get('message', default_message) or post.get('story', default_story) or post('type', default_type)
                savePost.save()

                #return print(savePost)



