from unittest import TestCase
import subprocess

class TestScript(TestCase):
    def test_wo_error(self):
        querries = ['name=Keith Jarrett',
            'name=ABC Impulse!',
            'title=Shades',
            'id=3318191']
        for q in querries:
            print q
            exit_code = subprocess.call(['discogs-finder', q])
            assert exit_code == 0