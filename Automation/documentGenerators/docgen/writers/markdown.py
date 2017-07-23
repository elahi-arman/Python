from docgen.writers.base import Base

class MarkdownGenerator(Base):
    """docstring for MarkdownGenerator."""
    def __init__(self):
        super(MarkdownGenerator, self).__init__()
        self.document = []

    def write(self, filehandle):
        """Write self.document to open filehandle, return true on success"""
        try:
            for element in self.document:
                filehandle.write(element.string)
                return True
        except IOError:
            return False

    @staticmethod
    def paragraph(string, shouldContinue=True):
        """Converts string to paragraph, adds lines if shouldContinue."""
        if not shouldContinue:
            return MarkdownGenerator.Element('p', '{}\n\n'.format(string))
        return MarkdownGenerator.Element('p', '{}\n')

    @staticmethod
    def heading(string):
        """Convert string to a heading."""
        return MarkdownGenerator.Element('h1', '{}\n===\n\n'.format(string))

    @staticmethod
    def subheading(string):
        """Convert string to a subheading."""
        return MarkdownGenerator.Element('h2', '{}\n---\n\n'.format(string))

    @staticmethod
    def unordered_list(currentList):
        """Convert currentList into a set of unordered list items."""
        return MarkdownGenerator.Element('ul', '{}\n\n'.format(
            ['* {}\n'.format(string) for string in currentList]
        ))

    @staticmethod
    def ordered_list(currentList):
        """Convert currentList into a set of ordered list items."""
        return MarkdownGenerator.Element('ol', '{}\n\n'.format(
            ['1. {}\n'.format(string) for string in currentList]
        ))

    @staticmethod
    def link(linkText, link):
        """Convert link and linkText to a link."""
        return MarkdownGenerator.Element('a', '[{}]({})'.format(linkText, link))

    @staticmethod
    def image(altText, path):
        """Convert altText and path to an image."""
        return MarkdownGenerator.Element('img', '![{}]({})'.format(altText, path))

    @staticmethod
    def bold(string):
        """Convert string to a bolded string."""
        return MarkdownGenerator.Element('b', '**{}**'.format(string))

    @staticmethod
    def italic(string):
        """Convert string to an italicized string."""
        return MarkdownGenerator.Element('i', '__{}__'.format(string))

    @staticmethod
    def inline_code(string):
        """Convert string to inline code."""
        return MarkdownGenerator.Element('code', '`{}`'.format(string))

    @staticmethod
    def code_block(codeLines):
        """Convert list of strings to a set of preformatted code lines."""
        return MarkdownGenerator.Element('pre', '{}'.format(
            ['\t{}\n'.format(loc) for loc in codeLines])
        )
