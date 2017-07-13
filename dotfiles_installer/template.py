import pystache


def render_template_to_string(tmpl, context) -> str:
    return pystache.render(tmpl, context)


def render_file_to_string(file_path, context) -> str:
    with open(file_path) as f:
        return render_template_to_string(f.read(), context)
