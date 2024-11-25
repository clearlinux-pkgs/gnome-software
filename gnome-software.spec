#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: 5424026
#
Name     : gnome-software
Version  : 47.2
Release  : 94
URL      : https://download.gnome.org/sources/gnome-software/47/gnome-software-47.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-software/47/gnome-software-47.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-software-bin = %{version}-%{release}
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-lib = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}
Requires: gnome-software-locales = %{version}-%{release}
Requires: gnome-software-man = %{version}-%{release}
Requires: clr-bundle-icons
Requires: clr-bundle-screenshots
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : libsoup-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(appstream)
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(flatpak)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gspell-1)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(xmlb)
BuildRequires : source-highlight
BuildRequires : valgrind-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build Status](https://gitlab.gnome.org/GNOME/gnome-software/badges/main/pipeline.svg)](https://gitlab.gnome.org/GNOME/gnome-software/pipelines)

%package bin
Summary: bin components for the gnome-software package.
Group: Binaries
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}

%description bin
bin components for the gnome-software package.


%package data
Summary: data components for the gnome-software package.
Group: Data

%description data
data components for the gnome-software package.


%package dev
Summary: dev components for the gnome-software package.
Group: Development
Requires: gnome-software-lib = %{version}-%{release}
Requires: gnome-software-bin = %{version}-%{release}
Requires: gnome-software-data = %{version}-%{release}
Provides: gnome-software-devel = %{version}-%{release}
Requires: gnome-software = %{version}-%{release}

%description dev
dev components for the gnome-software package.


%package doc
Summary: doc components for the gnome-software package.
Group: Documentation
Requires: gnome-software-man = %{version}-%{release}

%description doc
doc components for the gnome-software package.


%package lib
Summary: lib components for the gnome-software package.
Group: Libraries
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}

%description lib
lib components for the gnome-software package.


%package libexec
Summary: libexec components for the gnome-software package.
Group: Default
Requires: gnome-software-license = %{version}-%{release}

%description libexec
libexec components for the gnome-software package.


%package license
Summary: license components for the gnome-software package.
Group: Default

%description license
license components for the gnome-software package.


%package locales
Summary: locales components for the gnome-software package.
Group: Default

%description locales
locales components for the gnome-software package.


%package man
Summary: man components for the gnome-software package.
Group: Default

%description man
man components for the gnome-software package.


