import sublime
import sublime_plugin

settings = sublime.load_settings("Reindent.sublime-settings")


class PasteAndReindent(sublime_plugin.TextCommand):

    def clone_region_set(self, region_set):
        clone = []
        for region in region_set:
            clone.append(region)
        return clone

    def run(self, edit):
        region = self.view.line(self.view.sel()[0]) if len(self.view.sel()) == 1 else None
        command = 'use_paste_and_indent' if settings.get('use_paste_and_indent') else 'paste'
        self.view.run_command(command)
        if region is not None:
            original_sel = self.clone_region_set(self.view.sel())
            selections = self.view.sel()
            for sel in selections:
                self.view.sel().add(sel.cover(region))
            self.view.run_command('reindent')

            for sel in selections:
                selections.subtract(sel)
                selections.add(sublime.Region(sel.end(), sel.end()))


class MoveDownAndReindent(sublime_plugin.TextCommand):

    def run(self, edit):
        syntax = self.view.scope_name(self.view.sel()[0].a).split()[0]
        if syntax in settings.get('exclude_language_from_move'):
            self.view.run_command('swap_line_down')
        else:
            self.view.run_command('expand_selection', {'to': 'line'})
            self.view.run_command('move', {'by': 'characters', 'extend': True, 'forward': False})
            self.view.run_command('swap_line_down')
            self.view.run_command('reindent')


class MoveUpAndReindent(sublime_plugin.TextCommand):

    def run(self, edit):
        syntax = self.view.scope_name(self.view.sel()[0].a).split()[0]
        if syntax in settings.get('exclude_language_from_move'):
            self.view.run_command('swap_line_up')
        else:
            self.view.run_command('expand_selection', {'to': 'line'})
            self.view.run_command('move', {'by': 'characters', 'extend': True, 'forward': False})
            self.view.run_command('swap_line_up')
            self.view.run_command('reindent')
