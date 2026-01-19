from django.test import TestCase, Client
from django.urls import reverse
from .models import Feedback
import json

class FeedbackTests(TestCase):
    def test_submit_feedback(self):
        client = Client()
        url = reverse('submit_feedback')
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test feedback.'
        }
        response = client.post(url, json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertTrue(Feedback.objects.filter(name='Test User').exists())

    def test_index_view_elements(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        
        # Verify Stop Camera Button
        self.assertIn('stopCameraAccess()', content)
        self.assertIn('Stop Camera Access', content)
        
        # Verify Feedback Form Elements
        self.assertIn('We value your feedback', content)
        self.assertIn('feedbackForm', content)
        self.assertIn('submitFeedback(event)', content)
