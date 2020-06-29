"""Post views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


posts = [
    {
        'name': 'Mont Blac',
        'user': 'Kariscita Paiva',
        'timestamp': datetime.now().strftime('%b %dth, %Y-%H:%M hrs '),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Vía Láctea',
        'user': 'Dernier Servo',
        'timestamp': datetime.now().strftime('%b %dth, %Y-%H:%M hrs '),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Mont Blac',
        'user': 'Peguita Arrasco Paiva',
        'timestamp': datetime.now().strftime('%b %dth, %Y-%H:%M hrs '),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

def list_posts(request):
    """List existing posts."""
    content = []
    for post in posts:
        content.append(
            """
                <p><strong>{name}</strong></p>
                <p><small>{user}<p><i>{timestamp}</i></p></small></p>
                <figure><img src="{picture}"/></figure>
            """.format(**post)
        )
    return HttpResponse('<br>'.join(content))