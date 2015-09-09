from rpg.plugin import Plugin
import re


class FindFilePlugin(Plugin):

    def installed(self, project_dir, spec, sack):
        self.files = []
        self.exclude = {}
        for item in list(project_dir.glob('**/*')):
            if (item.is_file() and '__pycache__' not in str(item)):
                self.files.append(("/" + str(item.relative_to(project_dir)),
                                   None, None))
            elif str(item).endswith('__pycache__'):
                self.files.append(("/" + str(item.relative_to(project_dir)) + "/",
                                   None, None))
        sorted_files = sorted(self.files +
                              [(key, r'%exclude', None)
                               for key in self.exclude],
                              key=lambda e: e[0])
        for one_file in sorted_files:
            spec.files.add(one_file)
