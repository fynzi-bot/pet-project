from django.test import TestCase, Client
from site_app.models import News, Goods
from datetime import datetime, timezone


# Create your tests here.

class NewsPage(TestCase):

    def setUp(self):
        self.client = Client()
        news = News.objects.create(title='Мерседес амг', short_description='Крутой мужик',
                                   description='еще круче мужик',
                                   created_date=datetime.strptime('25.05.2025', '%d.%m.%Y'), category='N')
        news.save()
        news = News.objects.create(title='Мерседес амг', short_description='Крутой мужик',
                                   description='еще круче мужик',
                                   created_date=datetime.strptime('25.05.2025', '%d.%m.%Y'), category='U')
        news.save()
        self.response = self.client.get('/news/')

    def test_news_success(self):
        self.assertEqual(self.response.status_code, 200)

    def test_news_updates_post(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('news', self.response.context)
        self.assertIn('updates', self.response.context)


class NewsSinglePage(TestCase):

    def setUp(self):
        self.client = Client()
        news = News.objects.create(title='Мерседес амг',
                                   short_description='Крутой мужик',
                                   description='еще круче мужик',
                                   created_date=datetime(2025, 5, 25, 0, 0, tzinfo=timezone.utc),
                                   category='N')
        news.save()
        self.response = self.client.get('/news/1')

    def test_news_success(self):
        self.assertEqual(self.response.status_code, 200)

    def test_news_check_fields(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual('Мерседес амг', self.response.context['news'].title)
        self.assertEqual('Крутой мужик', self.response.context['news'].short_description)
        self.assertEqual('еще круче мужик', self.response.context['news'].description)
        self.assertEqual(datetime(2025, 5, 25, 0, 0, tzinfo=timezone.utc), self.response.context['news'].created_date)
        self.assertEqual('N', self.response.context['news'].category)


class Shop(TestCase):
    def setUp(self):
        self.client = Client()
        good = Goods.objects.create(img='test', name='test', price=1, description='test test')
        good.save()
        self.response = self.client.get('/shop/')

    def test_shop_response_success(self):
        self.assertEqual(self.response.status_code, 200)

    def test_invalid_goods_list(self):
        self.assertIn('goods_list', self.response.context)


class ShopSingle(TestCase):
    def setUp(self):
        self.client = Client()
        good = Goods.objects.create(img='test', name='test', price=1, description='test test')
        good.save()
        self.response = self.client.get('/shop-single/1')

    def test_shop_single_response_success(self):
        self.assertEqual(self.response.status_code, 200)

    def test_invalid_good(self):
        self.assertIn('good', self.response.context)
        self.assertEqual('test', self.response.context['good'].img)
        self.assertEqual('test', self.response.context['good'].name)
        self.assertEqual(1, self.response.context['good'].price)
        self.assertEqual('test test', self.response.context['good'].description)
