#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-software
Version  : 41.1
Release  : 59
URL      : https://download.gnome.org/sources/gnome-software/41/gnome-software-41.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-software/41/gnome-software-41.1.tar.xz
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
BuildRequires : clr-bundle-icons
BuildRequires : clr-bundle-screenshots
BuildRequires : docbook-xml
BuildRequires : gtk-doc
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
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(xmlb)
BuildRequires : source-highlight
BuildRequires : valgrind-dev
BuildRequires : zstd-dev

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
%setup -q -n gnome-software-41.1
cd %{_builddir}/gnome-software-41.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635541123
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfwupd=false \
-Dgtk_doc=false \
-Dmalcontent=false \
-Dpackagekit=false \
-Dpackagekit_autoremove=false \
-Drpm_ostree=false \
-Dsnap=false \
-Dsysprof=disabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-software
cp %{_builddir}/gnome-software-41.1/COPYING %{buildroot}/usr/share/package-licenses/gnome-software/4cc77b90af91e615a64ae04893fdffa7939db84c
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-software

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-software

%files data
%defattr(-,root,root,-)
/usr/share/app-info/xmls/org.gnome.Software.Featured.xml
/usr/share/applications/gnome-software-local-file.desktop
/usr/share/applications/org.gnome.Software.desktop
/usr/share/dbus-1/services/org.gnome.Software.service
/usr/share/glib-2.0/schemas/org.gnome.software.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Software-search-provider.ini
/usr/share/gnome-software/upgrade-bg.png
/usr/share/icons/hicolor/scalable/actions/app-remove-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/carousel-arrow-next-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/carousel-arrow-previous-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Software.svg
/usr/share/icons/hicolor/scalable/status/software-installed-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Software-symbolic.svg
/usr/share/metainfo/org.gnome.Software.Plugin.Flatpak.metainfo.xml
/usr/share/metainfo/org.gnome.Software.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-software/gnome-software.h
/usr/include/gnome-software/gs-app-collation.h
/usr/include/gnome-software/gs-app-list.h
/usr/include/gnome-software/gs-app.h
/usr/include/gnome-software/gs-appstream.h
/usr/include/gnome-software/gs-autocleanups.h
/usr/include/gnome-software/gs-category-manager.h
/usr/include/gnome-software/gs-category.h
/usr/include/gnome-software/gs-desktop-data.h
/usr/include/gnome-software/gs-enums.h
/usr/include/gnome-software/gs-external-appstream-utils.h
/usr/include/gnome-software/gs-icon.h
/usr/include/gnome-software/gs-ioprio.h
/usr/include/gnome-software/gs-key-colors.h
/usr/include/gnome-software/gs-metered.h
/usr/include/gnome-software/gs-odrs-provider.h
/usr/include/gnome-software/gs-os-release.h
/usr/include/gnome-software/gs-plugin-event.h
/usr/include/gnome-software/gs-plugin-job.h
/usr/include/gnome-software/gs-plugin-loader-sync.h
/usr/include/gnome-software/gs-plugin-loader.h
/usr/include/gnome-software/gs-plugin-types.h
/usr/include/gnome-software/gs-plugin-vfuncs.h
/usr/include/gnome-software/gs-plugin.h
/usr/include/gnome-software/gs-remote-icon.h
/usr/include/gnome-software/gs-utils.h
/usr/lib64/pkgconfig/gnome-software.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gnome\-software/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-software/libgnomesoftware.so
/usr/lib64/gnome-software/libgnomesoftware.so.16
/usr/lib64/gnome-software/plugins-16/libgs_plugin_appstream.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_dpkg.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_dummy.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_fedora-langpacks.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_fedora-pkgdb-collections.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_flatpak.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_generic-updates.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_hardcoded-blocklist.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_hardcoded-popular.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_icons.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_modalias.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_os-release.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_provenance-license.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_provenance.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_repos.so
/usr/lib64/gnome-software/plugins-16/libgs_plugin_rewrite-resource.so

%files libexec
%defattr(-,root,root,-)
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

