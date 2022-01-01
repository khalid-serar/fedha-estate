from fedha.models import Business, Neighbourhood, Profile
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
# Set up method
    def setUp(self):
        self.user = User(username="khalid", password="ikmaal855")
        self.user.save()
        self.neighbourhood= Neighbourhood(neighbourhood_name = "karen", neighbourhood_location= "Nairobi", admin = self.user, neighbourhood_description='hood of hoods')
        self.neighbourhood.save()
        self.profile = Profile(bio='my hood',email='khalid@gmail.com', id_number=37810415,user = self.user, neighbourhood = self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

    def test_get_profile(self):
        self.profile.save_profile()
        

    def test_delete_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)
    
class NeighbourhoodTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='jamal')
        self.user.save()
        self.neighbourhood = Neighbourhood(neighbourhood_name='Karen',neighbourhood_location='Nairobi',neighbourhood_description="hood of hoods",neighbourhood_photo='photo.url',admin = self.user)
        self.neighbourhood.create_neighbourhood()


    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_create_neighborhood(self):
        self.neighbourhood.create_neighbourhood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_neighborhood(self):
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

class BusinessTestClass(TestCase):
    # Set up method

    def setUp(self):

        self.user = User(username="khalid", password="ikmaal855")
        self.user.save()
        self.neighbourhood = Neighbourhood(neighbourhood_name="fedha", neighbourhood_location="Nairobi", admin=self.user, neighbourhood_description='our home')
        self.neighbourhood.save()
        self.business = Business(business_name='salama bakery', business_email='salama@gmail.com',business_description='my business')
     

   