from pathlib import Path

from jinja2 import Template

from .create_url import url_scheme, shorten_url

# todo: Pythonista3 以外での`Path` 挙動クッション用
ROOT_PATH: Path = Path(__file__).parent

md_name = 'readmeTemplate.md'
tmp_file = Path(ROOT_PATH, '../opt', md_name)
master_readme = Path(ROOT_PATH, '../../', 'README.md')


def to_override(json_dump: str,
                file_name: str,
                theme_name: str,
                override_file: Path = tmp_file,
                master_file: Path = master_readme):
  if override_file.suffix != '.md':
    # xxx: 雑
    raise print('markdown')
  source_md = override_file.read_text(encoding='utf-8')
  template: Template = Template(source=source_md)
  
  compiled_scheme = url_scheme(json_dump)
  shortened_url = shorten_url(compiled_scheme)
  
  
  
  
  render_kwargs = {
    'h2name': 'おほー',
    'code': 'code',
  }
  rendered = template.render(render_kwargs)
  master_file.write_text(rendered, encoding='utf-8')
  return rendered


# wip: export しないvar も？

