from django.test import TestCase

# Create your tests here.
from news import models


class NewsTestCase(TestCase):
    def test_news(self):
        for i in range(20):
            o = models.News(
                title="OHHH #{}".format(i + 1),
                description="News!News!News!",
                source='site.co.il',

            )

            o.full_clean()
            o.save()

        self.assertEquals(models.News.objects.count(), 20)
