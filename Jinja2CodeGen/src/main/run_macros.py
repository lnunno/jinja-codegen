'''
Created on Aug 1, 2013

@author: lnunno
'''
import jinja2
from jinja2.loaders import FileSystemLoader
import os

class JinjaProperties(object):
    '''Classdocs
    '''
    
    def __init__(self,render_path="renders/",template_path="templates/",env=None):
        '''docs
        '''
        self.render_path = render_path        
        self.template_path = template_path
        env = jinja2.Environment(loader=FileSystemLoader(template_path),
                                 trim_blocks=True, 
                                 lstrip_blocks=True,
                                 extensions=['jinja2.ext.do'])        
        self.env = env        


def run_macros():
    props = JinjaProperties()
    env = props.env
    template = env.get_template('python_examples.html')
    save_rendered_template(template, {}, os.path.join(props.render_path,'macro_out.py'))
    
def save_rendered_template(template,variables,outfile):
    with open(outfile,'w') as f:
        f.write(template.render(variables))
    
def main():
    run_macros()
    
if __name__ == '__main__':
    main()