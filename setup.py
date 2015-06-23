from distutils.core import setup
try:
    from DistUtilsExtra.command import *
except ImportError:
    missing_distutilsextra = True
else:
    missing_distutilsextra = False


setup_dict = dict(name='freepto-usb-utils',
    version='1.0',
	scripts=['freepto-live-tray'],
	data_files=[
        ('share/applications/', ['livehelper.desktop']),
        ('share/pixmaps/', ['livehelper.ico']),
        ('bin/', ['check-virt', 'usb-disk-utility', 'makefreepto','makepersistence']),
        ('share/freepto-usb-utils/', ['90-livetray']),
        ]
    )

if not missing_distutilsextra:
    setup_dict['cmdclass'] = {
        'build' : build_extra.build_extra,
        'build_i18n': build_i18n.build_i18n,
        }

setup(**setup_dict)
