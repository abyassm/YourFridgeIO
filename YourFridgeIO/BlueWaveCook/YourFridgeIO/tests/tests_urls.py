from django.urls import reverse, resolve

class TestUrls:

    @classmethod
    def test_detail_url(self):

        path = reverse('login')
        print("test")
        assert resolve(path).view_name == 'login'
        
