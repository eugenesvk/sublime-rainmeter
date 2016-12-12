import sublime
import sublime_plugin
import subprocess
import os

if sublime.platform() == 'windows':
    import ctypes
    from ctypes import c_int32, c_uint32, c_void_p, c_wchar_p, POINTER

    class CHOOSECOLOR(ctypes.Structure):
        _fields_ = [('lStructSize', c_uint32),
                    ('hwndOwner', c_void_p),
                    ('hInstance', c_void_p),
                    ('rgbResult', c_uint32),
                    ('lpCustColors', POINTER(c_uint32)),
                    ('Flags', c_uint32),
                    ('lCustData', c_void_p),
                    ('lpfnHook', c_void_p),
                    ('lpTemplateName', c_wchar_p)]

    CustomColorArray = c_uint32 * 16
    CC_SOLIDCOLOR = 0x80
    CC_RGBINIT = 0x01
    CC_FULLOPEN = 0x02

    ChooseColorW = ctypes.windll.Comdlg32.ChooseColorW
    ChooseColorW.argtypes = [POINTER(CHOOSECOLOR)]
    ChooseColorW.restype = c_int32

    GetDC = ctypes.windll.User32.GetDC
    GetDC.argtypes = [c_void_p]
    GetDC.restype = c_void_p

    ReleaseDC = ctypes.windll.User32.ReleaseDC
    ReleaseDC.argtypes = [c_void_p, c_void_p]  # hwnd, hdc
    ReleaseDC.restype = c_int32


class RainmeterColorPickCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sel = self.view.sel()
        start_color = None
        start_color_osx = None
        start_color_win = 0x000000

        # Get the currently selected color - if any
        if len(sel) > 0:
            selected = self.view.substr(self.view.word(sel[0])).strip()
            if selected.startswith('#'):
                selected = selected[1:]
            if self.__is_valid_hex_color(selected):
                if len(selected) > 6:
                    selected = selected[0:6]
                start_color = "#" + selected
                start_color_osx = selected
                start_color_win = self.__hexstr_to_bgr(selected)

        if sublime.platform() == 'windows':

            s = sublime.load_settings("ColorPicker.sublime-settings")
            custom_colors = s.get("custom_colors", ['0'] * 16)

            if len(custom_colors) < 16:
                custom_colors = ['0'] * 16
                s.set('custom_colors', custom_colors)

            cc = CHOOSECOLOR()
            ctypes.memset(ctypes.byref(cc), 0, ctypes.sizeof(cc))
            cc.lStructSize = ctypes.sizeof(cc)
            cc.hwndOwner = None
            cc.Flags = CC_SOLIDCOLOR | CC_FULLOPEN | CC_RGBINIT
            cc.rgbResult = c_uint32(start_color_win)
            cc.lpCustColors = self.__to_custom_color_array(custom_colors)

            if ChooseColorW(ctypes.byref(cc)):
                color = self.__bgr_to_hexstr(cc.rgbResult)
            else:
                color = None

        elif sublime.platform() == 'osx':
            location = os.path.join(sublime.packages_path(),
                                    'Rainmeter',
                                    'lib',
                                    'osx_colorpicker')
            args = [location]

            if not os.access(location, os.X_OK):
                os.chmod(location, 0o755)

            if start_color_osx:
                args.append('-startColor')
                args.append(start_color_osx)

        else:
            location = os.path.join(sublime.packages_path(),
                                    'Rainmeter',
                                    'lib',
                                    'linux_colorpicker.py')
            args = [location]

            if not os.access(location, os.X_OK):
                os.chmod(location, 0o755)

            if start_color:
                args.append(start_color)

        if sublime.platform() == 'osx' or sublime.platform() == 'linux':
            proc = subprocess.Popen(args, stdout=subprocess.PIPE)
            color = proc.communicate()[0].strip()

        if color:
            # Replace all regions with color
            for region in sel:
                word = self.view.word(region)
                # If the selected word is a valid color, replace it
                if self.__is_valid_hex_color(self.view.substr(word)):
                    if len(self.view.substr(word)) > 6:
                        word = sublime.Region(word.a, word.a + 6)
                    # Include '#' if present
                    self.view.replace(edit, word, color)
                # If the selected region starts with a #, keep it
                elif self.view.substr(region).startswith('#'):
                    reduced = sublime.Region(region.begin() + 1, region.end())
                    if self.__is_valid_hex_color(self.view.substr(reduced)):
                        if len(reduced) > 6:
                            reduced = sublime.Region(reduced.a, reduced.a + 6)
                        self.view.replace(edit, reduced, color)
                    else:
                        self.view.replace(edit, region, '#' + color)
                # Otherwise just replace the selected region
                else:
                    self.view.replace(edit, region, color)

    @classmethod
    def __to_custom_color_array(cls, custom_colors):
        cc = CustomColorArray()
        for i in range(16):
            cc[i] = int(custom_colors[i])
        return cc

    @classmethod
    def __from_custom_color_array(cls, custom_colors):
        cc = [0] * 16
        for i in range(16):
            cc[i] = str(custom_colors[i])
        return cc

    @classmethod
    def __is_valid_hex_color(cls, s):
        if len(s) not in (3, 6, 8):
            return False
        try:
            return 0 <= int(s, 16) <= 0xffffffff
        except ValueError:
            return False

    byte_table = list(['{0:02X}'.format(b) for b in range(256)])

    @classmethod
    def __bgr_to_hexstr(cls, bgr):
        # 0x00BBGGRR
        b = cls.byte_table[(bgr >> 16) & 0xff]
        g = cls.byte_table[(bgr >> 8) & 0xff]
        r = cls.byte_table[bgr & 0xff]

        return r + g + b

    @classmethod
    def __hexstr_to_bgr(cls, hexstr):
        if len(hexstr) == 3:
            hexstr = hexstr[0] + hexstr[0] + hexstr[1] + \
                hexstr[1] + hexstr[2] + hexstr[2]

        red = int(hexstr[0:2], 16)
        green = int(hexstr[2:4], 16)
        blue = int(hexstr[4:6], 16)

        return (blue << 16) | (green << 8) | red
