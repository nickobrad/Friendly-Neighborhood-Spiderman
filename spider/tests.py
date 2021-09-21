from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Business, Neighbourhood, Post

# Create your tests here.
class ReviewAppTestClass(TestCase):

    def setUp(self):
        self.new_user = User(id = 1, first_name = 'James', last_name = 'Bond', username = 'jamie', email = 'jamesbond@gmail.com')
        # self.new_user.save()

        self.new_hood = Neighbourhood(id = 1, name = 'TestArea', location = 'Location', occupants = 20)
        # self.new_hood.save()

        self.new_business = Business(id = 1, name = 'Test', business_logo = 'photo.jpg', business_details = 'Test project', owner = self.new_user, neighborhood = self.new_hood, contact = 'bizz@gmail.com')
        # self.new_business.save()

        self.new_profile = Profile(id =1, user = self.new_user, family_name = 'Test Name', family_members = 5, family_contact = '0711111111', profile_photo = 'save.jpg', neighborhood = self.new_hood)
        # self.new_profile.save()

        self.new_post = Post(id = 1, title = 'Title', details = 'Bang Bang', hood = self.new_hood, posted_by = self.new_profile)
        # self.new_review.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Post.objects.all().delete()
        Business.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_instance_user(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_instance_post(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_instance_business(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_instance_profile(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
    
    def test_instance_hood(self):
        self.assertTrue(isinstance(self.new_hood, Neighbourhood))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
    
    def test_save_business(self):
        self.new_business.save_business()
        bizz = Business.objects.all()
        self.assertTrue(len(bizz) > 0)

    def test_save_hood(self):
        self.new_hood.save_neighborhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_save_post(self):
        self.new_post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_delete_profile(self):
        profile = self.new_profile
        profile.save_profile()
        profile.delete_profile()        
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_delete_hood(self):
        hood = self.new_hood
        hood.save()
        hood.delete_neighborhood()
        self.assertTrue(len(Neighbourhood.objects.all()) == 0)

    def test_delete_business(self):
        bizz = self.new_business
        bizz.save_business()
        bizz.delete_business()        
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_delete_post(self):
        post = self.new_post
        post.save_post()
        post.delete_post()        
        self.assertTrue(len(Post.objects.all()) == 0)

    def test_update_profile(self):
        self.new_profile.save()
        profile_id = Profile.objects.last().id
        Profile.update_profile(profile_id, 'Testing2')
        new = Profile.objects.get(id = profile_id)
        self.assertEqual(new.family_name, 'Testing2')

    def test_update_neighborhood(self):
        self.new_hood.save()
        hood_id = Neighbourhood.objects.last().id
        Neighbourhood.update_neighborhood_name(hood_id, 'Testing2')
        new = Neighbourhood.objects.get(id = hood_id)
        self.assertEqual(new.name, 'Testing2')

    def test_update_occupants(self):
        self.new_hood.save()
        hood_id = Neighbourhood.objects.last().id
        Neighbourhood.update_neighborhood_occupants(hood_id, 10)
        new = Neighbourhood.objects.get(id = hood_id)
        self.assertEqual(new.occupants, 10)
    
    def test_update_business(self):
        self.new_business.save()
        bizz_id = Business.objects.last().id
        Business.update_business_name(bizz_id, 'bazinga')
        new = Business.objects.get(id = bizz_id)
        self.assertEqual(new.name, 'bazinga')

    def test_hood_search_by_name(self):
        self.new_hood.save()
        hood = Neighbourhood.find_neighborhood('TestArea')
        self.assertTrue(len(hood)== 1)

    def test_profile_search_by_username(self):
        self.new_user.save()
        profile = Profile.search_by_username('jamie')
        self.assertTrue(len(profile)== 1)

    def test_business_search_by_name(self):
        self.new_business.save()
        bizz = Business.search_by_name('Test')
        self.assertTrue(len(bizz)== 1)
