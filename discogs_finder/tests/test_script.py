from unittest import TestCase
import subprocess

class TestScript(TestCase):
    def test_wo_error(self):
        querries = ['name=Keith Jarrett',
            'name=ABC Impulse!',
            'title=Shades',
            'id=3318191']
        for q in querries:
            try:
                exit_code = subprocess.call(['discogs-finder',
                                             '--u', 'tim6her', q])
                assert exit_code == 0
            except OSError:
                pass