from setup import ExtensionInstaller

def loader():
    return ObserverIPInstaller()

class ObserverIPInstaller(ExtensionInstaller):
    def __init__(self):
        super(ObserverIPInstaller, self).__init__(
                version="1.0",
                name='observerip',
                description='driver for Ambient ObserverIP',
                author="Pat OBrien",
                config={
                    'ObserverIP': {
                        'loop_interval': '15',
                        'ip_address': '192.168.0.55',
                        'hardware': 'Ambient Weather WS-1200-IP with ObserverIP',
                        'driver': 'user.observerip',
                    }
                },
                files=[('bin/user', ['bin/user/observerip.py'])]
                )
