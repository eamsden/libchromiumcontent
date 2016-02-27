#!/usr/bin/env python

import os
import glob
import shutil
from lib.util import get_configuration, get_output_dir

SOURCE_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..'))
DIST_DIR = os.path.join(SOURCE_ROOT, 'dist')
MAIN_DIR = os.path.join(DIST_DIR, 'main')

BINARIES = {
  'all': [
    os.path.join('gen', 'extensions', 'extensions_resources.pak'),
    os.path.join('gen', 'extensions', 'extensions_renderer_resources.pak'),
    os.path.join('gen', 'chrome', 'extensions_api_resources.pak'),
  ],
  'darwin': [
    'libapi_gen_util.a',
    'libbrowsing_data.a',
    'libcast_common.a',
    'libcast_net.a',
    'libchrome_api.a',
    'libchrome_zlib.a',
    'libcld2_static.a',
    'libcommon.a',
    'libcommon_constants.a',
    'libcommon_net.a',
    'libcontent_settings_core_common.a',
    'libcrx_file.a',
    'libdevice_usb.a',
    'libextensions_api.a',
    'libextensions_api_registration.a',
    'libextensions_browser.a',
    'libextensions_common.a',
    'libextensions_common_constants.a',
    'libextensions_renderer.a',
    'libextensions_utility.a',
    'libguest_view_browser.a',
    'libguest_view_common.a',
    'libguest_view_renderer.a',
    'libleveldatabase.a',
    'libmojo_cpp_bindings.a',
    'libmojo_environment_chromium.a',
    'libmojo_js_bindings.a',
    'libpref_registry.a',
    'libre2.a',
    'libsafe_browsing_proto.a',
    'libsnappy.a',
    'libsyncable_prefs.a',
    'libui_zoom.a',
    'libvariations.a',
    'libversion_info.a',
    'libweb_cache_browser.a',
    'libweb_cache_common.a',
    'libweb_modal.a',
    'libxml2.a',
    'libzlib_x86_simd.a',
  ],
  'linux': [
    'libapi_gen_util.a',
    'libbrowsing_data.a',
    'libcast_common.a',
    'libcast_net.a',
    'libchrome_api.a',
    'libchrome_zlib.a',
    'libcld2_static.a',
    'libcommon.a',
    'libcommon_constants.a',
    'libcommon_net.a',
    'libcontent_settings_core_common.a',
    'libcrx_file.a',
    'libdevice_usb.a',
    'libextensions_api.a',
    'libextensions_api_registration.a',
    'libextensions_browser.a',
    'libextensions_common.a',
    'libextensions_common_constants.a',
    'libextensions_renderer.a',
    'libextensions_utility.a',
    'libguest_view_browser.a',
    'libguest_view_common.a',
    'libguest_view_renderer.a',
    'libleveldatabase.a',
    'libmojo_cpp_bindings.a',
    'libmojo_environment_chromium.a',
    'libmojo_js_bindings.a',
    'libpref_registry.a',
    'libre2.a',
    'libsafe_browsing_proto.a',
    'libsnappy.a',
    'libsyncable_prefs.a',
    'libui_zoom.a',
    'libvariations.a',
    'libversion_info.a',
    'libweb_cache_browser.a',
    'libweb_cache_common.a',
    'libweb_modal.a',
    'libxml2.a',
    'libzlib_x86_simd.a',
  ],
  'win32': [
    'libapi_gen_util.lib',
    'libbrowsing_data.lib',
    'libcast_common.lib',
    'libcast_net.lib',
    'libchrome_api.lib',
    'libchrome_zlib.lib',
    'libcld2_static.lib',
    'libcommon.lib',
    'libcommon_constants.lib',
    'libcommon_net.lib',
    'libcontent_settings_core_common.lib',
    'libcrx_file.lib',
    'libdevice_usb.lib',
    'libextensions_api.lib',
    'libextensions_api_registration.lib',
    'libextensions_browser.lib',
    'libextensions_common.lib',
    'libextensions_common_constants.lib',
    'libextensions_renderer.lib',
    'libextensions_utility.lib',
    'libguest_view_browser.lib',
    'libguest_view_common.lib',
    'libguest_view_renderer.lib',
    'libleveldatabase.lib',
    'libmojo_cpp_bindings.lib',
    'libmojo_environment_chromium.lib',
    'libmojo_js_bindings.lib',
    'libpref_registry.lib',
    'libre2.lib',
    'libsafe_browsing_proto.lib',
    'libsnappy.lib',
    'libsyncable_prefs.lib',
    'libui_zoom.lib',
    'libvariations.lib',
    'libversion_info.lib',
    'libweb_cache_browser.lib',
    'libweb_cache_common.lib',
    'libweb_modal.lib',
    'libxml2.lib',
    'libzlib_x86_simd.lib',
  ],
}

INCLUDE_DIRS = [
  'extensions/browser',
  'extensions/common',
  'extensions/components',
  'extensions/renderer',
  'extensions/strings',
  'extensions/utility',
  'sync/api',
  'sync/base',
  'sync/internal_api',
  'components/user_prefs',
  'components/pref_registry',
  'components/syncable_prefs',
  'components/keyed_service',
  'components/web_modal',
  'components/crx_file',
  'chrome/common/extensions',
]
GENERATED_INCLUDE_DIRS = [
  'chrome',
  'extensions',
]
OTHER_HEADERS = [
  'chrome/common/chrome_isolated_world_ids.h',
  'chrome/common/url_constants.h',
]
OTHER_DIRS = [
  'build',
  'tools/grit',
]

def copy_extension_locales(target_arch, component, output_dir):
  config = get_configuration(target_arch)
  target_dir = os.path.join(MAIN_DIR, component, 'locales')
  src_dir = os.path.join(output_dir, config, 'gen', 'extensions', 'strings', 'extension_strings')
  for src_file in glob.glob(os.path.join(src_dir, 'extension_strings_*.pak')):
    filename = os.path.basename(src_file)
    new_name = re.sub('extension_strings_', '', filename)
    shutil.copy2(src_file, os.path.join(target_dir, new_name))

