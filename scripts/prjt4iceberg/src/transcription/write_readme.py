from pathlib import Path

from jinja2 import Template

from .create_url import url_scheme, shorten_url

# todo: Pythonista3 以外での`Path` 挙動クッション用
ROOT_PATH: Path = Path(__file__).parent
tmp_dir = Path(ROOT_PATH, '../opt')

readme_template = 'readmeTemplate.md'
section_template = 'sectionTemplate.md'


def create_section(json_dump: str,
                   file_name: str,
                   theme_name: str,
                   override_file: Path = tmp_file,
                   section_file: Path = tmp_dir + section_template) -> str:
  if section_file.suffix != '.md':
    # xxx: 雑
    raise print('section markdown')
  section_md = section_file.read_text(encoding='utf-8')
  template: Template = Template(source=section_md)

  compiled_scheme = url_scheme(json_dump)
  shortened_url = shorten_url(compiled_scheme)

  render_kwargs = {
    'name_header': theme_name,
    'link_name': file_name,
    'link_url': shorten_url,
    'scheme_raw': compiled_scheme,
  }
  rendered = template.render(render_kwargs)
  return rendered


def to_override(*args):
  new_line = '\n'
  
  sections = (new_line * 2).join(args)
  
  
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