%prep
%setup -q -n gnome-software-47.2
cd %{_builddir}/gnome-software-47.2
pushd ..
cp -a gnome-software-47.2 buildavx2
popd
pushd ..
cp -a gnome-software-47.2 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732556182
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfwupd=false \
-Dgtk_doc=false \
-Dmalcontent=false \
-Dpackagekit=false \
-Dpackagekit_autoremove=false \
-Drpm_ostree=false \
-Dsnap=false \
-Dsysprof=disabled \
-Dhardcoded_foss_webapps=false \
-Dhardcoded_proprietary_webapps=false \
-Dwebapps=false \
-Dtests=false \
-Dexternal_appstream=false  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfwupd=false \
-Dgtk_doc=false \
-Dmalcontent=false \
-Dpackagekit=false \
-Dpackagekit_autoremove=false \
-Drpm_ostree=false \
-Dsnap=false \
-Dsysprof=disabled \
-Dhardcoded_foss_webapps=false \
-Dhardcoded_proprietary_webapps=false \
-Dwebapps=false \
-Dtests=false \
-Dexternal_appstream=false  builddiravx2
ninja -v -C builddiravx2
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 "  meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfwupd=false \
-Dgtk_doc=false \
-Dmalcontent=false \
-Dpackagekit=false \
-Dpackagekit_autoremove=false \
-Drpm_ostree=false \
-Dsnap=false \
-Dsysprof=disabled \
-Dhardcoded_foss_webapps=false \
-Dhardcoded_proprietary_webapps=false \
-Dwebapps=false \
-Dtests=false \
-Dexternal_appstream=false   builddirapx
ninja -v -C builddirapx

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-software
cp %{_builddir}/gnome-software-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-software/4cc77b90af91e615a64ae04893fdffa7939db84c || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v3
DESTDIR=%{buildroot}-va ninja -C builddirapx install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-software
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gnome-software
/VA/usr/bin/gnome-software
/usr/bin/gnome-software

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-software-local-file-flatpak.desktop
/usr/share/applications/org.gnome.Software.desktop
/usr/share/bash-completion/completions/gnome-software
/usr/share/dbus-1/services/org.gnome.Software.service
/usr/share/glib-2.0/schemas/org.gnome.software.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Software-search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Software.svg
/usr/share/icons/hicolor/scalable/categories/system-component-addon.svg
/usr/share/icons/hicolor/scalable/categories/system-component-application.svg
/usr/share/icons/hicolor/scalable/categories/system-component-codecs.svg
/usr/share/icons/hicolor/scalable/categories/system-component-driver.svg
/usr/share/icons/hicolor/scalable/categories/system-component-firmware.svg
/usr/share/icons/hicolor/scalable/categories/system-component-input-sources.svg
/usr/share/icons/hicolor/scalable/categories/system-component-language.svg
/usr/share/icons/hicolor/scalable/categories/system-component-os-updates.svg
/usr/share/icons/hicolor/scalable/categories/system-component-runtime.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Software-symbolic.svg
/usr/share/metainfo/org.gnome.Software.Plugin.Flatpak.metainfo.xml
/usr/share/metainfo/org.gnome.Software.metainfo.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-software/gnome-software.h
/usr/include/gnome-software/gs-app-collation.h
/usr/include/gnome-software/gs-app-list.h
/usr/include/gnome-software/gs-app-permissions.h
/usr/include/gnome-software/gs-app-query.h
/usr/include/gnome-software/gs-app.h
/usr/include/gnome-software/gs-appstream.h
/usr/include/gnome-software/gs-category-manager.h
/usr/include/gnome-software/gs-category.h
/usr/include/gnome-software/gs-desktop-data.h
/usr/include/gnome-software/gs-download-utils.h
/usr/include/gnome-software/gs-enums.h
/usr/include/gnome-software/gs-external-appstream-utils.h
/usr/include/gnome-software/gs-icon-downloader.h
/usr/include/gnome-software/gs-icon.h
/usr/include/gnome-software/gs-ioprio.h
/usr/include/gnome-software/gs-job-manager.h
/usr/include/gnome-software/gs-key-colors.h
/usr/include/gnome-software/gs-metered.h
/usr/include/gnome-software/gs-odrs-provider.h
/usr/include/gnome-software/gs-os-release.h
/usr/include/gnome-software/gs-plugin-event.h
/usr/include/gnome-software/gs-plugin-helpers.h
/usr/include/gnome-software/gs-plugin-job-cancel-offline-update.h
/usr/include/gnome-software/gs-plugin-job-download-upgrade.h
/usr/include/gnome-software/gs-plugin-job-file-to-app.h
/usr/include/gnome-software/gs-plugin-job-install-apps.h
/usr/include/gnome-software/gs-plugin-job-launch.h
/usr/include/gnome-software/gs-plugin-job-list-apps.h
/usr/include/gnome-software/gs-plugin-job-list-categories.h
/usr/include/gnome-software/gs-plugin-job-list-distro-upgrades.h
/usr/include/gnome-software/gs-plugin-job-manage-repository.h
/usr/include/gnome-software/gs-plugin-job-refine.h
/usr/include/gnome-software/gs-plugin-job-refresh-metadata.h
/usr/include/gnome-software/gs-plugin-job-trigger-upgrade.h
/usr/include/gnome-software/gs-plugin-job-uninstall-apps.h
/usr/include/gnome-software/gs-plugin-job-update-apps.h
/usr/include/gnome-software/gs-plugin-job-url-to-app.h
/usr/include/gnome-software/gs-plugin-job.h
/usr/include/gnome-software/gs-plugin-loader-sync.h
/usr/include/gnome-software/gs-plugin-loader.h
/usr/include/gnome-software/gs-plugin-types.h
/usr/include/gnome-software/gs-plugin-vfuncs.h
/usr/include/gnome-software/gs-plugin.h
/usr/include/gnome-software/gs-remote-icon.h
/usr/include/gnome-software/gs-rewrite-resources.h
/usr/include/gnome-software/gs-test.h
/usr/include/gnome-software/gs-utils.h
/usr/include/gnome-software/gs-worker-thread.h
/usr/lib64/pkgconfig/gnome-software.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/gnome\-software/*
/usr/share/help/C/gnome-software/figures/app-context-bar.png
/usr/share/help/C/gnome-software/figures/app-screenshot.png
/usr/share/help/C/gnome-software/figures/carousel.png
/usr/share/help/C/gnome-software/figures/install-webapp-from-gnome-web.png
/usr/share/help/C/gnome-software/figures/scalable/license-community-built.svg
/usr/share/help/C/gnome-software/figures/scalable/license-proprietary-and-special.svg
/usr/share/help/C/gnome-software/figures/scalable/license-unknown.svg
/usr/share/help/C/gnome-software/figures/scalable/links.svg
/usr/share/help/C/gnome-software/figures/scalable/no-links.svg
/usr/share/help/C/gnome-software/figures/scalable/symbolic/computer-fail-symbolic.svg
/usr/share/help/C/gnome-software/figures/scalable/symbolic/contact-symbolic.svg
/usr/share/help/C/gnome-software/figures/scalable/symbolic/donate-symbolic.svg
/usr/share/help/C/gnome-software/figures/scalable/symbolic/help-link-symbolic.svg
/usr/share/help/C/gnome-software/figures/scalable/symbolic/image-missing-symbolic.svg
/usr/share/help/C/gnome-software/figures/scalable/symbolic/translations-symbolic.svg
/usr/share/help/C/gnome-software/figures/scalable/symbolic/webpage-symbolic.svg
/usr/share/help/C/gnome-software/how-to-reinstall-a-web-app.page
/usr/share/help/C/gnome-software/index.page
/usr/share/help/C/gnome-software/legal.xml
/usr/share/help/C/gnome-software/software-licensing.page
/usr/share/help/C/gnome-software/software-metadata.page
/usr/share/help/de/gnome-software/figures/app-context-bar.png
/usr/share/help/de/gnome-software/figures/app-screenshot.png
/usr/share/help/de/gnome-software/figures/carousel.png
/usr/share/help/de/gnome-software/figures/install-webapp-from-gnome-web.png
/usr/share/help/de/gnome-software/figures/scalable/license-community-built.svg
/usr/share/help/de/gnome-software/figures/scalable/license-proprietary-and-special.svg
/usr/share/help/de/gnome-software/figures/scalable/license-unknown.svg
/usr/share/help/de/gnome-software/figures/scalable/links.svg
/usr/share/help/de/gnome-software/figures/scalable/no-links.svg
/usr/share/help/de/gnome-software/figures/scalable/symbolic/computer-fail-symbolic.svg
/usr/share/help/de/gnome-software/figures/scalable/symbolic/contact-symbolic.svg
/usr/share/help/de/gnome-software/figures/scalable/symbolic/donate-symbolic.svg
/usr/share/help/de/gnome-software/figures/scalable/symbolic/help-link-symbolic.svg
/usr/share/help/de/gnome-software/figures/scalable/symbolic/image-missing-symbolic.svg
/usr/share/help/de/gnome-software/figures/scalable/symbolic/translations-symbolic.svg
/usr/share/help/de/gnome-software/figures/scalable/symbolic/webpage-symbolic.svg
/usr/share/help/de/gnome-software/how-to-reinstall-a-web-app.page
/usr/share/help/de/gnome-software/index.page
/usr/share/help/de/gnome-software/legal.xml
/usr/share/help/de/gnome-software/software-licensing.page
/usr/share/help/de/gnome-software/software-metadata.page
/usr/share/help/hu/gnome-software/figures/app-context-bar.png
/usr/share/help/hu/gnome-software/figures/app-screenshot.png
/usr/share/help/hu/gnome-software/figures/carousel.png
/usr/share/help/hu/gnome-software/figures/install-webapp-from-gnome-web.png
/usr/share/help/hu/gnome-software/figures/scalable/license-community-built.svg
/usr/share/help/hu/gnome-software/figures/scalable/license-proprietary-and-special.svg
/usr/share/help/hu/gnome-software/figures/scalable/license-unknown.svg
/usr/share/help/hu/gnome-software/figures/scalable/links.svg
/usr/share/help/hu/gnome-software/figures/scalable/no-links.svg
/usr/share/help/hu/gnome-software/figures/scalable/symbolic/computer-fail-symbolic.svg
/usr/share/help/hu/gnome-software/figures/scalable/symbolic/contact-symbolic.svg
/usr/share/help/hu/gnome-software/figures/scalable/symbolic/donate-symbolic.svg
/usr/share/help/hu/gnome-software/figures/scalable/symbolic/help-link-symbolic.svg
/usr/share/help/hu/gnome-software/figures/scalable/symbolic/image-missing-symbolic.svg
/usr/share/help/hu/gnome-software/figures/scalable/symbolic/translations-symbolic.svg
/usr/share/help/hu/gnome-software/figures/scalable/symbolic/webpage-symbolic.svg
/usr/share/help/hu/gnome-software/how-to-reinstall-a-web-app.page
/usr/share/help/hu/gnome-software/index.page
/usr/share/help/hu/gnome-software/legal.xml
/usr/share/help/hu/gnome-software/software-licensing.page
/usr/share/help/hu/gnome-software/software-metadata.page
/usr/share/help/id/gnome-software/figures/app-context-bar.png
/usr/share/help/id/gnome-software/figures/app-screenshot.png
/usr/share/help/id/gnome-software/figures/carousel.png
/usr/share/help/id/gnome-software/figures/install-webapp-from-gnome-web.png
/usr/share/help/id/gnome-software/figures/scalable/license-community-built.svg
/usr/share/help/id/gnome-software/figures/scalable/license-proprietary-and-special.svg
/usr/share/help/id/gnome-software/figures/scalable/license-unknown.svg
/usr/share/help/id/gnome-software/figures/scalable/links.svg
/usr/share/help/id/gnome-software/figures/scalable/no-links.svg
/usr/share/help/id/gnome-software/figures/scalable/symbolic/computer-fail-symbolic.svg
/usr/share/help/id/gnome-software/figures/scalable/symbolic/contact-symbolic.svg
/usr/share/help/id/gnome-software/figures/scalable/symbolic/donate-symbolic.svg
/usr/share/help/id/gnome-software/figures/scalable/symbolic/help-link-symbolic.svg
/usr/share/help/id/gnome-software/figures/scalable/symbolic/image-missing-symbolic.svg
/usr/share/help/id/gnome-software/figures/scalable/symbolic/translations-symbolic.svg
/usr/share/help/id/gnome-software/figures/scalable/symbolic/webpage-symbolic.svg
/usr/share/help/id/gnome-software/how-to-reinstall-a-web-app.page
/usr/share/help/id/gnome-software/index.page
/usr/share/help/id/gnome-software/legal.xml
/usr/share/help/id/gnome-software/software-licensing.page
/usr/share/help/id/gnome-software/software-metadata.page
/usr/share/help/pt_BR/gnome-software/figures/app-context-bar.png
/usr/share/help/pt_BR/gnome-software/figures/app-screenshot.png
/usr/share/help/pt_BR/gnome-software/figures/carousel.png
/usr/share/help/pt_BR/gnome-software/figures/install-webapp-from-gnome-web.png
/usr/share/help/pt_BR/gnome-software/figures/scalable/license-community-built.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/license-proprietary-and-special.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/license-unknown.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/links.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/no-links.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/symbolic/computer-fail-symbolic.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/symbolic/contact-symbolic.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/symbolic/donate-symbolic.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/symbolic/help-link-symbolic.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/symbolic/image-missing-symbolic.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/symbolic/translations-symbolic.svg
/usr/share/help/pt_BR/gnome-software/figures/scalable/symbolic/webpage-symbolic.svg
/usr/share/help/pt_BR/gnome-software/how-to-reinstall-a-web-app.page
/usr/share/help/pt_BR/gnome-software/index.page
/usr/share/help/pt_BR/gnome-software/legal.xml
/usr/share/help/pt_BR/gnome-software/software-licensing.page
/usr/share/help/pt_BR/gnome-software/software-metadata.page
/usr/share/help/sv/gnome-software/figures/app-context-bar.png
/usr/share/help/sv/gnome-software/figures/app-screenshot.png
/usr/share/help/sv/gnome-software/figures/carousel.png
/usr/share/help/sv/gnome-software/figures/install-webapp-from-gnome-web.png
/usr/share/help/sv/gnome-software/figures/scalable/license-community-built.svg
/usr/share/help/sv/gnome-software/figures/scalable/license-proprietary-and-special.svg
/usr/share/help/sv/gnome-software/figures/scalable/license-unknown.svg
/usr/share/help/sv/gnome-software/figures/scalable/links.svg
/usr/share/help/sv/gnome-software/figures/scalable/no-links.svg
/usr/share/help/sv/gnome-software/figures/scalable/symbolic/computer-fail-symbolic.svg
/usr/share/help/sv/gnome-software/figures/scalable/symbolic/contact-symbolic.svg
/usr/share/help/sv/gnome-software/figures/scalable/symbolic/donate-symbolic.svg
/usr/share/help/sv/gnome-software/figures/scalable/symbolic/help-link-symbolic.svg
/usr/share/help/sv/gnome-software/figures/scalable/symbolic/image-missing-symbolic.svg
/usr/share/help/sv/gnome-software/figures/scalable/symbolic/translations-symbolic.svg
/usr/share/help/sv/gnome-software/figures/scalable/symbolic/webpage-symbolic.svg
/usr/share/help/sv/gnome-software/how-to-reinstall-a-web-app.page
/usr/share/help/sv/gnome-software/index.page
/usr/share/help/sv/gnome-software/legal.xml
/usr/share/help/sv/gnome-software/software-licensing.page
/usr/share/help/sv/gnome-software/software-metadata.page

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gnome-software/libgnomesoftware.so.21
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_appstream.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_dpkg.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_dummy.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_fedora-langpacks.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_fedora-pkgdb-collections.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_flatpak.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_generic-updates.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_hardcoded-blocklist.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_icons.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_modalias.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_os-release.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_provenance-license.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_provenance.so
/V3/usr/lib64/gnome-software/plugins-21/libgs_plugin_repos.so
/VA/usr/lib64/gnome-software/libgnomesoftware.so.21
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_appstream.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_dpkg.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_dummy.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_fedora-langpacks.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_fedora-pkgdb-collections.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_flatpak.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_generic-updates.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_hardcoded-blocklist.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_icons.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_modalias.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_os-release.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_provenance-license.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_provenance.so
/VA/usr/lib64/gnome-software/plugins-21/libgs_plugin_repos.so
/usr/lib64/gnome-software/libgnomesoftware.so
/usr/lib64/gnome-software/libgnomesoftware.so.21
/usr/lib64/gnome-software/plugins-21/libgs_plugin_appstream.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_dpkg.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_dummy.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_fedora-langpacks.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_fedora-pkgdb-collections.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_flatpak.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_generic-updates.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_hardcoded-blocklist.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_icons.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_modalias.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_os-release.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_provenance-license.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_provenance.so
/usr/lib64/gnome-software/plugins-21/libgs_plugin_repos.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gnome-software-cmd
/V3/usr/libexec/gnome-software-restarter
/VA/usr/libexec/gnome-software-cmd
/VA/usr/libexec/gnome-software-restarter
/usr/libexec/gnome-software-cmd
/usr/libexec/gnome-software-restarter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-software/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-software.1

%files locales -f gnome-software.lang
%defattr(-,root,root,-)

