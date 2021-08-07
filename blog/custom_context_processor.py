from .models import Category

def subject_renderer(request):
    return {
       'all_topics': Category.objects.all(),
    }