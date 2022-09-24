from django.db import models


class Template(models.Model):
    templates = models.Manager()
    en = models.TextField()
    ru = models.TextField()
    uz = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        for lang in ['uz', 'ru']:
            file_name = f'locale/{lang}/LC_MESSAGES/django.po'
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(r'msgid ""')
                file.write('\n')
                file.write(r'msgstr ""')
                file.write('\n')
                file.write(r'"Project-Id-Version: 1.0.0\n"')
                file.write('\n')
                file.write(r'"Report-Msgid-Bugs-To: \n"')
                file.write('\n')
                file.write(r'"POT-Creation-Date: 2013-10-04 13:06-0500\n"')
                file.write('\n')
                file.write(r'"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"')
                file.write('\n')
                file.write(r'"Last-Translator: XXXXX\n"')
                file.write('\n')
                file.write(r'"Language-Team: Es XXXX\n"')
                file.write('\n')
                file.write(r'"Language: Es\n"')
                file.write('\n')
                file.write(r'"MIME-Version: 1.0\n"')
                file.write('\n')
                file.write(r'"Content-Type: text/plain; charset=UTF-8\n"')
                file.write('\n')
                file.write(r'"Content-Transfer-Encoding: 8bit\n"')
                file.write('\n')
                file.write(r'"Plural-Forms: nplurals=2; plural=(n != 1);\n"')
                file.write('\n')
                file.write('\n')

                for template in Template.templates.all():
                    file.write(f"""msgid "{template.get("en")}"\n""")
                    file.write(f"""msgstr "{template.get(lang)}"\n""")
                    file.write("\n")

        return result

    def get(self, lang):
        return getattr(self, lang)

    def __str__(self):
        return self.en
