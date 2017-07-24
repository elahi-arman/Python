from Docgen.Writers.Markdown import MarkdownGenerator

def test_paragraph():
     out =  MarkdownGenerator.paragraph('herp')
     assert out.semantic == 'p'
     assert out.string == 'herp\n'

def test_paragraph_no_continue():
    out =  MarkdownGenerator.paragraph('herp', shouldContinue=False)
    assert out.semantic == 'p'
    assert out.string == 'herp\n\n'

def test_heading():
    out = MarkdownGenerator.heading('herp')
    assert out.semantic == 'h1'
    assert out.string == 'herp\n===\n\n'

def test_subheading():
    out = MarkdownGenerator.subheading('herp')
    assert out.semantic == 'h2'
    assert out.string == 'herp\n---\n\n'

def test_unordered_list():
    out = MarkdownGenerator.unordered_list(['herp', 'derp', 'boop'])
    print(out.string)
    assert out.semantic == 'ul'
    assert out.string == '* herp\n* derp\n* boop\n\n'

def test_ordered_list():
    out = MarkdownGenerator.ordered_list(['herp', 'derp', 'boop'])
    print(out.string)

    assert out.semantic == 'ol'
    assert out.string == '1. herp\n1. derp\n1. boop\n\n'

def test_link():
    out = MarkdownGenerator.link('herp', 'derp')
    assert out.semantic == 'a'
    assert out.string == '[herp](derp)'

def test_image():
    out = MarkdownGenerator.image('herp', 'derp')
    assert out.semantic == 'img'
    assert out.string == '![herp](derp)'

def test_bold():
    out = MarkdownGenerator.bold('herp')
    assert out.semantic == 'b'
    assert out.string == '**herp**'

def test_italic():
    out = MarkdownGenerator.italic('herp')
    assert out.semantic == 'i'
    assert out.string == '__herp__'

def test_inline_code():
    out = MarkdownGenerator.inline_code('herp')
    assert out.semantic == 'code'
    assert out.string == '`herp`'

def test_code_block():
    out = MarkdownGenerator.code_block(['herp', 'derp', 'boop'])
    assert out.semantic == 'pre'
    assert out.string == '\therp\n\tderp\n\tboop\n'

def test_successful_write():
    import io

    doc = MarkdownGenerator()
    doc.document = [
        MarkdownGenerator.heading('Test Document'),
        MarkdownGenerator.paragraph('Yay, wrote something out')
    ]

    f = io.StringIO()
    doc.write(f)
    f.seek(0)

    output = f.read()

    assert (output ==
        MarkdownGenerator.heading('Test Document').string +
        MarkdownGenerator.paragraph('Yay, wrote something out').string)
