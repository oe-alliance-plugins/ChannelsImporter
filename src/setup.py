from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.ChannelsImporter'
setup(name='enigma2-plugin-systemplugins-channelsimporter',
       version='3.0',
       description='channelsimporter...',
       package_dir={pkg: 'ChannelsImporter'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'setup.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
