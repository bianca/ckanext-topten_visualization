import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging

ignore_missing = plugins.toolkit.get_validator('ignore_missing')

class Topten_VisualizationPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'topten_visualization')
    '''
    This extension views a hard-coded visual summary of a resource.
    '''
    def info(self):
        return {'name': 'topten_visualization',
                'title': 'Top Ten Summary',
                'icon': 'table',
                'requires_datastore': False,
                'always_available': True,
                'schema': {
                    'topten_title_1': [ignore_missing],
                    'topten_description_1': [ignore_missing],
                    'topten_title_2': [ignore_missing],
                    'topten_description_2': [ignore_missing],
                    'topten_title_3': [ignore_missing],
                    'topten_description_3': [ignore_missing],
                    'topten_title_4': [ignore_missing],
                    'topten_description_4': [ignore_missing],
                    'topten_title_5': [ignore_missing],
                    'topten_description_5': [ignore_missing],
                    'topten_title_6': [ignore_missing],
                    'topten_description_6': [ignore_missing],
                    'topten_title_7': [ignore_missing],
                    'topten_description_7': [ignore_missing],
                    'topten_title_8': [ignore_missing],
                    'topten_description_8': [ignore_missing],
                    'topten_title_9': [ignore_missing],
                    'topten_description_9': [ignore_missing],
                    'topten_title_10': [ignore_missing],
                    'topten_description_10': [ignore_missing]
                },
                'default_title': plugins.toolkit._('Top Ten Summary'),
                }

    def can_view(self, data_dict):
      return True

    def view_template(self, context, data_dict):
        return 'topten_view.html'

    def form_template(self, context, data_dict):
        return 'topten_form.html'